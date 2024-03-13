import os
from werkzeug.exceptions import NotFound
from .logger_util import LoggerUtil
from ..util.constants import Constants
from ..util.extensions import project_detail

class ASCIIArtPrinter:
    def __init__(self):
        try:
            # Show project details
            LOGGER =  LoggerUtil(project_detail['name'])
            LOGGER.info(f"Version: {project_detail['version']}")
            LOGGER.info(f"{project_detail['description']}")

            #load banner
            file_path = os.environ.get('ASCII_ART_DIR', Constants.ENV_NOT_FOUND.name)
            with open(file_path, 'r') as file:
                ascii_art = file.read()
                print(ascii_art)
        except FileNotFoundError:
            e = NotFound("Banner not found!")
            LOGGER.error(type(e), e.description)