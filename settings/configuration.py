import os

# Secret Key
SECRET_KEY = os.environ.get('SECRET_KEY', '2b9a7143128cf34a43a82ffe5d3f6db5a0e3b06b4c126455')
# Database configurations
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', '')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', True)
