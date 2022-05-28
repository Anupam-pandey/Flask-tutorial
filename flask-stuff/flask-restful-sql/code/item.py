import sqlite3
from flask import jsonify
from flask_restful import reqparse, request, Resource
from flask_jwt import jwt_required

def create_connection():
    connection = sqlite3.Connection("mydata.db")
    cursor = connection.cursor()
    return cursor,connection
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',required="True",help="this cannot be left blank")

    @jwt_required()
    def get(self,name):
        cursor,connection = create_connection()
        query = "select * from Items where name = ?"
        row = cursor.execute(query,(name,)).fetchone()
        connection.close()
        
        if row:
            return jsonify({'item': row[0],'price':row[1]})
        return ({'message': 'nhi h item'})  

        # for item in items:
        #     if item.get('name') == name:
        #         return jsonify({'item': item})
        # return ({'message': 'nhi h item'})
        # item = (list(filter(lambda x : x.get('name')==name,items)),None)
        # return ({'item':item},200 if item else 404)
    def post( self, name):
        cursor,connection = create_connection()
        query = "select * from items where name = ?"
        row = cursor.execute(query,(name,)).fetchone()
        if row:
            connection.close()
            return ({'message': 'an item already exist with the same name'})
        query = "insert into items values(?,?)"
        request_data = Item.parser.parse_args()
        # request_data = request.get_json()
        row = cursor.execute(query,(name,request_data['price'],))
        connection.commit()
        connection.close()
        if row:
            return jsonify({'message':'done'})
        return jsonify({'message':'error'})

        # request_data = request.get_json()
        # for item in items:
        #     if item.get('name') == name:
        #         return ({'message': 'an item already exist with the same name'})
        # item = {'name':name, 'price':data['price']}
        # items.append(item)
        # return jsonify({'item': item})
    
    def delete(self,name):
        cursor,connection = create_connection()
        query = "select * from items where name = ?"
        row = cursor.execute(query,(name,)).fetchone()
        if not row:
            connection.close()
            return ({'message': 'no item exist with this same name'})
        query = "delete from items  where name =(?)"
        # request_data = request.get_json()
        row = cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return ({"message":"item deleted"})
        # global items
        # temp_items = []
        # for item in items:
        #     if item.get('name')!=name:
        #         temp_items.append(item)
        # items = temp_items
        # return ({"message":"item deleted"})

    def put(self,name):
        cursor,connection = create_connection()
        query = "select * from items where name = ?"
        row = cursor.execute(query,(name,)).fetchone()
        if not row:
            query = "insert into items values(?,?)"
            request_data = Item.parser.parse_args()
            # request_data = request.get_json()
            row = cursor.execute(query,(name,request_data['price'],))
            connection.commit()
            connection.close()
            return ({'message': 'created'})
        else:
            query = "update items set price = ? where name = ?"
            request_data = Item.parser.parse_args()
            # request_data = request.get_json()
            row = cursor.execute(query,(request_data['price'],name,))
            return ({'message': 'updated'})
            connection.commit()
            connection.close()
        
        # global items
        # # data = request.get_json()
        # data = Item.parser.parse_args()
        # item = next(iter(filter(lambda x:x['name'] == name, items)),None)
        # if item:
        #     temp = {'name':name,'price':data['price']}
        #     item.update(temp)
        # else:
        #     temp = {'name':name,'price':data['price']}
        #     items.append(temp)
        #     return temp
        # return item



class Items(Resource):
    def get(self):
        cursor,connection = create_connection()
        query = "select * from items"
        result = cursor.execute(query)
        items_list = []
        for row in result:
            items_list.append({'name':row[0],'price':row[1]})
        connection.close()
        return ({'items':items_list})

    def post( self, name):

        item = {'name':name, 'price':12.00}
        items.append(item)
        return jsonify({'item': item})
    
    