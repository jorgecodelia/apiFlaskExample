import os
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

doc_url = os.environ.get('DOC_URL', 'local')
if "html" in doc_url:
    doc_url = doc_url
else:
    doc_url = False

api = Api(default ='Users', default_label='Users CRUD endpoitns', doc=doc_url)
db = SQLAlchemy()