from flask import session, render_template, Blueprint

sort_blueprint = Blueprint("sort", __name__, template_folder="templates")

@sort_blueprint.route('/sort', methods=["GET", "POST"])
def sort_page():
  return session["selected_playlist_id"]