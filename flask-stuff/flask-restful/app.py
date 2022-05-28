from flask import Flask,jsonify,request
from flask_restful import Resource, Api ,reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate,identity
app = Flask(__name__)
app.secret_key = "anupam"
api = Api(app)

items = []

jwt = JWT(app,authenticate,identity)

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',required="True",help="this cannot be left blank")

    @jwt_required()
    def get(self,name):
        for item in items:
            if item.get('name') == name:
                return jsonify({'item': item})
        return ({'message': 'nhi h item'})
        # item = (list(filter(lambda x : x.get('name')==name,items)),None)
        # return ({'item':item},200 if item else 404)
    def post( self, name):
        # request_data = request.get_json()
        for item in items:
            if item.get('name') == name:
                return ({'message': 'an item already exist with the same name'})
        Item.parser.add_argument('name',required="True",help="this cannot be left blank")
        data = Item.parser.parse_args()
        item = {'name':name, 'price':data['price']}
        items.append(item)
        return jsonify({'item': item})
    
    def delete(self,name):
        global items
        temp_items = []
        for item in items:
            if item.get('name')!=name:
                temp_items.append(item)
        items = temp_items
        return ({"message":"item deleted"})

    def put(self,name):
        global items
        # data = request.get_json()
        data = Item.parser.parse_args()
        item = next(iter(filter(lambda x:x['name'] == name, items)),None)
        if item:
            temp = {'name':name,'price':data['price']}
            item.update(temp)
        else:
            temp = {'name':name,'price':data['price']}
            items.append(temp)
            return temp
        return item



class Items(Resource):
    def get(self):
        if items:
            return jsonify({'items': items})
        else:
            return ({"message": "nhi h item"} ,404)

    def post( self, name):

        item = {'name':name, 'price':12.00}
        items.append(item)
        return jsonify({'item': item})
    
    


api.add_resource(Item,'/item/<string:name>') #http://127.0.0.1:5000/item/anupam

api.add_resource(Items,'/items')

app.run(debug=True)