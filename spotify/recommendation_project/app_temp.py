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
    scope = 'user-read-private user-read-email'
    url = f'https://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&scope={scope}&redirect_uri={redirect_uri}&state={state}'

    return redirect(url)


@app.route("/callback")
def callback():
    global refresh_token
    code = request.args.get('code')
    state = request.args.get('state')
    if state == None:
       return redirect('#/error=state_mismatch')
    else:
       res = exchange_code_for_token(code)
       print(res)
       refresh_token = res['refresh_token']
       return refresh_token

def exchange_code_for_token(code):
    url = 'https://accounts.spotify.com/api/token'

    params = {
        'code': code,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }

    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'Authorizaiton': 'Basic ' + base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
    }

    response = requests.post(url, params=params, headers=headers)
    return response.json()

if __name__=="__main__":
   app.run(debug=True, host="0.0.0.0", port="8888")


def get_playlist():
   access_token = my_secrets.get_newToken(refresh_token)
