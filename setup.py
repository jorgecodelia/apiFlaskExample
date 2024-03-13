from setuptools import setup, find_packages
from app.api.util.config_loader import ConfigLoader


project_detail = ConfigLoader.load_project_version()


setup(
    name=project_detail['name'],
    version=project_detail['version'],
    packages=find_packages()
)
