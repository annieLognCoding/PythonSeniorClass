import json
import pprint
import requests
import secrets

class lastFmSpotify:
    def __init__(self):
        self.token = secrets.get_newToken()
        self.api_key = secrets.last_fm_api_key()
        self.user_id = secrets.spotify_user_id()
        self.headers = {"Content-Type": 'application/json',
                        "Authorization": f"Bearer {self.token}"}
        self.playlist_id = self.get_playlist_id()
        self.song_info = {}
        self.uris = []

    def fetch_songs_from_lastfm(self):
        params = {'limit': 20, 'api_key': self.api_key}
        url = f'https://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&format=json'
        response = requests.get(url, params = params)
        res = response.json()

        for item in res['tracks']['track']:
            song = item['name']
            artist = item['artist']['name']
            self.song_info[song] = artist
        
    def get_uri_from_spotify(self):
        for (song, artist) in self.song_info.items():
            url=f"https://api.spotify.com/v1/search?query=track%3A{song}+artist%3A{artist}&type=track&offset=0&limit=10"
            response = requests.get(url, headers=self.headers)
            res = response.json()
            uri = res["tracks"]["items"][0]["uri"]
            self.uris.append(uri)
        print(self.uris)

    def create_spotify_playlist(self):
        data = {
            "name": "Last FM top 20",
            "description": "New playlist description",
            "public": True
        }
        data = json.dumps(data)
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = requests.post(url, data = data, headers=self.headers)
        if response.status_code == 201:
            print("Spotify successfully created playlist")
            res = response.json()
            self.playlist_id = res['id']
        else:
            print(response.content)
    
    def get_playlist_id(self):
        url = f'https://api.spotify.com/v1/users/{self.user_id}/playlists'
        response = requests.get(url, headers=self.headers)
        res = response.json()
        for item in res['items']:
            if(item['name'] == 'Last FM top 20'):
                return item['id']
    
    def add_songs_to_playlist(self):
        data = {
            "uris": self.uris,
            "position": 0
        }
        data = json.dumps(data)
        url = f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks"
        response = requests.post(url, headers = self.headers, data = data)
        if response.status_code == 201:
            print("Successfully added songs to playlist")
        else:
            print(response.content)


        

d = lastFmSpotify()
# print(d.token)
# d.fetch_songs_from_lastfm()
# d.get_uri_from_spotify()
# d.create_spotify_playlist()
print(d.playlist_id)
# d.add_songs_to_playlist()