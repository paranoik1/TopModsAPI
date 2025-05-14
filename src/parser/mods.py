import yarl

from bs4 import BeautifulSoup, Tag
from aiohttp import ClientSession
from aiohttp.http_exceptions import HttpBadRequest
from urllib.parse import urlencode

from src.config import HEADERS, COOKIES, URL
from src.utils import get_mod_id
from src.utils import get_beautiful_soup, get_session


def __get_category(url):
    category = yarl.URL(url).parts[3]
    if ".html" in category:
        return None

    return category


def __get_image_url(soup: BeautifulSoup) -> str:
    return URL + soup.select_one("img.img-fluid")["src"]


def __get_title(soup: BeautifulSoup):
    return soup.select_one("div#controller_wrap.clr.float_right h1").text.strip()


def __get_description(soup: BeautifulSoup):
    description = soup.select_one("section#content-tab1.value").get_text()

    return description


def __get_download_code(soup: BeautifulSoup):
    url_page_generate_link = soup.select_one("div.download-anchor.text-left.down-redirect a")["href"]

    return url_page_generate_link.split("/")[-1]


def __get_game(url: str):
    return yarl.URL(url).parts[2]


@get_session(headers=HEADERS, cookies=COOKIES)
async def get_mod(url, session: ClientSession):
    soup = await get_beautiful_soup(url, session)
    await session.close()

    if not soup:
        raise HttpBadRequest("Not Found")

    download_code = __get_download_code(soup)
    image_url = __get_image_url(soup)
    title = __get_title(soup)
    description = __get_description(soup)
    category = __get_category(url)
    game = __get_game(url)
    mod_id = get_mod_id(url)

    return {
        "id": mod_id,
        "image_url": image_url,
        "title": title,
        "description": description,
        "download_code": download_code,
        "category": category,
        "game": game,
    }


def get_short_info_mod(mod: Tag) -> dict[str, str]:
    url = URL + mod.select_one("h2 > a")["href"]
    image_url = URL + mod.select_one("a > img")["src"]
    title = mod.find("h2").text.strip()
    description = mod.select_one("div.fields > div.field.ft_html.f_content > div.value").text.strip()
    category = __get_category(url)
    game = __get_game(url)
    mod_id = get_mod_id(url)

    return {
        "id": mod_id,
        "image_url": image_url,
        "title": title,
        "description": description,
        "category": category,
        "game": game,
    }


#title=pack&mod_author=p&date_pub[from]=01.07.2023&date_pub[to]=27.07.2024
@get_session(headers=HEADERS, cookies=COOKIES)
async def get_mod_list(
    page: int,
    game: str,
    category: str,
    filters: dict[str, str],
    session: ClientSession
) -> dict[str, list[dict[str, str]]]:
    url = URL

    if game:
        url += "/mods/" + game
        if category:
            url += "/" + category

    filters["page"] = str(page)
    query_params = urlencode(filters)
    url += "?" + query_params

    soup = await get_beautiful_soup(url, session)
    await session.close()

    if not soup:
        raise HttpBadRequest("Not Found")

    mod_list = soup.find("div", {"class": "content_list mods_list"}).find_all("div", {"class": "content_list_item"})

    items_quantity = soup.find("div", {"class": "pagebar_notice"})
    if items_quantity:
        quantity = int(items_quantity.get_text().split("of")[-1].strip())
    else:
        quantity = len(mod_list)

    result = {
        "items": quantity,
        "mods": []
    }
    for mod in mod_list:
        info = get_short_info_mod(mod)
        result["mods"].append(info)

    return result


if __name__ == "__main__":
    from pprint import pprint
    from asyncio import run

    res = run(get_mod_list(1, "melon-playground", "", {"title": ""}))
    pprint(res)
