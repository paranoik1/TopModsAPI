<div align="center">

# 🚀 TopModsAPI 

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/github/license/paranoik1/TopModsAPI?style=for-the-badge)](LICENSE)

> API для доступа к базе модификаций с [top-mods.com](https://top-mods.com) без рекламы и лишних перенаправлений

![TopModsAPI Banner](./banner.jpg) <!-- Замените на реальный баннер -->

</div>

## ✨ Ключевые возможности

- 🔍 **Поиск модов** по играм, категориям и тегам
- ⚡ **Прямые ссылки** на скачивание (без рекламы)
- 📊 **Кэширование данных** для максимальной скорости
- 📱 **Оптимизированный JSON** для мобильных приложений
- 🔒 **Обход защиты** с помощью bypass TLS Fingerprint
- 📚 **Полная документация** Swagger/OpenAPI

## 🛠 Технологический стек


| Компонент | Описание |
|-----------|----------|
| FastAPI | Высокопроизводительный API-фреймворк |
| aiohttp | Асинхронные HTTP-запросы |
| Redis | Кэширование данных и сессий |
| BeautifulSoup | Парсинг HTML контента |
| curl_cffi | Обход TLS Fingerprint защиты |
| Docker | Контейнеризация приложения |

## 🚀 Быстрый старт

### Варианты развертывания:

#### 1. Docker Compose (рекомендуется)
```bash
git clone https://github.com/username/TopModsAPI.git
cd TopModsAPI
docker compose up -d
```

#### 2. Локальная установка
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker run -d --rm -p 127.0.0.1:32768:6379 redis
fastapi run src/main.py
```

После запуска API будет доступен на:  
http://localhost:8000  
Документация: http://localhost:8000/docs

## 📡 API Endpoints

### 🎮 Модификации
| Метод | Путь | Параметры | Описание |
|-------|------|-----------|----------|
| `GET` | `/mods` | `page`, `game`, `category`, `title`, `author`, `date_pub_from`, `date_pub_to` | Получение списка модов с фильтрацией |
| `GET` | `/mods/{mod_id}` | - | Детальная информация о моде |
| `GET` | `/download/{code}` | - | Скачивание файла мода |

### 🕹️ Игры
| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/games` | Список доступных игр |


## 🔍 Примеры запросов

```python
import requests

# Получить список игр
response = requests.get("http://localhost:8000/api/games")
print(response.json())

# Поиск модов по фильтрам
params = {"game": "melon-playground", "title": "Hell"}
response = requests.get("http://localhost:8000/api/mods", params=params)
```

## 🛡 TLS Fingerprint Bypass
Я использую [curl_cffi](https://github.com/lexiforest/curl_cffi) для обхода защиты сайта

## 🤝 Участие в разработке

1. Форкните репозиторий
2. Создайте ветку (`git checkout -b feature/AmazingFeature`)
3. Сделайте коммит (`git commit -m 'Add some AmazingFeature'`)
4. Запушьте изменения (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📜 Лицензия

Этот проект распространяется под лицензией MIT - подробности см. в файле [LICENSE](LICENSE).
