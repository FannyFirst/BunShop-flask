import enum
from enum import Enum

from flask import jsonify, make_response


class BaseResponse(Enum):
    SUCCESS = {"code": 10000, "msg": "SUCCESS"}

    PARAM_NOT_ALLOW = {"code": 10001, "msg": "PARAM_NOT_ALLOW"}

    PARAM_TYPE_NOT_ALLOW = {"code": 10002, "msg": "PARAM_TYPE_NOT_ALLOW"}


def response(data=None, code: enum = BaseResponse.SUCCESS):
    code.value["data"] = data
    res = make_response(code.value)
    # res.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    # res.headers["Content-Type"] = "application/json; charset=utf-8"
    # print(res.headers)
    return res


class UserResponse(Enum):
    USER_NOT_FOUND = {"code": 20001, "msg": "USER_NOT_FOUND"}
    USER_NOT_LOGIN = {"code": 20002, "msg": "USER_NOT_LOGIN"}


class BunsResponse(Enum):
    BUNS_NOT_ENOUGH = {"code": 30000, "msg": "BUNS_NOT_ENOUGH"}


class BuyingResponse(Enum):
    ORDER_NOT_FOUND = {"code": 40000, "msg": "ORDER_NOT_FOUND"}
    ORDER_NOT_ALREADY = {"code": 40001, "msg": "ORDER_NOT_ALREADY"}
    HAS_NOT_CONFIRMED_ORDER = {"code": 40002, "msg": "HAS_NOT_CONFIRMED_ORDER"}
