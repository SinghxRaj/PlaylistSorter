from flask import Flask
from PlaylistSorter.config import Config

def create_app() -> Flask:
  """
  Creates and returns an instance of the Flask Application

  This can be used for creating different instance of the application,
  each with different configurations which can be useful when testing.
  """
  app = Flask(__name__)
  app.config.from_object(Config)
  from PlaylistSorter.home.routes import home_blueprint
  from PlaylistSorter.auth.routes import auth_blueprint
  from PlaylistSorter.selection.routes import selection_blueprint
  from PlaylistSorter.sort.routes import sort_blueprint
  # from PlaylistSorter.result.routes import result_blueprint

  app.register_blueprint(home_blueprint)
  app.register_blueprint(auth_blueprint)
  app.register_blueprint(selection_blueprint)
  app.register_blueprint(sort_blueprint)
  return app