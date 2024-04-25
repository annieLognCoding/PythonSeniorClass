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
        self.playlist_id = '0EB4HyuAaaidTOHR6ilIZX'
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
            
    def get_uri_from_spotify(self):
        for (song, artist) in self.song_info.items():
            url=f"https://api.spotify.com/v1/search?query=track%3A{song}+artist%3A{artist}&type=track&offset=0&limit=10"
            response = requests.get(url, headers=self.headers)
            res = response.json()
            uri = res["tracks"]["items"][0]["uri"]
            self.uris.append(uri)
        print(self.uris)
        
d = lastFmSpotify()
# d.fetch_songs_from_lastfm()
# d.get_uri_from_spotify()
# d.create_spotify_playlist()
# d.add_songs_to_playlist()
url = f"https://api.spotify.com/v1/me/playlists"
response = requests.get(url, headers = d.headers)
res = response.json()
print(response.content)
for item in res["items"]:
    if item["name"] == "Last FM top 20":
        print(item["id"])



refreshToken = secrets.refresh_token()
url = "https://accounts.spotify.com/api/token"

payload = {
    "method": 'POST',
    "headers": {
    'Content-Type': 'application/x-www-form-urlencoded'
    },
    "body": new URLSearchParams({
    "grant_type": 'refresh_token',
    "refresh_token": refreshToken,
    "client_id": clientId
    }),
}

body = requests.get(url, payload);
response = body.json();
