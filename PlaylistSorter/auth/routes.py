from flask import redirect, request, session, url_for, Blueprint
from PlaylistSorter.auth.util import create_spotify_oauth

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login')
def login():
  """
  Redirects the user to the Spotify login page to authorize
  permissions
  """
  spotify_oauth = create_spotify_oauth()
  auth_url = spotify_oauth.get_authorize_url()
  return redirect(auth_url)

@auth_blueprint.route('/callback')
def callback():
  """
  The user to redirected to this route after they finish logging
  in
  """
  spotify_oauth = create_spotify_oauth()
  session.clear()
  code = request.args.get('code')
  session['token_info'] = spotify_oauth.get_access_token(code)
  return redirect(url_for('selection.selection_page'))