from DB import Database


class User():

    def __init__(self):
        self.db = Database()

    def login(self, uid, username):
        response = self.db.find_user({"userid": uid})
        if(response is None):
            self.add_user(uid, username)
        return "OKAY"

    def add_user(self, uid, username):
        self.db.add_user({"userid": uid, "username": username})
        return "OKAY"
