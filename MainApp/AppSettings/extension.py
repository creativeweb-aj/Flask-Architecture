from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restx import Api

# Flask app initialize
FlaskApp = Flask(__name__)
FlaskApp.config.from_pyfile('configuration.py')

# DB initialize
# db variable use for create models from here
db = SQLAlchemy()

# Migrate initialize
# Migrate database config
migrate = Migrate()

# Marshmallow for database model schema
ma = Marshmallow()

# Rest Api initialize
# Token security for api's
authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'authorizations'
    }
}
# Create rest api object
restApi = Api(
    version="1.0",
    title="Flask Rest Api",
    description="This is flask rest api documentation for all apps.",
    doc='/api/doc/',
    authorizations=authorizations
)
