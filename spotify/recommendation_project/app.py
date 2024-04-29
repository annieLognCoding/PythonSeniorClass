from flask import Flask, redirect, request, render_template
import requests, my_secrets, base64
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
        features = {}
        for item in res["items"]:
            try:
                track = item["track"]
                id = track["id"]
                url = f'https://api.spotify.com/v1/audio-features/{id}'
                response_call = requests.get(url, headers=headers)
                res_call = response_call.json()
                features[track["name"]] = res_call
            except:
                continue
        return features
    except Exception as e:
        return redirect("/")
    

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8888)