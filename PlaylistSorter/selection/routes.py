from flask import render_template, session, redirect, request, url_for, Blueprint
import spotipy
from PlaylistSorter.auth.util import get_token

selection_blueprint = Blueprint('selection', __name__, template_folder='templates')

@selection_blueprint.route('/selection', methods=["GET", "POST"])
def selection_page():
  """
  Retrieves of the user's playlists and renders them
  on the selection page
  """
  if request.method =="POST":
    session['selected_playlist_id'] = request.form['selected_playlist']
    return redirect(url_for("sort.sort_page"))
  try:
    token_info = get_token()
  except Exception:
    return redirect(url_for('home.home_page'))
  sp = spotipy.Spotify(auth=token_info['access_token'])
  display_name = sp.me()['display_name']
  playlists_info = {}
  playlists_info['display_name'] = display_name
  playlists_info['all_playlists'] = []
  iter = 0
  has_playlists = True
  while has_playlists:
    curr_playlists_chunk = sp.current_user_playlists(limit=50, offset=iter*50)
    curr_playlists_chunk_items = curr_playlists_chunk['items']
    for curr_playlist in curr_playlists_chunk_items:
      curr = {}
      curr['id'] = curr_playlist['id']
      curr['name'] = curr_playlist['name']
      curr['image'] = curr_playlist['images'][0]
      playlists_info['all_playlists'].append(curr)
    iter += 1
    if not curr_playlists_chunk['next']:
      has_playlists = False
  return render_template('selection.html', playlists_info=playlists_info)
