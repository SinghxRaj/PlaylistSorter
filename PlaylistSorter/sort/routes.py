from flask import session, request, redirect, url_for, render_template, Blueprint
from PlaylistSorter.auth.util import get_token
from PlaylistSorter.spotify_api.util import get_playlist_display_data, get_track_items_data, create_new_playlist, replace_playlist
from PlaylistSorter.sort.util import sort_on_key

sort_blueprint = Blueprint("sort", __name__, template_folder="templates")

@sort_blueprint.route('/owner-sort', methods=["GET", "POST"])
def owner_sort_page():
  """
  If the request is a GET method, it will render `owner_sort.html`.
  If the request is a POST method, it will create a new playlist sorted
  on the attribute the user gave on the selected playlist if the user chose
  to create a new playlist. Otherwise, it will replace the currently selected
  playlist with the tracks in sorted order.
  """
  try:
    token_info = get_token()
  except:
    return redirect(url_for('home.home_page'))
  playlist_id = session.get("selected_playlist_id", None)
  if playlist_id is None:
    return redirect(url_for("home.home_page"))
  if request.method == "GET":
    playlist = get_playlist_display_data(token_info, playlist_id)
    return render_template("owner_sort.html", playlist=playlist)
  if request.method == "POST":
    items = get_track_items_data(token_info, playlist_id)
    sorted_items = sort_on_key(request.form["sort"], items)
    sorted_tracks_id = [item["track"]["id"] for item in sorted_items]
    if request.form.get("playlist", False) == "Create New Playlist":
      playlist_name = request.form.get("playlist-name", None)
      new_playlist_id = create_new_playlist(token_info, playlist_name, sorted_tracks_id)
      session["new_playlist_id"] = new_playlist_id
    else:
      replace_playlist(token_info, playlist_id, sorted_tracks_id)
      session["new_playlist_id"] = playlist_id
    return redirect(url_for("home.home_page"))
    # return redirect(url_for("result.result_page"))

@sort_blueprint.route('/not-owner-sort', methods=["GET", "POST"])
def not_owner_sort_page():
  """
  If the request is a GET method, it will render `not_owner_sort.html`.
  If the request is a POST method, it will create a new playlist sorted
  on the attribute the user gave on the selected playlist if the user chose
  to create a new playlist.
  """
  try:
    token_info = get_token()
  except:
    return redirect(url_for('home.home_page'))
  playlist_id = session.get("selected_playlist_id", None)
  if playlist_id is None:
    return redirect(url_for("home.home_page"))
  if request.method == "GET":
    playlist = get_playlist_display_data(token_info, playlist_id)
    return render_template("not_owner_sort.html", playlist=playlist)
  if request.method == "POST":
    items = get_track_items_data(token_info, playlist_id)
    sorted_items = sort_on_key(request.form["sort"], items)
    sorted_tracks_id = [item["track"]["id"] for item in sorted_items]
    playlist_name = request.form.get("playlist-name", None)
    new_playlist_id = create_new_playlist(token_info, playlist_name, sorted_tracks_id)
    session["new_playlist_id"] = new_playlist_id
    return redirect(url_for("home.home_page"))
    # return redirect(url_for("result.result_page"))
