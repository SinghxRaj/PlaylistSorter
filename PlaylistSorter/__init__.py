from flask import Flask
from PlaylistSorter.config import Config

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)
  from PlaylistSorter.home.routes import home_blueprint
  # from PlaylistSorter.auth.routes import auth_blueprint
  # from PlaylistSorter.selection.routes import selection_blueprint
  # from PlaylistSorter.sort.routes import sort_blueprint
  # from PlaylistSorter.result.routes import result_blueprint

  app.register_blueprint(home_blueprint)
  return app