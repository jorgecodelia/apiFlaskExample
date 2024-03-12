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
        LOGGER.info("Loading environment configurations from: "+env.capitalize())
        if os.path.isfile(yml_file):
            with open(yml_file, 'r') as f:
                return yaml.safe_load(f)
        else:
            LOGGER.error(f"Error: yaml file '{yml_file}' not found.")
            raise FileNotFoundError(f"yaml environment file {yml_file} not found")
        
    @staticmethod
    def load_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            LOGGER.error(f"Error: File '{file_path}' not found.")
            raise FileNotFoundError(f"file {file_path} not found")