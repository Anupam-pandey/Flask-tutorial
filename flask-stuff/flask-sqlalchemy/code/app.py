from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store,StoreList
from db import db
from security import authenticate,identity
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
app.secret_key = "anupam"
api = Api(app)

@app.before_first_request
def create_tables():
    print "hi 3"
    db.create_all()
    print "hi 4"


jwt = JWT(app,authenticate,identity)




api.add_resource(Store,'/store/<string:name>')

api.add_resource(StoreList,'/stores/')

api.add_resource(Item,'/item/<string:name>') #http://127.0.0.1:5000/item/anupam

api.add_resource(Items,'/items')

api.add_resource(UserRegister,'/register')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)