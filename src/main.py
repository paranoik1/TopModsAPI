from fastapi import FastAPI, HTTPException

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from aiohttp.http_exceptions import HttpBadRequest
from os.path import join
from contextlib import asynccontextmanager
from redis import asyncio as aioredis
from os import getenv

from src.parser import mods
from src.parser import games
from src.schemas import *
from src.utils import get_url_from_id, content_manager, get_streaming_response
from src.config import MODSFIRE_URL, EXPIRE_CACHE


@asynccontextmanager
async def lifespan(_: FastAPI):
    port = getenv("REDIS_PORT", "32768")
    host = getenv("REDIS_HOST", "localhost")

    redis = aioredis.from_url(f"redis://{host}:{port}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/mods", response_model=ResponseModList, description="Получение списка модификаций, отфильтрованных по заданным параметрам (страница, игра, категория).")
@cache(expire=EXPIRE_CACHE)
async def get_mod_list(
        page: int = 1,
        game: str = "",
        category: str = "",
        title: str = "",
        author: str = "",
        date_pub_from: str = "",
        date_pub_to: str = ""
):
    """
    - **page**: Номер страницы с результатами (по умолчанию 1).
    - **game**: Игра, для которой отображаются модификации (необязательный параметр).
    - **category**: Категория модификаций (необязательный параметр).

    Возвращает список объектов `ModShortInfo`, содержащих краткую информацию о модификациях.

    Если возникает ошибка `HttpBadRequest`, будет вызвано исключение `HTTPException` с кодом 404 и соответствующим сообщением.
    """
    try:
        filters = {
            "title": title,
            "mod_author": author,
            "date_pub[from]": date_pub_from,
            "date_pub[to]": date_pub_to
        }
        return await mods.get_mod_list(page, game, category, filters)
    except HttpBadRequest as ex:
        raise HTTPException(status_code=404, detail=ex.message)


@app.get("/mods/{mod_id}", response_model=ModInfo, description="Получение детальной информации о модификации по ее идентификатору.")
@cache(expire=EXPIRE_CACHE)
async def get_mod(mod_id: str):
    """
    - **mod_id**: Идентификатор модификации.

    Возвращает объект `ModInfo`, содержащий подробную информацию о модификации.

    Если возникает ошибка `HttpBadRequest`, будет вызвано исключение `HTTPException` с кодом 404 и соответствующим сообщением.
    """
    try:
        url = get_url_from_id(mod_id)
        return await mods.get_mod(url)
    except HttpBadRequest as ex:
        raise HTTPException(status_code=404, detail=ex.message)


@app.get("/download/{code}", description="Получение файла модификации для скачивания.")
async def download_file(code: str):
    """
    - **code**: Код модификации, используемый для формирования ссылки на скачивание.

    Возвращает streaming response, содержащий файл модификации.

    Если возникает ошибка `HttpBadRequest`, будет вызвано исключение `HTTPException` с кодом 404 и соответствующим сообщением.
    """
    url = join(MODSFIRE_URL, "d", code)

    try:
        response = await get_streaming_response(url)
    except HttpBadRequest as ex:
        raise HTTPException(status_code=404, detail=ex.message)

    return response


@app.get("/games", response_model=list[Game], description="Получение списка доступных игр.")
@cache(expire=EXPIRE_CACHE*7)
async def get_game_list():
    """
    Возвращает список объектов `Game`, содержащих информацию об играх.

    Если возникает ошибка `HttpBadRequest`, будет вызвано исключение `HTTPException` с кодом 404 и соответствующим сообщением.
    """
    try:
        return await games.get_games()
    except HttpBadRequest as ex:
        raise HTTPException(status_code=404, detail=ex.message)
