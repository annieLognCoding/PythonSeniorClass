from flask import Flask, redirect, request, render_template, jsonify
import requests, my_secrets, base64
import numpy as np

app = Flask(__name__)

client_id = my_secrets.client_id()
client_secret = my_secrets.client_secret()
redirect_uri = 'http://localhost:8888/callback'
refresh_token = ''


def generate_random_string(length):
    import random, string
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(length))

@app.route("/")
def get_access():

  state = generate_random_string(16)
  scope = 'playlist-read-private playlist-read-collaborative user-read-private user-read-email'

  params = {
     'response_type': 'code',
     'client_id': client_id,
     'scope': scope,
     'redirect_uri': redirect_uri,
     'state': state
  }

  return redirect('https://accounts.spotify.com/authorize?' + requests.compat.urlencode(params))

@app.route('/callback')
def callback():
    global refresh_token
    code = request.args.get('code')
    state = request.args.get('state')

    if state == None:
        return redirect(f'/#error=state_mismatch')
    else:
      res = exchange_code_for_token(code)
      refresh_token = res['refresh_token']
      playlists = get_playlists()
      print(playlists)

      return refresh_token

def exchange_code_for_token(code):
    url = 'https://accounts.spotify.com/api/token'
    headers = {
       'content-type': 'application/x-www-form-urlencoded',
       'Authorization': 'Basic ' + base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
    }
    params = {
       'code': code,
       'redirect_uri': redirect_uri,
       'grant_type': 'authorization_code'
    }
    
    response = requests.post(url, headers=headers, params=params)
    return response.json()

def get_playlists():
    access_token = my_secrets.get_newToken(refresh_token)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    url = 'https://api.spotify.com/v1/me'
    response = requests.get(url, headers = headers)
    res = response.json()
    user_id = res['id']
    url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
    
 
    response = requests.get(url, headers = headers)
    res = response.json()
    playlists = []
    for item in res['items']:
        playlists.append({'name': item['name'], 'id': item['id']})
    return playlists

def get_first_playlist_tracks():
    try:
        global refresh_token
        token = my_secrets.get_newToken(refresh_token)
        headers = {
            "Content-Type": 'application/json',
            "Authorization": f"Bearer {token}"
        }
        
        # Retrieve the user's playlists
        playlists = get_playlists()
        
        # Extract the ID of the first playlist
        first_playlist_id = playlists[0]["id"]

        # Fetch the tracks from the first playlist
        """
            IMPLEMENT YOUR CODE HERE
        """

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8888)
