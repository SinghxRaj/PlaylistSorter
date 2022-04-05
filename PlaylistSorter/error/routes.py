from flask import Blueprint, render_template

error_blueprint = Blueprint("error", __name__, template_folder="templates")

@error_blueprint.route("/error")
def error_page():
  return render_template("error.html")