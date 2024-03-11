import logging
import traceback
from .constants import Constants

class LoggerUtil:
    
    def __init__(self, name=__name__):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add formatter to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        self.logger.addHandler(ch)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, exc_class, message):
        self.logger.exception("%s: %s", exc_class.__name__, self.decorate_message(message), exc_info=True)
        traceback.print_exc()

    def decorate_message(self, message):
        current_level = self.get_log_level()
        if current_level == 'DEBUG':
            return Constants.INFO_MESSAGE.value.format(message)
        elif current_level == 'WARNING':
            return Constants.WARNING_MESSAGE.value.format(message)
        elif current_level == 'ERROR':
            return Constants.ERROR_MESSAGE.value.format(message.args[0])
        else:
            return None

    def get_log_level(self):
        return logging.getLevelName(self.logger.level)