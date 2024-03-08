from enum import Enum

class Constants(Enum):
    # Logger library messages
    INFO_MESSAGE = "Information: {}"
    WARNING_MESSAGE = "Warning: {}"
    ERROR_MESSAGE = "Error: {}"
    CRITICAL_MESSAGE = "Critical: {}"

    ## http error status
    CREATED = "CREATED"
    BAD_REQUEST = "BAD REQUEST"
    SERVICE_ERROR = "INTERNAL SERVER ERROR"
    SUCCESS = "SUCCESS"