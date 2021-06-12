from .Access_database import Database
import json
from datetime import datetime
from random import randint

database = Database()

class Process():
    def __init__(self,db = database):
        self.db = db

    def create_init(self):
        now = datetime.now()
        ra = randint(0,100000)
        dt_string = now.strftime("%d/%m/%Y/%H/%M/%S")+str(ra)
        data = {
                'sender':dt_string
                

        }
        self.db.write_user(data)
        
        # self.db.update_graph(gr,dt_string)
        return {
                'sender':dt_string
        }
                