from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return ({'message':'store not found'},404)

    def post(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return ({'message','this store already exist'})
        
        store = StoreModel(name)
        try :
            store.save_to_db()
        except:
            return ({'message':'some issue is there'},400)
        return store.json()


        

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if not store:
            return ({'message','this store doesnt exist'})
        try:
            store.delete_from_db()
        except:
            return ({'message':'some issue is there'},400)

        return ({'message':'store is deleted'},200)

        
        




class StoreList(Resource):
    def get(self):
        return ({'stores':[store.json() for store in StoreModel.query.all()]})
