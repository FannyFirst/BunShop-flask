# from . import modules, extensions
from flask import Flask
from flask_cors import CORS
from app import extensions, modules


def create_app():
    app = Flask(__name__)

    extensions.init_app(app)

    modules.init_app(app)

    CORS(app, supports_credentials=True)

    return app
