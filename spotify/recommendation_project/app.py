from flask import Flask, redirect, request, render_template, jsonify
import requests, my_secrets, base64
import numpy as np

app = Flask(__name__)

client_id = my_secrets.client_id()
client_secret = my_secrets.client_secret()
access_token = my_secrets.spotify_token()
redirect_uri = "http://localhost:8888/callback"
refresh_token = ""

def generate_random_string(length):
    import random, string
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(length))

@app.route("/")
def home():
    return render_template(f'index.html')

@app.route("/" , methods=['POST'])
def get_access():
    
    state = generate_random_string(16);
    scope = 'playlist-read-private playlist-read-collaborative user-read-private user-read-email';

    params = {
        'response_type': 'code',
        'client_id': client_id,
        'scope': scope,
        'redirect_uri': redirect_uri,
        'state': state
    }
    url = 'https://accounts.spotify.com/authorize?' + requests.compat.urlencode(params)
    return redirect(url)

@app.route('/playlists')
def get_playlists():
    try:
        global refresh_token
        token = my_secrets.get_newToken(refresh_token)
        url = "https://api.spotify.com/v1/me"
        headers = {
            "Content-Type": 'application/json',
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)
        res = response.json()
        user_id = res["id"]
        url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
        headers = {
            "Content-Type": 'application/json',
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)
        res = response.json()
        playlists = []
        for item in res["items"]:
            playlists.append({"name": item["name"], "id": item["id"]})
        return render_template('playlists.html', names = playlists)
    except:
        return redirect("/")

@app.route('/callback')
def callback():
    global refresh_token
    code = request.args.get('code')
    state = request.args.get('state')
    if state is None:
        return redirect(f'/#error=state_mistmatch')
    else:
        auth_response = exchange_code_for_token(code)
        refresh_token = auth_response["refresh_token"]
        return redirect("/playlists")
    
def exchange_code_for_token(code):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
      }
    
    payload = {
        "code": code,
        "redirect_uri": redirect_uri,
        "grant_type": 'authorization_code'
    }

    response = requests.post(url, headers = headers, data=payload)
    return response.json()

def analyze_features(features):
    """ Analyze and average the audio features of the playlist. """
    feature_keys = ['danceability', 'energy', 'valence', 'acousticness', 'tempo']
    averages = {key: np.mean([f[key] for f in features if key in f]) for key in feature_keys}
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

# Example feature averages
features = {'danceability': 0.6297, 'energy': 0.5645, 'valence': 0.4323, 'acousticness': 0.2789, 'tempo': 131.697}
tags = derive_tags(features)

print("Derived Tags:", tags)


def get_lastfm_recommendations(tags, lastfm_api_key):
    recommendations = []
    for tag in tags:
        url = f"http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={tag}&api_key={lastfm_api_key}&format=json&limit=5"
        response = requests.get(url)
        top_tracks = response.json().get('tracks', {}).get('track', [])
        for track in top_tracks:
            song_name = track['name']
            artist_name = track['artist']['name']
            spotify_url = track['url']
            recommendation = f"{song_name} - {artist_name}"
            item = {"name": recommendation, "url": spotify_url}
            if item not in recommendations:
                recommendations.append({"name": recommendation, "url": spotify_url})
    return list(recommendations)[:10]


@app.route('/recommend', methods=["POST"])
def recommend_songs():
    try:
        global refresh_token
        token = my_secrets.get_newToken(refresh_token)
        playlist_id = request.form['playlist_id']
        headers = {
            "Content-Type": 'application/json',
            "Authorization": f"Bearer {token}"
        }
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
        response = requests.get(url, headers=headers)
        res = response.json()
        features = []
        for item in res["items"]:
            try:
                track = item["track"]
                track_id = track["id"]
                url = f'https://api.spotify.com/v1/audio-features/{track_id}'
                response_call = requests.get(url, headers=headers)
                res_call = response_call.json()
                features.append(res_call)
            except:
                continue
        averages = analyze_features(features)
        tags = derive_tags(averages)
        lastfm_api_key = my_secrets.last_fm_api_key()
        recommendations = get_lastfm_recommendations(tags, lastfm_api_key)
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8888)