from flask import render_template, Blueprint

sort_blueprint = Blueprint()

@sort_blueprint.route('/sort')
def sort():
  return render_template('sort.html')