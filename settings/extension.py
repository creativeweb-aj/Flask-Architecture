from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flasgger import Swagger
import datetime
import os

# Date time object
timestamp = str(datetime.datetime.timestamp(datetime.datetime.now()))

# DB initialize
# db variable use for create models from here
db = SQLAlchemy()

# Migrate initialize
# Migrate database config
migrate = Migrate()

# Marshmallow for database model schema
ma = Marshmallow()

# Swagger initialize document
swagger_config = {
    "title": "App API",
    "uiversion": 3,
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/api/doc"
}
SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "App Api",
        "description": "Api for all service",
        "contact": {
            "responsibleOrganization": "Creative Web",
            "responsibleDeveloper": "Ajay Kumar Sharma",
            "email": "webcreations100@gmail.com",
            "url": "https://learnpyjs.blogspot.com",
        },
        "version": "1.0.0"
    },
    "host": os.environ.get('BASE_URL'),  # overrides localhost:500
    "basePath": "",  # base bash for blueprint registration
    "schemes": ["http", "https"],
    "operationId": "data",
    "securityDefinitions": {"APIKeyHeader": {"type": "apiKey", "name": "Authorization", "in": "header"}}
}
swagger = Swagger(config=swagger_config, template=SWAGGER_TEMPLATE)
