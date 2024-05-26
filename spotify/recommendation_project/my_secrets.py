import base64, requests
def spotify_user_id():
    return '31bymk7hg5t4ej2hxc4m76abxcoy'

def last_fm_api_key():
    return 'f16cd08c7639f56ecfdfafd183c1b621'

def refresh_token():
    return 'AQBwXjYe_lyP6KmnEUl4vvCpazKH4JapZX4hvy5dsSz5IZ7yna66W6F-U0pne66CnEiS_9GSZsIn8J5-fRoGN4SDJUuYhoro22BuAf6fAdMNHRzCsOMEBqkKhV_WC4im5W4'

def client_id():
    return '886e7c52a19141c6b84e98e0d45c5ddd'

def client_secret():
    return 'e38a2ec9b47d43b1ba1457f697b7e6f9'

def spotify_token():
    id = client_id()
    secret = client_secret()
    url = "https://accounts.spotify.com/api/token"
    payload = {
            "grant_type": 'client_credentials',
            "client_id": id,
            "client_secret": secret
        }

    response = requests.post(url, headers={'content-type': 'application/x-www-form-urlencoded'}, data=payload)
    res = response.json()
    access_token = res['access_token']
    return access_token


def get_newToken(refreshToken):
    url = "https://accounts.spotify.com/api/token"

    # Headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + base64.b64encode(f'{client_id()}:{client_secret()}'.encode()).decode()
    }

    # Body data
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refreshToken
    }

    # Making the POST request
    response = requests.post(url, headers=headers, data=data)
    print(response)
    res = response.json()
    # Print the response text (or process it in other ways)
    return res["access_token"]

def get_playlist_id():
    url = f"https://api.spotify.com/v1/me/playlists"
    response = requests.get(url, headers = {"Content-Type": 'application/json',
                        "Authorization": f"Bearer {get_newToken()}"})
    res = response.json()
    for item in res["items"]:
        if item["name"] == "Last fm Top 20 Playlist":
            return item["id"]