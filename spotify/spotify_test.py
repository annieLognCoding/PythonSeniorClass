import json
import pprint
import requests
import secrets
import base64

class lastFmSpotify:
    def __init__(self):
        self.token = secrets.get_newToken()
        self.api_key = secrets.last_fm_api_key()
        self.user_id = secrets.spotify_user_id()
        self.headers = {"Content-Type": 'application/json',
                        "Authorization": f"Bearer {self.token}"}
        self.playlist_id = secrets.get_playlist_id()
        self.song_info = {}
        self.uris = []

    def fetch_songs_from_lastfm(self):
        params = {'limit': 20, 'api_key': self.api_key, 'format': 'json', }
        url = f'https://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&format=json'
        response = requests.get(url, params = params)
        try:
            res = response.json()
            for item in res['tracks']['track']:
                song = item['name']
                artist = item['artist']['name']
                self.song_info[song] = artist
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error occured: {e}")
        except requests.exceptions.RequestException as e:
            print(f"REQUEST Error occured: {e}")
        except ValueError as e:
            print(f"VALUE Error occured: {e}")
            
    def get_uri_from_spotify(self):
        for (song, artist) in self.song_info.items():
            url=f"https://api.spotify.com/v1/search?query=track%3A{song}+artist%3A{artist}&type=track&offset=0&limit=1"
            response = requests.get(url, headers=self.headers)
            res = response.json()
            uri = res["tracks"]["items"][0]["uri"]
            self.uris.append(uri)
        print(self.uris)
    
    def create_spotify_playlist(self):
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        payload = {
            "name": "Last fm Top 20 Playlist",
            "description": "Made with my own Spotify API!",
            "public": True
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        res = response.json()
        print(res["id"])
        self.playlist_id = res["id"]

        

d = lastFmSpotify()
d.fetch_songs_from_lastfm()
d.get_uri_from_spotify()
# d.create_spotify_playlist()
# d.add_songs_to_playlist()





