# app/app.py

import os
from flask import Flask, Blueprint
from flask_restx import Api
from werkzeug.exceptions import HTTPException
from app.api.common.util.error_handler import ErrorHandler
from app.api.common.exception.service_exception import ServiceException

# Import controllers
from app.api.controller.user_controller import UserController

def create_app(env=None):
    app = Flask(__name__)
    api = Api(app)
    error_handler = ErrorHandler(api)

    # Load configuration
    if env:
        env = os.environ.get('FLASK_ENV', 'local')

    config_file = f'./resources/{env}.yml'

    # Register blueprints
    user_bp = Blueprint('user', __name__, url_prefix='/users')
    app.register_blueprint(user_bp)

    # Initialize Flask-Restx API
    api.init_app(app)

    # Check if the config file exists, if not, use the local config
    if os.path.isfile(config_file):
        app.config.from_pyfile(config_file)
    else:
        app.config.from_pyfile('./resources/local.yml')

    # Define error handler for ServiceException
    @api.errorhandler(ServiceException)
    def handle_custom_exception(error):
        return error_handler.handle_custom_exception(error)

    # Define error handler for HTTPException
    @api.errorhandler(HTTPException)
    def handle_http_exception(error):
        return error_handler.handle_http_exception(error)

    # Define routes
    api.add_resource(UserController, '/v1/users')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)