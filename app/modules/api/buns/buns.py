from flask_restplus import Namespace, Resource
from flask import request
from app.modules.dao.buns.buns import Buns
from app.extensions.response import *

api = Namespace("Buns", "user api", "/buns")

pic_url = ["https://bkimg.cdn.bcebos.com/pic/7c1ed21b0ef41bd546b0012d5fda81cb38db3d0c?x-bce"
           "-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UxMTY=,xp_5,yp_5",
           "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1593418888543&di"
           "=f7e165230b17f04a0d6104b969476d34&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com"
           "%2Fimages%2F20181125%2F9ab317947ef44a9d8da5f60dd9d7226e.jpeg"]

DAO = Buns()


@api.route("/")
class BunsList(Resource):
    def get(self):
        return response(DAO.list())

    def post(self):
        name = request.args.get("name")
        price = request.args.get("price")
        _type = request.args.get("type")
        num = request.args.get("num")

        if name is None or num is None or price is None:
            return response(code=BaseResponse.PARAM_NOT_ALLOW)

        try:
            num = int(num)
        except ValueError:
            return response(code=BaseResponse.PARAM_TYPE_NOT_ALLOW)

        if num <= 0 or not isinstance(num, int):
            return response(code=BaseResponse.PARAM_TYPE_NOT_ALLOW)

        res = DAO.create(name, num, price, 1 if (_type is not None) else 0)
        return response(res)


@api.route("/<int:_id>")
class Buns(Resource):
    def get(self, _id):
        return response(DAO.get(_id))

    def put(self, _id):

        try:
            num = int(request.args.get("num"))
        except ValueError:
            return response(code=BaseResponse.PARAM_TYPE_NOT_ALLOW)

        if not isinstance(num, int):
            return response(code=BaseResponse.PARAM_NOT_ALLOW)

        if num < 0:
            return response(code=BaseResponse.PARAM_TYPE_NOT_ALLOW)

        res = DAO.update(_id, num)
        return response(res)

    def delete(self, _id):
        return response(DAO.delete(_id))
