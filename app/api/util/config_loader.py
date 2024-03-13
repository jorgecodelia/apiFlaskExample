import os
import yaml
from .logger_util import LoggerUtil

LOGGER =  LoggerUtil('ConfigLoader')

class ConfigLoader:
    
    @staticmethod
    def load_yaml_file(file_path):
        try:
            with open(file_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError as e:
            e = FileNotFoundError(f"yaml environment file {file_path} not found")
            LOGGER.error(type(e),f"Error: yaml file '{file_path}' not found.")
            raise e
        
    @staticmethod
    def load_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            e = FileNotFoundError(f"file {file_path} not found")
            LOGGER.error(f"Error: File '{file_path}' not found.")
            raise e

    @staticmethod
    def load_environment_configuration():
        env = os.environ.get('FLASK_ENV', 'local')
        yml_file = f'./app/resources/{env}.yaml'
        LOGGER.info("Loading environment configurations from: "+env.capitalize())
        return ConfigLoader.load_yaml_file(yml_file)
    
    @staticmethod
    def load_project_version():
        env = os.environ.get('PROJECT_VERSION', './ci/version.yaml')
        yml_file = f'./ci/version.yaml'
        version_data = ConfigLoader.load_yaml_file(yml_file)
        return version_data['project']