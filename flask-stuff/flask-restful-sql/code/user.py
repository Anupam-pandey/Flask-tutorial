import sqlite3
from flask_restful import Resource,request,reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.password = password
        self.username = username
    
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.Connection("mydata.db")
        cursor = connection.cursor()
        query = "select * from users where username=?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()
        if row:
            #user = cls(row[0],row[1],row[2]) # same as below
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.Connection("mydata.db")
        cursor = connection.cursor()
        query = "select * from users where id=?"
        result = cursor.execute(query,(_id,)) #tuple need to be passed always
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user



class  UserRegister(Resource):
    parser = reqparse.RequestParser()
    def post(self):
        #data = request.get_json()
        UserRegister.parser.add_argument('username', required=True)
        UserRegister.parser.add_argument('password', required=True)
        data = UserRegister.parser.parse_args()
        username = data['username']
        password = data['password']
        if User.find_by_username(username):            
            return ({'message':'already exist'})
        else:
            connection = sqlite3.Connection("mydata.db")
            cursor = connection.cursor()
            query = "insert into users values (NULL,?,?)"
            cursor.execute(query,(username,password,))
            connection.commit()
            connection.close()
            return ({'message':'done'})


