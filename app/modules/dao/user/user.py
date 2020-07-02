class User:
    from app.modules.dao.db import users

    def get(self, _id: int):
        if 0 <= _id < len(self.users):
            return self.users[_id]
        return -1

    def list(self):
        return self.users

    def create(self):
        self.users.append(len(self.users))
        return len(self.users) - 1

    # def update(self, _id: int, name: str):
    #     if self.users[_id] is not None:
    #         self.users[_id]["name"] = name
    #     else:
    #         self.create(name)
    #     return self.users[_id]

    # def status(self, _id: int):
    #     if self.users[_id] is not None:
    #         self.users[_id]["status"] = not self.users[_id]["status"]
    #         return True
    #     return False
