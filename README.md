# Youtube2Spotify
Скрипт берет последнее из понравившихся на Youtube видео и добавляет его в плейлист на Spotify.
# Настройка
1. Установить зависимости.
 pip install -r requirements.txt
2. Настроить переменные окружения:
  Данные переменные можно взять из файла client_secrets.json, который генерируется после Oauth авторизации на Youtube: CLIENT_ID, PROJECT_ID, CLIENT_SECRET, REDIRECT_URIS.
  YOUTUBE_TOKEN - Youtube API Key.
  SPOTIFY_USER_ID и SPOTIFY_TOKEN - Spotify.
3. Запустить скрипт
  python create_playlist.py
 # Технологии
* Youtube Data API v3
* Spotify Web API
* Requests Library v 2.27.1
* Youtube_dl v 2021.12.17
