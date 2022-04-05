from flask import render_template, session, redirect, request, url_for, Blueprint
from PlaylistSorter.auth.util import get_token
from PlaylistSorter.spotify_api.util import all_playlists, isOwner

selection_blueprint = Blueprint('selection', __name__, template_folder='templates')

@selection_blueprint.route('/selection', methods=["GET", "POST"])
def selection_page():
  """
  Retrieves of the user's playlists and renders them
  on the selection page
  """
  try:
    token_info = get_token()
  except Exception:
    return redirect(url_for('error.error_page'))
  if request.method == "POST":
    session['selected_playlist_id'] = request.form.get('selected_playlist', None)
    if(isOwner(token_info, session.get('selected_playlist_id', None))):
      return redirect(url_for("sort.owner_sort_page"))
    else:
      return redirect(url_for("sort.not_owner_sort_page"))
  else:
    playlists_info = all_playlists(token_info)
    return render_template('selection.html', playlists_info=playlists_info)
