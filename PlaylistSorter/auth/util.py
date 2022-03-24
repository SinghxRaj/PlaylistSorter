import os
from spotipy.oauth2 import SpotifyOAuth
from flask import url_for, session

def create_spotify_oauth() -> SpotifyOAuth:
  """
  Returns an instance of the SpotifyOAuth that is configured for
  the application
  """
  return SpotifyOAuth(
    client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
    client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
    redirect_uri=url_for('auth.callback', _external=True),
    scope='playlist-modify-private playlist-read-private playlist-modify-public user-read-recently-played user-top-read'
  )

def get_token() -> dict:
  """
  Returns the access token

  If the current access token is expired a new one will be created
  and returned

  Raises
  -----------
  Exception
  If there doesn't exist an access token in the current session
  """
  token_info = session.get("token_info", None)
  if not token_info:
    raise "exception"
  spotify_oauth = create_spotify_oauth()
  token_info = session['token_info']
  if(spotify_oauth.is_token_expired(token_info)):
    token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
    session['token_info'] = token_info
  return token_info
