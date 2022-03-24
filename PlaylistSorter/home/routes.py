from flask import render_template, Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
@home_blueprint.route('/home')
def home_page():
  """
  Renders the home page
  """
  return render_template('home.html')
