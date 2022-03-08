import requests
import json

import youtube_dl

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

import config


class CreatePlaylist:
    def __init__(self):
        self.youtube_client = self.get_youtube_client()

    def get_youtube_client(self):
        """ Log Into Youtube """
        flow = InstalledAppFlow.from_client_config(config.CLIENT_CONFIG, config.SCOPES)
        credentials = flow.run_local_server()
        try:
            youtube_client = build(config.API_SERVICE_NAME, config.API_VERSION, credentials=credentials)
            return youtube_client
        except HttpError as e:
            print(e)

    def get_liked_video_info(self):
        """ Grab info about the last liked video """
        request = self.youtube_client.videos().list(
            part="snippet,contentDetails,statistics",
            myRating="like"
        )
        response = request.execute()

        last_video = response["items"][0]
        youtube_url = f'https://www.youtube.com/watch?v={last_video["id"]}'

        video_info = youtube_dl.YoutubeDL({}).extract_info(youtube_url, download=False)
        title = video_info["title"].split('-')
        artist = title[0]
        track = title[1]

        if track is not None and artist is not None:
            song_info = {"track": track, "artist": artist}
            return song_info

    def create_playlist(self):
        """ Create a new playlist and return its id """
        request_body = json.dumps({
            "name": "Youtube Music",
            "description": "Music that I found on Youtube",
            "public": True
        })

        query = f'https://api.spotify.com/v1/users/{config.SPOTIFY_USER_ID}/playlists'
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {config.SPOTIFY_TOKEN}"
            }
        )
        response_json = response.json()
        return response_json["id"]

    def get_spotify_uri(self, track, artist):
        """ Search for the song and return uri """
        query = f'https://api.spotify.com/v1/search?q=track%3A{track}+artist%3A{artist}&type=track&offset=0&limit=5'
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {config.SPOTIFY_TOKEN}"
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]
        uri = songs[0]["uri"]
        return uri

    def add_song_to_playlist(self):
        """ Get the liked video and add it to a playlist """
        song_info = self.get_liked_video_info()
        song_uri = self.get_spotify_uri(song_info["track"], song_info["artist"])
        playlist_id = self.create_playlist()
        request_data = {"uris":[song_uri], "position":0}

        query = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

        response = requests.post(
            query,
            data=json.dumps(request_data),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {config.SPOTIFY_TOKEN}"
            }
        )

        if response.status_code != 200:
            return response.status_code

        response_json = response.json()
        return response_json


if __name__ == '__main__':
    cp = CreatePlaylist()
    cp.add_song_to_playlist()
