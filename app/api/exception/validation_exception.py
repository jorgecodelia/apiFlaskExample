from werkzeug.exceptions import HTTPException
from ..util.logger_util import LoggerUtil

LOGGER =  LoggerUtil('ValidationException')

class ValidationException(HTTPException):
    def __init__(self, description, payload=None):
        super().__init__()
        self.description = description
        self.code = 400
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['description'] = self.description
        return rv