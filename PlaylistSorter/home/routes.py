from flask import render_template, Blueprint

#Configure the blueprint correctly
home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/')
def home():
  return render_template('home.html')
