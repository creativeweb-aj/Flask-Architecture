from dotenv import load_dotenv
# To load environment variables
load_dotenv()
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from settings.extension import db, migrate, ma, swagger
from apps.AuthApp.router import AuthApp, models


# Flask App initialize with extensions and run
def create_app():
    # Flask app initialize
    app = Flask(__name__)
    app.config.from_pyfile('settings/configuration.py')

    # Flask Admin
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='Flask Admin Panel', template_mode='bootstrap4')
    admin.add_view(ModelView(models.User, db.session, category='Auth'))
    admin.add_view(ModelView(models.EmailHandler, db.session, category='Auth'))

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


