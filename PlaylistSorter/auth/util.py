import os
from spotipy.oauth2 import SpotifyOAuth
from flask import url_for

def create_spotify_oauth():
  return SpotifyOAuth(
    client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
    client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
    redirect_uri=url_for('auth.callback', _external=True),
    scope='playlist-modify-private playlist-read-private playlist-modify-public user-read-recently-played user-top-read'
  )