import sqlite3

connection = sqlite3.Connection("mydata.db")
cursor = connection.cursor()

create_table = "create table  if not exists  users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

user = (4,'bob', 'asdf')

insert_query = "insert into users values(?,?,?)"


users = [
(1,'ronnie', 'asdf'),
(2,'rolf', 'asdf'),
(3,'anne', 'asdf')
]
cursor.execute(insert_query,user)

cursor.executemany(insert_query, users)

select_query = "select * from users"
for row in  cursor.execute(select_query):
    print row 





create_table = "create table  if not exists  items (name text, price real)"
cursor.execute(create_table)

items = [
('chair', '15.00'),
('table', '16.00'),
('piano', '17.00')
]


insert_query = "insert into items values(?,?)"
cursor.executemany(insert_query, items)


connection.commit()
connection.close()
