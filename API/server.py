from flask import Flask
from flask import request, jsonify
from DB import Database
from messages import Message
from friends import Friend
from users import User


#setup the app and the db
app = Flask(__name__)
db = Database()
messages = Message()
friends = Friend()
users = User()


def validate_post_request(args):
    for arg in args:
        if arg is None:
            return False
    return True

@app.route("/login", methods=['POST'])
def login():
    uid = int(request.form.get('uid'))
    username = request.form.get('username')
    print uid
    return users.login(uid, username)


@app.route("/addUser", methods=['POST'])
def add_user():
    username = request.form.get('username')
    uid = int(request.form.get('uid'))
    users.add_user(uid, username)
    return "OKAY"

@app.route("/addFriend", methods=['POST'])
def add_friend():
    uid = int(request.form.get('uid'))
    friend_name = request.form.get('friend')
    friends.add_friend(uid, friend_name)
    return "OKAY"

@app.route("/listFriends", methods=['POST'])
def list_friends():
    uid = int(request.form.get('uid'))
    x = {"friends list": friends.list_friends(uid)}
    return jsonify(x)


'''
Endpoint for adding a new bottle to the database. Requires 5 arguments
x: the x coordinate where the bottle is dropped (float)
y: the y coordinate where the bottle is dropped (float)
message: the content of the message  (plain text, or matrix representation of picture/video)
userId: the unique user id of the user who dropped the message (int)
viewable_by: a string containing who can view the message (friend or public)

'''

@app.route("/dropMessage", methods=['POST'])
def drop_message():
    message_x = request.form.get('x', type=float)
    message_y = request.form.get('y', type=float)
    message = request.form.get('message')
    user_id = request.form.get('userId')
    viewable_by = request.form.get('viewableBy')
    is_picture = request.form.get('isPicture')
    args = [user_id, message_x, message_y, message, viewable_by, is_picture]
    if validate_post_request(args):
        messages.drop_message(user_id, message_x, message_y, message, viewable_by, is_picture)
        return "Post Successful\n"
    else:
        return "Invalid argument matching\n", 400

@app.route("/pickupMessage", methods=['POST'])
def pickup_message():
    user_x = request.form.get('x', type=float)
    user_y = request.form.  get('y', type=float)
    user_id = request.form.get('userId')
    args = [user_x, user_y, user_id]
    if validate_post_request(args):
        print "Pickup successful\n"
        temp = messages.pickup_message(user_id, user_x, user_y)
        return str(temp)
    else:
        return "Invalid argument matching\n", 400


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run()
