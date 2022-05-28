import sqlite3

connection = sqlite3.Connection("mydata.db")
cursor = connection.cursor()

create_table = "create table  if not exists  users (id int, username text, password text)"
cursor.execute(create_table)

user = (1,'bob', 'asdf')

insert_query = "insert into users values(?,?,?)"


users = [
(1,'ronnie', 'asdf'),
(1,'rolf', 'asdf'),
(1,'anne', 'asdf')
]
cursor.execute(insert_query,user)

cursor.executemany(insert_query, users)

select_query = "select * from users"
for row in  cursor.execute(select_query):
    print row 

connection.commit()
connection.close()