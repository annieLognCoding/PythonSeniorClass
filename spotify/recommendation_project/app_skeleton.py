from flask import Flask, redirect, request, render_template, jsonify
import requests, my_secrets, base64, pprint, random
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
        audio_features = get_audio_features()
        averages = analyze_features(audio_features)
        tags = derive_tags(averages)
        recommendations = get_recommendation(tags)
        return recommendations

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
            "Authorization": f"Bearer {token}"
        }
        
        # Retrieve the user's playlists
        playlists = get_playlists()
        
        # Extract the ID of the first playlist
        first_playlist_id = playlists[0]["id"]

        # Fetch the tracks from the first playlist
        url = f'https://api.spotify.com/v1/playlists/{first_playlist_id}/tracks'
        response = requests.get(url, headers = headers)
        res = response.json()
        tracks = []
        for item in res['items']:
            tracks.append({'track': item['track']['name'], 'id': item['track']['id']})
        return tracks

    except Exception as e:
        return jsonify({"error": str(e)}), 400

def get_audio_features():
    try:
        global refresh_token
        token = my_secrets.get_newToken(refresh_token)
        headers = {
            "Authorization": f"Bearer {token}"
        }

        tracks = get_first_playlist_tracks()
        ids = ''
        for track in tracks:
            id = track['id']
            ids += id + ','
        ids = ids[:-1]

        url = f'https://api.spotify.com/v1/audio-features?ids={ids}'
        response = requests.get(url, headers = headers)
        res = response.json()
        return res['audio_features']
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def analyze_features(audio_features):
    feature_keys = ['danceability', 'energy', 'valence', 'acousticness', 'tempo']
    averages = {key: np.mean([f[key] for f in audio_features if key in f]) for key in feature_keys}
    return averages

def derive_tags(features):
    """ Derive more nuanced tags from audio features. """
    tags = []
    # Danceability
    if features['danceability'] > 0.7:
        tags.extend(['dance', 'electronic', 'house'])
    elif features['danceability'] > 0.5:
        tags.extend(['pop', 'hip-hop'])
    
    # Energy
    if features['energy'] > 0.8:
        tags.extend(['rock', 'metal', 'workout'])
    elif features['energy'] > 0.6:
        tags.extend(['party', 'dance'])
    elif features['energy'] < 0.4:
        tags.extend(['chill', 'ambient'])

    # Valence
    if features['valence'] > 0.75:
        tags.extend(['happy', 'uplifting', 'summer'])
    elif features['valence'] < 0.3:
        tags.extend(['sad', 'melancholic'])

    # Acousticness
    if features['acousticness'] > 0.5:
        tags.extend(['acoustic', 'folk', 'singer-songwriter'])
    elif features['acousticness'] < 0.1:
        tags.extend(['electronic', 'synth'])

    # Tempo
    if features['tempo'] > 140:
        tags.extend(['fast-tempo', 'drum and bass'])
    elif features['tempo'] < 100:
        tags.extend(['slow-tempo', 'ballad'])

    return list(set(tags))  # Remove duplicates if any

def get_recommendation(tags):
    limit = 15 // len(tags)
    leftOver = 15 % len(tags)
    recommendations = []
    count = 1
    for tag in tags:
        url = f'https://ws.audioscrobbler.com/2.0/?method=tag.gettopalbums&tag={tag}&api_key={my_secrets.last_fm_api_key()}&format=json&limit={limit}'
        response = requests.get(url)
        res = response.json()
        albums = res['albums']
        for album in albums['album']:
            recommendations.append({'name': album['name'], 'artist': album['artist']['name'], 'url': album['url'], 'count': count})
            count += 1
    
    for i in range(leftOver):
        index = int(random.random() * len(tags))
        url = f'https://ws.audioscrobbler.com/2.0/?method=tag.gettopalbums&tag={tags[index]}&api_key={my_secrets.last_fm_api_key()}&format=json&limit=1'
        response = requests.get(url)
        res = response.json()
        albums = res['albums']
        for album in albums['album']:
            recommendations.append({'name': album['name'], 'artist': album['artist']['name'], 'url': album['url'], 'count': count})
            count += 1
    
    return recommendations

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8888)
