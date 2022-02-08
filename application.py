from dotenv import load_dotenv
# To load environment variables
load_dotenv()
from flask import Flask
from settings.extension import db, migrate, ma, swagger
from AuthApp.router import AuthApp
from AuthApp import models


# Flask App initialize with extensions and run
def create_app():
    # Flask app initialize
    app = Flask(__name__)
    app.config.from_pyfile('settings/configuration.py')

    # Blueprints
    app.register_blueprint(AuthApp, url_prefix='/auth')

    # Database connection initialize
    db.init_app(app)

    # Marshmallow initialize
    ma.init_app(app)

    # Database migrate initialize
    migrate.init_app(app, db)

    # Swagger initialize
    swagger.init_app(app)

    # Return App for run in run.py file
    return app


# Run Application
if __name__ == "__main__":
    create_app().run(debug=True, host='0.0.0.0', port='5001')


