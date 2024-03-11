from enum import Enum

class Constants(Enum):
    # Logger library messages
    INFO_MESSAGE = "Information: {}"
    WARNING_MESSAGE = "Warning: {}"
    ERROR_MESSAGE = "Critical: {}"

    ## http common error status
    CREATED = "CREATED"
    BAD_REQUEST = "BAD REQUEST"
    SERVICE_ERROR = "INTERNAL SERVER ERROR"
    FORBIDDEN = "FORBIDDEN"
    UNAUTHORIZED = "UNAUTHORIZED"
    SUCCESS = "SUCCESS"