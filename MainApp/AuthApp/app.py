from flask import Blueprint
from flask_restx import Namespace
from MainApp.AppSettings.extension import FlaskApp, restApi

# Initialize blueprint and register it with flask app
AuthApp = Blueprint('Auth App', __name__)
FlaskApp.register_blueprint(AuthApp)

# Initialize Namespace and add it with rest api
AuthApi = Namespace(
    name='Auth',
    description='Auth App Description',
    path='/auth',
    validate=True
)
restApi.add_namespace(AuthApi)
