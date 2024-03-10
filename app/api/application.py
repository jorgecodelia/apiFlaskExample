from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from .router import Router
from .util.config_loader import ConfigLoader
from .util.extensions import api, db
from .util.error_handler import ErrorHandler

class Application:
    def create_app(app):
        
        environment_configurations = ConfigLoader.load_config()
        app.config.update(environment_configurations)
        
        # Initialize dependencies
        api.init_app(app)
        db.init_app(app)

        #Error handler
        ErrorHandler()

        # Define routes
        Router.route()

        return app