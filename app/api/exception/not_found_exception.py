from werkzeug.exceptions import HTTPException

class NotFoundException(HTTPException):
    def __init__(self, description, payload=None):
        super().__init__()
        self.description = description
        self.code = 404
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['description'] = self.description
        return rv