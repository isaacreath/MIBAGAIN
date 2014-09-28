from DB import Database


class Friend():

    def __init__(self):
        self.db = Database()

    def add_friend(self, uid, friend):
        self.db.add_friend(uid, friend)
        return "success"

    def list_friends(self, uid):
        return self.db.list_friends(uid)