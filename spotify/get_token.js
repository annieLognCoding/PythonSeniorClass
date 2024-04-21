const express = require('express');
const querystring = require('querystring');
const axios = require('axios'); // Make sure to install axios

var client_id = 'f491e5a3cf11442e9eeed75b7d8f18bd'; // Your Spotify Client ID
var client_secret = '9cf6d661f60b411293dce3581b2c78dd'; // Your Spotify Client Secret
var redirect_uri = 'http://localhost:8888/callback';

var app = express();

function generateRandomString(length) {
  let text = '';
  const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  for (let i = 0; i < length; i++) {
    text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return text;
}

app.get('/login', function(req, res) {
  var state = generateRandomString(16);
  var scope = 'user-read-private user-read-email playlist-modify-public';
  res.redirect('https://accounts.spotify.com/authorize?' +
    querystring.stringify({
      response_type: 'code',
      client_id: client_id,
      scope: scope,
      redirect_uri: redirect_uri,
      state: state
    }));
});

app.get('/callback', function(req, res) {
  var code = req.query.code || null;
  var state = req.query.state || null;

  if (state === null) {
    res.redirect('/#' +
      querystring.stringify({
        error: 'state_mismatch'
      }));
  } else {
    // Use Axios to make a POST request to Spotify to exchange the code for an access token
    axios({
      method: 'post',
      url: 'https://accounts.spotify.com/api/token',
      data: querystring.stringify({
        code: code,
        redirect_uri: redirect_uri,
        grant_type: 'authorization_code'
      }),
      headers: {
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + (new Buffer.from(client_id + ':' + client_secret).toString('base64'))
      }
    }).then(response => {
      // Handle success
      const access_token = response.data.access_token;
      const refresh_token = response.data.refresh_token;
      // Here you might redirect or send tokens to the client, for example:
      res.send({ access_token: access_token, refresh_token: refresh_token });
    }).catch(error => {
      // Handle error, such as by sending error details
      res.status(500).send('Authentication failed');
    });
  }
});

// Listen on a specific port
app.listen(8888, function() {
  console.log('Your app is listening on port 8888');
});
