import sqlite3

conn=sqlite3.connect('test.db')
#create a cursor
cursor=conn.cursor()
#execute a SQL argument to create a table
cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
#to insert a record into the table
cursor.execute('insert into user (id,name) values (\'1\',\'Michael\')')
#to get rowcountq
cursor.rowcount
#close cursor
cursor.close()

conn.commit()
#close connection
conn.close()

