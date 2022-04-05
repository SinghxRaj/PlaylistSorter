from flask import Blueprint, render_template

result_blueprint = Blueprint("result", __name__, template_folder="templates")

@result_blueprint.route("/result")
def result_page():
  return render_template("result.html")