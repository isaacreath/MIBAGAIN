from DB import Database


class Message():

    def __init__(self):
        self.db = Database()

    def drop_message(self, user_id, message_x, message_y, message, viewable_by, is_picture):
        message_coordinates = (message_x, message_y)
        print "(" + str(message_coordinates) + ") " + str(message)
        message_entry = {"coordinates":message_coordinates,
                         "message":message,
                         "userid":user_id,
                         "viewable_by":viewable_by,
                         "is_picture":is_picture
                        }
        self.db.insert(message_entry)
        self.db.get_entries()

    def pickup_message(self, user_id, user_x, user_y):
        #This is an estimation... The length of a single degree of latitude changes as the longitude changes. This won't
        #work accurately for latitudes within about 20-30 degrees of either pole.
        #360 degrees / 40075 km = .00898 degrees/km = .00000898 degrees/km ~= .00001

        # coords = (user_x, user_y)
        # p = self.db.posts.find({"coordinates": coords})

        # p = self.db.posts.find({"coordinates":(
        #     {"$gt": user_x + .01, "$lt": user_x + .01},
        #     {"$gt": user_y + .01, "$lt": user_y + .01}
        #                                       )})

        # This is shit... Hung would be ashamed of us.
        for p in self.db.posts.find():
            if(p["coordinates"][0] >= user_x - 0.00001 and p["coordinates"][0] <= user_x + 0.00001):
                if(p["coordinates"][1] >= user_y - 0.00001 and p["coordinates"][1] <= user_y + 0.00001):
                    if(p["userId"] != user_id): #Don't want user to pick up his own message
                        self.db.delete_entries(p)
                        return p
        # print str(p[0]),'\n'
        return "NONE"