# app/__init__.py

from flask import Flask
from .api.application import Application
from .api.util.ascii_art_printer import ASCIIArtPrinter

app = Flask(__name__)

#bonus starting banner
ASCIIArtPrinter()

#the real app
Application.create_app(app)

