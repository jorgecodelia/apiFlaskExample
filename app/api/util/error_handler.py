from werkzeug.exceptions import HTTPException, BadRequest, NotFound, Unauthorized, ServiceUnavailable
from .logger_util import LoggerUtil
from .extensions import api
from ..exception.service_exception import ServiceException

LOGGER =  LoggerUtil('ErrorHandler')

class ErrorHandler:    
    @staticmethod
    def handle_exception(e):
        """
        The function `handle_exception` logs a warning message and raises specific custom exceptions
        based on the HTTP status code of the input exception, or a generic `ServiceException` if the
        status code is not recognized.
        
        :param e: The `handle_exception` method you provided is a way to handle different types of
        exceptions that may occur in your code. The method checks if the exception `e` is an instance of
        `HTTPException` and then handles it based on the status code of the exception
        :return: If the exception `e` is an instance of `HTTPException`, one of the specific exception
        classes like `BadRequest`, `Unauthorized`, `NotFound`, `ServiceException`, or
        `ServiceUnavailable` will be raised based on the status code of the HTTP exception. If the
        status code does not match any of these specific cases, an instance of `HTTPException` will be
        returned.
        """
        LOGGER.warning("Handling Exception...")
        if isinstance(e, HTTPException):
            status_code = e.code
            if status_code == 400:
                api.abort(e.code, str(e))
                raise BadRequest(e)
            if status_code == 401:
                api.abort(e.code, str(e))
                raise Unauthorized(e)
            elif status_code == 404:
                api.abort(e.code, str(e))
                raise NotFound(e)
            elif status_code == 503:
                api.abort(e.code, str(e))
                raise ServiceUnavailable(e)
            else:
                api.abort(e.code, str(e))
                raise ServiceException(e)
        else:
            api.abort(500, str(e))
            raise ServiceException("An unexpected error occurred", e)