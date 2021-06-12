from App import app
from flask_sqlalchemy import SQLAlchemy

db  = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id_convers = db.Column(db.Integer, autoincrement = True)
    sender = db.Column(db.String(30),primary_key = True)
    
db.create_all()