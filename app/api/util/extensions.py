import os
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from .config_loader import ConfigLoader

doc_url = os.environ.get('DOC_URL', 'local')
if "html" in doc_url:
    doc_url = doc_url
else:
    doc_url = False

project_detail = ConfigLoader.load_project_version()
api = Api(
    version= project_detail['version'], 
    default ='Users',
    default_label='Users CRUD endpoitns',  
    title=project_detail['name'], 
    description=project_detail['description'], 
    doc=doc_url
    )
db = SQLAlchemy()