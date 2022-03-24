from flask import Blueprint

selection_blueprint = Blueprint('selection', __name__, template_folder='template')

@selection_blueprint.route('/selection')
def selection_page():
  return 'success'