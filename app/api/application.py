#from flask_sqlalchemy import SQLAlchemy
from .router import Router
from .util.config_loader import ConfigLoader
from .util.extensions import api, db
from .util.ascii_art_printer import ASCIIArtPrinter

class Application:
    def create_app(app):
        app.config.update(ConfigLoader.load_environment_configuration())
        
        #bonus starting banner
        ASCIIArtPrinter()

        # Initialize dependencies
        api.init_app(app)
        #db.init_app(app)

        # Define routes
        Router.route()

        return app