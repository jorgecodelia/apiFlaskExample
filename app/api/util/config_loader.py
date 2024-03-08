import os
import yaml
from .logger_util import LoggerUtil

LOGGER =  LoggerUtil('ConfigLoader')

class ConfigLoader:
    @staticmethod
    def load_config():
        # Load configuration
        env = os.environ.get('FLASK_ENV', 'local')
        # Load configuration from YAML file
        yml_file = f'./app/resources/{env}.yaml'
        LOGGER.info("Loading environment configurations from : "+yml_file)
        if os.path.isfile(yml_file):
            with open(yml_file, 'r') as f:
                return yaml.safe_load(f)
        else:
            raise FileNotFoundError(f"yaml environment file {yml_file} not found")