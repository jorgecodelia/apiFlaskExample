import re
from werkzeug.exceptions import BadRequest
from .logger_util import LoggerUtil
from .error_handler import ErrorHandler

LOGGER =  LoggerUtil('ValidatorUtil')
HANDLER = ErrorHandler()

class ValidatorUtil:
    @staticmethod
    def is_valid_email(email):
        # Regular expression pattern for validating email addresses
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
        # Use the search function to check if the email matches the pattern
        if re.search(pattern, email):
            return True
        else:
            e = BadRequest("Invalid email!")
            LOGGER.error(type(e), e.description)
            HANDLER.handle_exception(e)

    def check_user_id(user_id):
        if not user_id:
            e = BadRequest("User ID is required!")
            LOGGER.error(type(e), e.description)
            HANDLER.handle_exception(e)