import os

class Config:
  SECRET_KEY = os.environ.get('SECERET_KEY') or 'mysecretkey123'