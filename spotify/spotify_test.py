import json
import pprint
import requests
import secrets

class lastFmSpotify:
    def __init__(self):
        self.token = secrets.spotify_token()
        self.api_key = secrets.last_fm_api_key()
        self.user_id = secrets.spotify_user_id()
        self.headers = {"Content-Type": 'application/json',
                        "Authorization": f"Bearer {self.token}"}
        self.playlist_id = ''
        self.song_info = {}
        self.uris = []

    def fetch_songs_from_lastfm(self):
        params = {'limit': 20, 'api_key': self.api_key}
        url = f'https://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&format=json'
        response = requests.get(url, params = params)
        res = response.json()
        for item in res['tracks']['track']:
            song = item['name']
            print(song)



    #     if response.status_code != 200:
    #         print("ERROR")
    #     res = response.json()
    #     for item in res['tracks']['track']:
    #         song = item['name'].title()
    #         artist = item['artist']['name']
    #         self.song_info[song] = artist
    #     self.get_uri_from_spotify()

    # def get_uri_from_spotify(self):
    #     for song_name, artist in self.song_info.items():
    #         url = f"https://api.spotify.com/v1/search?query=track%3A{song_name}+artist%3A{artist}&type=track&offset=0&limit=10"
    #         response = requests.get(url, headers = self.headers)
    #         print(response.status_code)
    #         res = response.json()
    #         output_uri = res['tracks']['items']
    #         #print(output_uri[0])
    #         self.uris.append(output_uri[0]["uri"])

    # def create_spotify_playlist(self):
    #     data = {
    #         "name": "LastFM top songs",
    #         "description": "songs from the top tracks",
    #         "public": True
    #     }
    #     data = json.dumps(data)
    #     url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
    #     response = requests.post(url, data = data, headers=self.headers)
    #     if response.status_code == 201:
    #         print("Spotify successfully created playlist")
    #         res = response.json()
    #         self.playlist_id = res['id']
    #     else:
    #         print(response.content)

    # def add_songs_to_playlist(self):
    #     uri_list = json.dumps(self.uris)
    #     url = f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks"
    #     response = requests.post(url, data = uri_list, headers=self.headers)
    #     print(response.status_code, response.content)
    #     if response.status_code == 201:
    #         print("Song added successfully")

    # def list_songs_in_playlist(self):
    #     pass

d = lastFmSpotify()
d.fetch_songs_from_lastfm()
# d.create_spotify_playlist()
# d.add_songs_to_playlist()
