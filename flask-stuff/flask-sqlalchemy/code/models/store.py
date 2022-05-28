import sqlite3
from db  import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    name = db.Column(db.String(80))
    id = db.Column(db.Integer, primary_key=True)

    items = db.relationship('ItemModel', lazy='dynamic') #many to one relationship so this would return a list of items

    # TABLE_NAME = 'items'
    def __init__(self, name):
        self.name = name
    
    def json(self):
        return ({'name':self.name,'items':[item.json() for item in self.items.all()]})
    
    @classmethod
    def find_by_name(cls, name):
        #return ItemModel.query.filter_by(name=name).filter() #done with the help of sql alchemy , returns item object by default & all the below code is same as this line 
        return cls.query.filter_by(name=name).first() #done with the help of sql alchemy , returns item model object by default & all the below code is same as this line 

        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()

        # if row:
        #     #return {'item': {'name': row[0], 'price': row[1]}}
        #     #return cls(row[0],row[1])
        #     return cls(*row)

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    
    def save_to_db(self):
        db.session.add(self) # automatic translation of object to row by sql alchemy also it can do update any old rows as well (UPSERTING the data) so update function is also not needed
        db.session.commit()
        
        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO {table} VALUES(?, ?)".format(table=ItemModel.TABLE_NAME)
        # cursor.execute(query, (self.name, self.price))

        # connection.commit()
        # connection.close()
    
    # def update(self):

        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()

        # query = "UPDATE {table} SET price=? WHERE name=?".format(table=ItemModel.TABLE_NAME)
        # cursor.execute(query, (self.price, self.name))

        # connection.commit()
        # connection.close()

