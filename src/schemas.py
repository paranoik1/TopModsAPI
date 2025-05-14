from pydantic import BaseModel


class ModShortInfo(BaseModel):
    """
    Модель, представляющая краткую информацию о модификации.

    - **id**: Идентификатор модификации.
    - **game**: Игра, для которой предназначена модификация.
    - **title**: Название модификации.
    - **image_url**: URL изображения модификации.
    - **description**: Описание модификации.
    - **category**: Категория модификации (необязательный параметр).
    """
    id: str
    game: str
    title: str
    image_url: str
    description: str
    category: str | None


class ResponseModList(BaseModel):
    """
    Модель ответа для /mods

    - **items** - кол-во модов найденных по фильтрам
    - **mods** - список модов
    """
    items: int
    mods: list[ModShortInfo]


class ModInfo(ModShortInfo):
    """
    Модель, представляющая подробную информацию о модификации.
    Наследуется от `ModShortInfo`.

    - **download_code**: Код модификации, используемый для скачивания файла.
    """
    download_code: str


class Category(BaseModel):
    """
    Модель, представляющая информацию о категории модификаций.

    - **title**: Название категории.
    - **translit_title**: Транслитерированное название категории.
    """
    title: str
    translit_title: str


class Game(BaseModel):
    """
    Модель, представляющая информацию об игре.

    - **title**: Название игры.
    - **translit_title**: Транслитерированное название игры.
    - **categories**: Список категорий модификаций, доступных для данной игры.
    """
    title: str
    translit_title: str
    categories: list[Category]
