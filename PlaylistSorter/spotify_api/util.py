import spotipy

# TODO: If certain session data can't be found either
# the user should be sent to a 404 page or back to the home page

def get_playlist_display_data(token_info, playlist_id) -> dict:
  """
  Retrieves information about a playlist. This information includes
  the display name of the playlist, the url for the cover image,
  and information about each track in the playlist. The information
  retrieved for each track includes the name, the url for the cover
  image, and the artists on the track.

  Args
  ----------
  token_info (dict): Information about the Spotify token which is need
                    to communicate with the Spotify API
  playlist_id (str): The id of the Spotify playlist

  Returns
  ----------
  (dict of str and list): Information about playlist
  """
  sp = spotipy.Spotify(auth=token_info['access_token'])
  selected_playlist = sp.playlist(playlist_id)
  playlist = {}
  playlist["display_name"] = selected_playlist["name"]
  playlist["cover_image_url"] = selected_playlist["images"][0]["url"]
  playlist["tracks"] = []
  hasTracks = True
  iter = 0
  while hasTracks:
    tracks = sp.playlist_tracks(playlist_id, offset=iter * 100)
    iter += 1
    for track_item in tracks["items"]:
      track = {}
      track["name"] = track_item["track"]["name"]
      track["cover_image_url"] = track_item["track"]["album"]["images"][0]["url"]
      track["artists"] = ", ".join(artist["name"] for artist in track_item["track"]["artists"])
      playlist["tracks"].append(track)
    if tracks["next"] is None:
      hasTracks = False
  return playlist


def all_playlists(token_info) -> dict:
  """
  Retrieves all of a user's playlists. The information retrieved includes
  the id, the name, and the url for the cover image.

  Args
  ----------
  token_info (dict): Information about the Spotify token which is need
                    to communicate with the Spotify API

  Returns
  -----------
  (dict of str, list): Information about all of the user's playlists
  """
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
    if curr_playlists_chunk['next'] is None:
      has_playlists = False
  return playlists_info


def get_track_items_data(token_info, playlist_id) -> list:
  """
  Retrieves all information about each track in a playlist

  Args
  ----------
  token_info (dict): Information about the Spotify token which is need
                    to communicate with the Spotify API
  playlist_id (str): The id of the Spotify playlist

  Returns
  ----------
  list: Information about each track in the playlist
  """
  sp = spotipy.Spotify(auth=token_info['access_token'])
  tracks = []
  hasTracks = True
  iter = 0
  while hasTracks:
    temp_tracks = sp.playlist_tracks(playlist_id, offset=iter * 100)
    iter += 1
    for track_item in temp_tracks["items"]:
      tracks.append(track_item)
    if temp_tracks["next"] is None:
      hasTracks = False
  return tracks


def isOwner(token_info, playlist_id):
  """
  Determines whether the current user is the owner of
  the playlist

  Args
  --------------
  token_info (dict): Information about the Spotify token which is need
                    to communicate with the Spotify API
  playlist_id (str): The id of the Spotify playlist

  Returns
  --------------
  bool: Whether the current user is the owner of the playlist
  """
  sp = spotipy.Spotify(auth=token_info['access_token'])
  user_display_name = sp.me()['display_name']
  owner_display_name = sp.playlist(playlist_id)['owner']['display_name']
  return user_display_name == owner_display_name


def create_new_playlist(token_info, playlist_name, track_ids) -> str:
  """
  Creates a new playlist for the user which consists of the given tracks.

  Args
  ------------
  token_info (dict): Information about the Spotify token which is need
                    to communicate with the Spotify API.
  playlist_name (str): The name of the new playlist
  track_ids (list): The ids of tracks in the playlist

  Returns
  ----------
  playlist_id (str): The id of the newly created playlist
  """
  sp = spotipy.Spotify(auth=token_info['access_token'])
  user_id = sp.me()["id"]
  playlist_id = sp.user_playlist_create(user_id, playlist_name, public=False)["id"]
  limit = 100
  playlist_id_chunks = [track_ids[i:i + limit] for i in range(0, len(track_ids), limit)]
  for i in range(len(playlist_id_chunks)):
    sp.playlist_add_items(playlist_id, playlist_id_chunks[i], i * limit)
  return playlist_id


def replace_playlist(token_info, playlist_id, track_ids):
  """
  Replaces the tracks of a playlist with the given tracks.

  Args
  ----------
  token_info (dict): Information about the Spotify token which is need
                    to communicate with the Spotify API.
  playlist_id (str): The id of the playlist that is being modified
  track_ids (list): The id of the tracks that will replace the old tracks
  """
  sp = spotipy.Spotify(auth=token_info['access_token'])
  limit = 100
  playlist_id_chunks = [track_ids[i:i + limit] for i in range(0, len(track_ids), limit)]
  sp.playlist_replace_items(playlist_id, playlist_id_chunks[0])
  itr = 1
  while itr < len(playlist_id_chunks):
    sp.playlist_add_items(playlist_id, playlist_id_chunks[itr], itr * limit)
    itr += 1
