# app/__init__.py

from flask import Flask
from .api.application import Application

app = Flask(__name__)

#the real app
Application.create_app(app)

