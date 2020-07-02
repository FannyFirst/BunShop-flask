class Buns(object):
    from app.modules.dao.db import buns

    def get(self, _id: int):
        if _id in self.buns:
            return self.buns[_id]
        return None

    def create(self, name: str, num: int, price: int, pic_url: int):
        self.buns[len(self.buns)] = {"name": name, "num": num, "price": price, "pic_url": pic_url}
        return self.buns[len(self.buns) - 1]

    # def update(self, _id: int, num: int):
    #     if self.buns[_id] is not None:
    #         self.buns[_id]["num"] = num
    #         return True
    #     return False

    def list(self):
        return [item for item in self.buns.values()]

    def sub(self, _id: int, num: int):
        if _id in self.buns and self.buns[_id]['num'] >= num:
            self.buns[_id]['num'] -= num
            return True
        return False

    def delete(self, _id):
        if _id in self.buns:
            temp = self.buns[_id]
            del self.buns[_id]
            return temp
        return None
