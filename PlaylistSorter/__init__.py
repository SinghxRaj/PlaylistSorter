from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = '5b40cce1306229212c00b3c7eee4f2c68189d8f5f8116bea'
  # Config the blue prints for the app or import the modules
  return app