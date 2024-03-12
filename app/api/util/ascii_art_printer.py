import os
from .logger_util import LoggerUtil

LOGGER =  LoggerUtil('ASCIIArtPrinter')

class ASCIIArtPrinter:
    def __init__(self):
        try:
            file_path = os.environ.get('ASCII_ART_DIR')
            with open(file_path, 'r') as file:
                ascii_art = file.read()
                print(ascii_art)
        except FileNotFoundError:
            LOGGER.error("Banner not found!")