from pymongo import MongoClient
from urlparse import urlparse
import os


class Database():

    def _init__(self):
        self.MONGO_URL = os.environ.get('MONGOHQ_URL')
        self.client = MongoClient(self.MONGO_URL)
        self.db = self.client[urlparse(self.MONGO_URL).path[1:]]
        self.collection = self.db['collection']
        self.friend_collection = self.db['friend_collection']
        self.user_collection = self.db['user_collection']
        self.posts = self.db.posts

    def insert(self, entry):
        self.posts.insert(entry)

    def get_entries(self):
        for p in self.posts.find():
            print p

    def delete_entries(self, entry):
        self.posts.remove(entry)

    def add_user(self, user):
        uid = user["userid"]
        self.user_collection.insert(user)
        self.friend_collection.insert({"userid": uid, "friend_list": []})

    def add_friend(self, uid, friend):
        print self.friend_collection.find({"userid": uid})[0]["friend_list"]
        friend_list = self.friend_collection.find({"userid": uid})[0]["friend_list"]
        if not friend in friend_list:
            friend_list.append(friend)
            self.friend_collection.update(
                {"userid": uid},
                {
                    "userid": uid,
                    "friend_list": friend_list
                }
            )
            print self.friend_collection.find({"userid": uid})[0]["friend_list"]
            return "friend added successfully"
        else:
            return "friend is already added"

    def list_friends(self, uid):
        print self.friend_collection.find({"userid": uid})
        return self.friend_collection.find({"userid": uid})[0]["friend_list"]

    def find_user(self, uid):
        try:
            return self.user_collection.find(uid)[0]
        except:
            return None


