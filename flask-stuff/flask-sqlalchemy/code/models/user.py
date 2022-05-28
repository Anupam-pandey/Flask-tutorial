import sqlite3
from flask_restful import Resource,request,reqparse
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    id = db.Column(db.Integer, primary_key=True)


    def __init__(self, username, password):
        self.password = password
        self.username = username
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

        # connection = sqlite3.Connection("mydata.db")
        # cursor = connection.cursor()
        # query = "select * from users where username=?"
        # result = cursor.execute(query,(username,))
        # row = result.fetchone()
        # if row:
        #     #user = cls(row[0],row[1],row[2]) # same as below
        #     user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id = _id).first() #cls.query means select * from <table> 
        # connection = sqlite3.Connection("mydata.db")
        # cursor = connection.cursor()
        # query = "select * from users where id=?"
        # result = cursor.execute(query,(_id,)) #tuple need to be passed always
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
