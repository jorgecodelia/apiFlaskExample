from flask_restx import Api
from werkzeug.exceptions import HTTPException

class ErrorHandler:
    def __init__(self, api: Api):
        self.api = api

    def handle_error(self, error):
        code = getattr(error, 'code', 500)
        message = getattr(error, 'description', 'Internal Server Error')
        return {'message': message}, code
    
    def register_error_handler(self):
        self.api.errorhandler(HTTPException)(self.handle_error)
