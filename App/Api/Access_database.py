from random import randint
import time 
from .CreateDatabase import db, User


class Database:
    def __init__(self):
        pass

    def write_user(self, data):
        mess = User(sender = data['sender'])
        db.session.add(mess)
        db.session.commit()
