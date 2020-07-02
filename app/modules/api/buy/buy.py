from flask_restplus import Namespace, Resource
from flask import request, json
from app.modules.dao.buyingList.buyingList import BuyingList
from app.modules.dao.buns.buns import Buns
from app.modules.dao.user.user import User
from app.modules.dao.order.order import Order
from app.extensions.response import *
import copy, time

api = Namespace("Order", "user api", "/buy")

BuyingListDAO = BuyingList()
BunsDAO = Buns()
UserDAO = User()
OrderDAO = Order()
bunsLock = False


# 事务相关，简易检查
def checkHasEnoughBunsInCart(cart):
    for item in cart:
        bun = BunsDAO.get(item['index'])
        if bun is None or item['num'] > bun['num']:
            return False
    return True


def checkHasNotConfirmOrder(uid):
    tempList = BuyingListDAO.list()
    for item in tempList:
        if 'uid' in tempList[item] and int(tempList[item]['uid']) is uid:
            return item
    return None


@api.route("/")
class Buy(Resource):
    def post(self):
        data = json.loads(request.data)
        uid = data['uid']
        cart = data['cart']
        totalPrice = data['totalPrice']

        if uid is None:
            return response(code=UserResponse.USER_NOT_LOGIN)

        if UserDAO.get(int(uid)) == -1:
            return response(code=UserResponse.USER_NOT_FOUND)

        temp = checkHasNotConfirmOrder(int(uid))
        if temp is not None:
            return response(temp, BuyingResponse.HAS_NOT_CONFIRMED_ORDER)

        if checkHasEnoughBunsInCart(cart):
            waitItem = {'uid': uid, 'buns': [], 'totalPrice': totalPrice, 'start': time.time()}
            for item in cart:
                if BunsDAO.sub(item['index'], item['num']):
                    temp = copy.deepcopy(BunsDAO.get(item['index']))
                    temp['num'] = item['num']
                    waitItem['buns'].append(temp)
                else:
                    return response(code=BunsResponse.BUNS_NOT_ENOUGH)

            return response(BuyingListDAO.put(waitItem))
        else:
            return response(code=BunsResponse.BUNS_NOT_ENOUGH)

    def get(self):
        _id = request.args.get("id")
        temp = BuyingListDAO.get(int(_id))
        if temp is not None:
            if 'ready' in temp and temp['ready']:
                OrderDAO.create(temp['uid'], temp['buns'], temp['totalPrice'], str(int(time.time() - temp['start'])))
                BuyingListDAO.remove(int(_id))
                return response()
            return response(code=BuyingResponse.ORDER_NOT_ALREADY)
        return response(code=BuyingResponse.ORDER_NOT_FOUND)


@api.route("/buying")
class Buying(Resource):
    def get(self):
        return BuyingListDAO.list()

    def post(self):
        _id = request.args.get("id")
        temp = BuyingListDAO.get(int(_id))
        if temp is not None:
            temp['ready'] = True
            return response()
        return response(code=BuyingResponse.ORDER_NOT_FOUND)


@api.route("/buying/<int:uid>")
class BuyingCheck(Resource):
    def get(self, uid):
        temp = checkHasNotConfirmOrder(int(uid))
        if temp is not None:
            return response(temp, BuyingResponse.HAS_NOT_CONFIRMED_ORDER)
        return response()
