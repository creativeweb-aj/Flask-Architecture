import os
from dotenv import load_dotenv
# To load environment variables
load_dotenv()

# Configuration keys and server host & port
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = os.environ.get('PORT', '5001')
DEBUG = os.environ.get('DEBUG', True)
# Secret Key
SECRET_KEY = os.environ.get('SECRET_KEY')
# Database configurations
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
