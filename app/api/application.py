from flask_sqlalchemy import SQLAlchemy
from .router import Router
from .util.config_loader import ConfigLoader
from .util.extensions import api, db
from .util.error_handler import ErrorHandler

class Application:
    def create_app(app):
        app.config.update(ConfigLoader.load_config())
        
        # Initialize dependencies
        api.init_app(app)
        db.init_app(app)

        # Define routes
        Router.route()

        return app