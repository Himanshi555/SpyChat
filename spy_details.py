from datetime import datetime
class SPY:

    def __init__(self, name, salutation, age, rating, is_online):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = is_online
        self.chats = []
        self.current_status_message = None

class ChatMessage:

    def __init__(self, message, send_by_me):
        self.message = message
        self.timeStamp = datetime.now()
        self.send_by_me = send_by_me
