from . import user, buns, order, buy


def init_app(app):
    user.init_app(app)
    buns.init_app(app)
    order.init_app(app)
    buy.init_app(app)
