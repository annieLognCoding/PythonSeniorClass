import base64, requests
def spotify_user_id():
    return '31bymk7hg5t4ej2hxc4m76abxcoy'

def spotify_token():
    return 'BQBu4KiqBVIXinW7hFptnSuwU6hHNLlW6Obxdkd7qztn6meK1R8JooY8IN_dxwdqsewhZT_u4m6TVm6GOUemTaZLD7Qryuu5PiHv3bnwv31C_EMqzCC7d0mM8pMUusOom0-sbrb9KLhBtV4oCeWq4AjqnOJD-gOrnGICimqvwvmq_gUcko2_P1wd3963768cAmO6kF_S6_Q0874to-5fT-md6kvVXKNHr5sKmBjLCc2YYYc5BVM'

def last_fm_api_key():
    return 'f16cd08c7639f56ecfdfafd183c1b621'

def refresh_token():
    return 'AQBwXjYe_lyP6KmnEUl4vvCpazKH4JapZX4hvy5dsSz5IZ7yna66W6F-U0pne66CnEiS_9GSZsIn8J5-fRoGN4SDJUuYhoro22BuAf6fAdMNHRzCsOMEBqkKhV_WC4im5W4'

def client_id():
    return '886e7c52a19141c6b84e98e0d45c5ddd'

def client_secret():
    return 'e38a2ec9b47d43b1ba1457f697b7e6f9'

def get_newToken():
    refreshToken = refresh_token()
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
    res = response.json()
    # Print the response text (or process it in other ways)
    return res["access_token"]
