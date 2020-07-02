from . import buns
from app.extensions.api import api


def init_app(app):
    api.add_namespace(buns.api)
