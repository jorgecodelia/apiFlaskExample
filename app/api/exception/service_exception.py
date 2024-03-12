from werkzeug.exceptions import HTTPException

class ServiceException(Exception):
    def __init__(self, description, payload=None, code=None):
        super().__init__()
        self.messadescriptionge = description
        if not code:
            self.code = 500
        else:
            self.code = code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['description'] = self.description
        return rv