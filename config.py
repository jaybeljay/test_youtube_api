import os

CLIENT_CONFIG = {"web": {
                      "client_id": os.getenv('CLIENT_ID'),
                      "project_id": os.getenv('PROJECT_ID'),
                      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                      "token_uri": "https://oauth2.googleapis.com/token",
                      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                      "client_secret": os.getenv('CLIENT_SECRET'),
                      "redirect_uris": ["http://localhost:8080/"],
                      "key": os.getenv('YOUTUBE_TOKEN')}}

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
SPOTIFY_USER_ID = os.getenv('SPOTIFY_USER_ID')
SPOTIFY_TOKEN = os.getenv('SPOTIFY_TOKEN')
