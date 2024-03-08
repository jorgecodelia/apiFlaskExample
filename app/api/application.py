from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from .router import Router
from .util.config_loader import ConfigLoader
from .util.extensions import api, db

class Application:
    def create_app(app):
        
        environment_configurations = ConfigLoader.load_config()
        app.config.update(environment_configurations)
        
        # Initialize dependencies
        api.init_app(app)
        db.init_app(app)

        # Define routes
        Router.route(app)

        return app