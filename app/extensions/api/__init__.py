from flask_restplus import Api

api = Api(version='1.0', title='TodoMVC API',
          description='A simple TodoMVC API',
          )


def init_app(app):
    api.init_app(app)
