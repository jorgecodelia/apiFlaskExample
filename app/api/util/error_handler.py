from flask import json, jsonify, abort
from flask_restx import Api
from werkzeug.exceptions import HTTPException
from ..exception.not_found_exception import NotFoundException
from ..exception.service_exception import ServiceException
from ..exception.service_unavailable import ServiceUnavailable
from ..exception.validation_exception import ValidationException

# Remove the import of `app`

class ErrorHandler:

    def handle_exception_not_found(self, e):
        abort(e.code, str(e))

    def handle_exception_service(self, e):
        abort(e.code, str(e))

    def handle_exception_service_unavailable(self, e):
        abort(e.code, str(e))

    def handle_exception_validation(self, e):
        abort(e.code, str(e))
    
    def handle_default_exception(self, e):
        return (jsonify(e.to_dict()), 500)

    def handle_http_error(self, e):
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response
    
    def handle_exception(self, e):
        if isinstance(e, HTTPException):
            status_code = e.code
            if status_code == 400:
                return self.handle_exception_validation(e)
            elif status_code == 404:
                return self.handle_exception_not_found(e)
            elif status_code == 500:
                return self.handle_exception_service(e)
            elif status_code == 503:
                return self.handle_exception_service_unavailable(e)
            else:
                return self.handle_http_error(e)
        else:
            return self.handle_default_exception(e)
