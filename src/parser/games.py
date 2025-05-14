import asyncio

from aiohttp import ClientSession
from os.path import join

from src.config import URL, HEADERS, COOKIES
from src.utils import get_session, get_beautiful_soup


async def get_categories(session, game_uid):
    url = join(URL, "mods", game_uid)
    soup = await get_beautiful_soup(url, session)
    if not soup:
        raise ValueError("Error: not get categories in game: " + game_uid)
    
    categories_tags = soup.select("div.gui-panel.content_categories > ul > li")
    categories = []
    for tag in categories_tags:
        title = tag.find("a").text.strip()
        translit_title = tag["class"][0].replace(game_uid + "-", "")

        categories.append({
            "title": title,
            "translit_title": translit_title
        })

    return categories


async def get_game(game_tag, session):
    title = game_tag.find("a").text.strip()
    translit_title = game_tag["class"][0]
    categories = await get_categories(session, translit_title)

    return {
        "title": title,
        "categories": categories,
        "translit_title": translit_title
    }


@get_session(headers=HEADERS, cookies=COOKIES)
async def get_games(session: ClientSession):
    soup = await get_beautiful_soup(URL, session)
    if not soup:
        raise ValueError("Error: not get beautiful soup class")

    tasks = []
    game_tags = soup.select("div.gui-panel.content_categories.categories_small > ul > li")

    for game_tag in game_tags:
        task = get_game(game_tag, session)
        tasks.append(task)
    
    return await asyncio.gather(*tasks)
