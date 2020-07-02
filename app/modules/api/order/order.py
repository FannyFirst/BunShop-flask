from flask_restplus import Namespace, Resource
from flask import request
from app.modules.dao.order.order import Order

from app.extensions.response import *

api = Namespace("Order", "user api", "/order")

DAO = Order()


@api.route("/")
class OrderList(Resource):
    def get(self):
        return response(DAO.list())
        # waitingBuns id


@api.route("/<int:uid>")
class Order(Resource):
    def get(self, uid):
        return response(DAO.get(uid))
