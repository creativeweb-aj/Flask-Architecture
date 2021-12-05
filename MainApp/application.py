from MainApp.AppSettings.configuration import HOST, PORT, DEBUG
from MainApp.AppSettings.extension import FlaskApp, db, migrate, ma, restApi


# Flask App initialize with extensions and run
def create_app():
    # Rest api swagger initialize
    restApi.init_app(FlaskApp)

    # Database connection initialize
    db.init_app(FlaskApp)

    # Database migrate initialize
    migrate.init_app(FlaskApp, db)

    # Marshmallow initialize
    ma.init_app(FlaskApp)

    # Return App for run in run.py file
    return FlaskApp


# Run Application
if __name__ == "__main__":
    create_app().run(debug=DEBUG, host=HOST, port=PORT)
