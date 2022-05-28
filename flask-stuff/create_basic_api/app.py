from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

@app.route('/') #accessing like http://www.google.com
def home():
    return render_template('index.html')



# from browser prospective the get request is use to send data back only
# from browser prospective the post request is use to recieve data 

# create apis for following scenarios


stores = [
    {
        'name':'my store',
        'items':
        [
            {
            'name': 'my item',
            'price':15.99
            }
        ]
    }
]





#post /store data:{name}
@app.route('/store',methods=["post"])
def create_store():
    request_data = request.get_json()
    new_store = {
         'name' : request_data['name'],
         'items' : []
    }
    stores.append(new_store)
    return jsonify({'stores': stores})


#get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store.get('name') == name:
            return jsonify({'stores': stores})
    return jsonify({'message':'store not found'})
   


#get /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

#post /store/<string:name>/item {name:price}
@app.route('/store/<string:name>/item',methods=["post"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store.get('name') == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price'],
            }
            store['items'].append(new_item)
            return jsonify({'stores': stores})
    return jsonify({'message':'item not found'}) 

#get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store.get('name') == name:
            return jsonify({'items': store.get('items')})
    return jsonify({'message':'item not found'})





app.run()