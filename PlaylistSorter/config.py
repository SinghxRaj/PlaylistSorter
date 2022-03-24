import os

class Config:
  """
  A class that provides the configurations for the flask application

  Attributes:
  -----------
  SECRET_KEY : str
    A string that is used to sign session cookies
    which protects against cookies tampering. This value should be
    hidden.
  """
  SECRET_KEY = os.environ.get('SECERET_KEY') or 'mysecretkey123'