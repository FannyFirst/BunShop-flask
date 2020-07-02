import time


class Order(object):
    from app.modules.dao.db import orders

    def get(self, _id: int):
        userOrderList = list(filter(lambda v: 'uid' in v and int(v['uid']) == int(_id), self.orders))
        return userOrderList

    def create(self, uid: int, buns: list, money: int, waiting_time: str):
        self.orders.append(
            {"uid": uid, "buns": buns, "money": money, "created_at": time.time(), "waiting_time": waiting_time})

    def list(self):
        return self.orders
