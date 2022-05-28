import sqlite3
from models.user import UserModel
from flask_restful import Resource,request,reqparse

class  UserRegister(Resource):
    parser = reqparse.RequestParser()
    def post(self):
        #data = request.get_json()
        UserRegister.parser.add_argument('username', required=True)
        UserRegister.parser.add_argument('password', required=True)
        data = UserRegister.parser.parse_args()
        username = data['username']
        password = data['password']
        if UserModel.find_by_username(username):            
            return ({'message':'already exist'})
            print "hi 2"
        else:
            user = UserModel(username,password)
            # user = UserModel(**data) #same as above , unpacking data args
            print "hi"
            user.save_to_db()
            # connection = sqlite3.Connection("mydata.db")
            # cursor = connection.cursor()
            # query = "insert into users values (NULL,?,?)"
            # cursor.execute(query,(username,password,))
            # connection.commit()
            # connection.close()
            return ({'message':'done'})


