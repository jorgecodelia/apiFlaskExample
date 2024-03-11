from flask import json
from werkzeug.exceptions import HTTPException
from .logger_util import LoggerUtil
from .extensions import api

LOGGER =  LoggerUtil('ErrorHandler')

class ErrorHandler:

    def handle_exception_not_found(self, e):
        api.abort(e.code, str(e))
        raise e

    def handle_exception_service(self, e):
        api.abort(e.code, str(e))
        raise e

    def handle_exception_service_unavailable(self, e):
        api.abort(e.code, str(e))
        raise e

    def handle_exception_validation(self, e):
        api.abort(e.code, str(e))
        raise e
    
    def handle_default_exception(self, e):
        raise Exception(e)

    def handle_http_error(self, e):
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        if e.code is not None:
            api.abort(e.code, e.description)
        else:
            api.abort(500, "An unexpected error occurred")
        return response
    
    def handle_exception(self, e):
        LOGGER.warning("Handling Exception...")
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
