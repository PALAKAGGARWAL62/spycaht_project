from datetime import datetime


class spy:
    def __init__(self, name, age, rating):
        self.name = name
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status = None


class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        time = datetime.now ()
        self.time = time.strftime ("%a, %d %b %Y %H:%M:%S")
        self.sent_by_me = sent_by_me


Spy = spy ('Mr Peter', 15, 3.2)
