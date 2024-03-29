from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from user import UserRegister
from item import Item, Items

from security import authenticate,identity
app = Flask(__name__)
app.secret_key = "anupam"
api = Api(app)


jwt = JWT(app,authenticate,identity)



api.add_resource(Item,'/item/<string:name>') #http://127.0.0.1:5000/item/anupam

api.add_resource(Items,'/items')

api.add_resource(UserRegister,'/register')


if __name__ == '__main__':
    app.run(debug=True)