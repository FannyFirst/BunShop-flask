
class BuyingList:
    from app.modules.dao.db import buyingList

    def put(self, data: dict):
        _id = len(self.buyingList)
        self.buyingList[_id] = data
        return _id

    def get(self, index: int):
        if index in self.buyingList:
            return self.buyingList[index]
        return None

    def remove(self, index: int):
        if index in self.buyingList:
            del self.buyingList[index]
            return True
        return False

    def list(self):
        return self.buyingList
