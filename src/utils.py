import yarl

from os.path import join

from aiohttp import ClientSession
from bs4 import BeautifulSoup
from aiohttp.http_exceptions import HttpBadRequest
from starlette.responses import StreamingResponse
from curl_cffi import AsyncSession, BrowserType, Headers, Response as CuffiResponse

from src.config import COOKIES, HEADERS, URL, MOD_ID_SEPARATOR


def get_session(headers: dict = None, cookies: dict = None):
    if not headers: headers = dict()
    if not cookies: cookies = dict()

    def decorator(func):
        async def wrapper(*args, **kwargs):
            session = ClientSession(headers=headers, cookies=cookies)
            try:
                res = await func(*args, **kwargs, session=session)
            except HttpBadRequest as e:
                await session.close()
                raise e
            
            if not session.closed:
                await session.close()

            return res
            
        return wrapper
    return decorator


async def get_beautiful_soup(url: str, session: ClientSession):
    async with session.get(url) as response:
        if response.status != 200:
            print(response)
            return None
        
        content = await response.text()
        
    return BeautifulSoup(content, "html.parser")


def get_mod_id(url: str) -> str:
    _, relative_url = url.split("/mods/")

    mod_id = relative_url.replace("/", MOD_ID_SEPARATOR)
    mod_id = mod_id.replace(".html", "")

    return mod_id


def get_url_from_id(mod_id: str) -> str:
    relative_url = mod_id.replace(MOD_ID_SEPARATOR, "/")
    
    return join(URL, "mods", relative_url + ".html")


# async def get_curl_response_headers(url: str):
#     proc = await asyncio.create_subprocess_shell(
#         CURL_COMMAND_HEADERS.format(url=url),
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE)

#     stdout, _ = await proc.communicate()

#     response_lines = stdout.decode().split("\n")
#     status_code = ""
#     headers = {}

#     for line in response_lines:
#         if "HTTP/" in line:
#             status_code = line.split()[1]
#         elif ":" in line:
#             key, value = line.split(":", 1)
#             headers[key.strip()] = value.strip()


#     return headers, status_code


# async def get_curl_stdout_file_content(url: str):
#     proc = await asyncio.create_subprocess_shell(
#         CURL_COMMAND.format(url=url),
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE)

#     return proc.stdout


# async def get_streaming_response(url: str):
#     response_headers, status_code = await get_curl_response_headers(url)
#     if status_code not in ["403", "200"]:
#         raise HttpBadRequest("Not Found")

#     async def read_bytes():
#         stdout_content_file = await get_curl_stdout_file_content(url)

#         while True:
#             content = await stdout_content_file.read(4096)

#             if not content:
#                 break

#             yield content

#     filename = yarl.URL(response_headers.get("location")).name

#     if filename == "d.php":
#         print("stream resp")
#         response_headers["content-type"] = "application/octet-stream"
#         response = StreamingResponse(read_bytes(), headers=response_headers)
#     else:
#         print("redirect resp")
#         # response_headers["Content-Disposition"] = "attachment; filename=" + filename
#         response = RedirectResponse(response_headers["location"], status_code=302, headers=response_headers)

#     return response


async def get_streaming_response(url: str):
    session = AsyncSession(headers=HEADERS, cookies=COOKIES, impersonate=BrowserType.chrome110)

    try:
        response, response_headers = await get_response_file(url, session)
    except HttpBadRequest as ex:
        await session.close()
        raise ex

    return StreamingResponse(
        content_manager(session, response), 
        headers=response_headers
    )
    

async def get_response_file(url, session: AsyncSession) -> tuple[CuffiResponse, Headers]:
    response: CuffiResponse = await session.get(url, allow_redirects=True, stream=True)

    if response.status_code != 200:
        raise HttpBadRequest(f"Not Found - {response.status_code}")

    filename = yarl.URL(response.url).name
    response_headers = response.headers
    
    if filename != "d.php":
        response_headers["Content-Disposition"] = "attachment; filename=" + filename
    
    response_headers["Content-Type"] = "application/octet-stream"
    
    return response, response_headers


async def content_manager(session: AsyncSession, response: CuffiResponse):
    async for chunk in response.aiter_content(1024*4):
        yield chunk

    response.close()
    await session.close()
