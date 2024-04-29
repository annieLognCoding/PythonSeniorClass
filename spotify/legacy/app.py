from flask import Flask, request, redirect, jsonify

import requests
import secrets
import json
import base64


app = Flask(__name__)

client_id = secrets.client_id()
client_secret = secrets.client_secret()
redirect_uri = 'http://localhost:8888/callback'
user_id = secrets.spotify_user_id()


def generate_random_string(length):
    import random, string
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(length))

@app.route('/login')
def login():
    state = generate_random_string(16)
    scope = 'user-read-private user-read-email playlist-modify-public'
    auth_url = f"https://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&scope={scope}&redirect_uri={redirect_uri}&state={state}"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    if state is None:
        return redirect(f'/#error=state_mistmatch')
    else:
        auth_response = exchange_code_for_token(code)
        return jsonify(auth_response)
    
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

#flask run --port 8888