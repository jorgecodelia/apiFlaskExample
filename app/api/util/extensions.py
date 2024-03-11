import os
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

doc_url = os.environ.get('DOC_URL', 'local')
if "html" in doc_url:
    doc_url = doc_url
else:
    doc_url = False

api = Api(
    version="1.0.0", 
    default ='Users',
    default_label='Users CRUD endpoitns',  
    title='Sample Users API', 
    description='A sample user API archetype', 
    doc=doc_url
    )
db = SQLAlchemy()