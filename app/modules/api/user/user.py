from flask_restplus import Namespace, Resource
from flask import request
from app.modules.dao.user.user import User
from app.extensions.response import *

api = Namespace("User", "user api", "/user")

DAO = User()


@api.route("/")
class UserList(Resource):

    def get(self):
        return response(DAO.list())


# @api.route("/<int:_id>")
# class User(Resource):
#
#     def get(self, _id):
#         return response(DAO.get(_id))
#
#     # @api.param("name", "user name")
#     # def put(self, _id):
#     #     name = request.args.get("name")
#     #     if name is None:
#     #         return response(code=BaseResponse.PARAM_NOT_ALLOW)
#     #     return response(DAO.update(_id, name))
#
#     def delete(self, _id):
#         return response(DAO.status(_id))


@api.route("/login")
class UserAuth(Resource):
    def post(self):
        _id = request.args.get("id")
        if _id is not None:
            try:
                _id = int(_id)
            except ValueError:
                return response(BaseResponse.PARAM_TYPE_NOT_ALLOW)

            user = DAO.get(_id)
            if user != -1:
                return response(_id)

        return response(DAO.create())
