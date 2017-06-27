import sqlite3

# con=sqlite3.connect('test1.db')
# c=con.cursor()
connection=sqlite3.connect('test1.db')

with sqlite3.connect('test1.db') as con:
    c=con.cursor()
    #c.execute('drop table book')
    #c.execute('create table book(id INT PRIMARY KEY ,sort INT ,name text,price REAL ,category INT ,FOREIGN KEY (category) REFERENCES category(id))')

    books=[(1,1,'Python Cookbook',3.1,1),
           (2,3,'Introducing Python',17,2),
           (3,2,'R in Action',12,2)]
    #c.executemany('insert into book VALUES (?,?,?,?,?)',books)
    for value in c.execute('select * from book'):
        print(value)
    # values=c.fetchall()
    # for value in values:
    #     print(value)

#1 create table
# c.execute('CREATE TABLE category(id INT PRIMARY KEY ,sort INT ,name text)')
# c.execute('create table book(id INT PRIMARY KEY ,sort INT ,name text,price REAL ,category INT ,FOREIGN KEY (category) REFERENCES category(id))')

# con.commit()
# con.close()

#2 insert values into table
# books=[(1,1,'Python Cookbook',3.1,1),
#        (2,3,'Introducing Python',17,2),
#        (3,2,'R in Action',12,2)]
#
# c.execute('INSERT INTO category VALUES (1,1,\'kitchen\')')
# c.execute('INSERT INTO category VALUES (?,?,?)',[2,2,'computer'])
# c.executemany('INSERT INTO book VALUES (?,?,?,?,?)',books)

#3 query
# c.execute('SELECT * FROM category ORDER BY sort')
# print(c.fetchone())
# print(c.fetchone())
#
# c.execute('SELECT * FROM book WHERE book.category=1')
# print(c.fetchall())
#
# for row in c.execute('SELECT name,price FROM book ORDER BY sort'):
#     print(row)
#
# c.execute('UPDATE book SET price=? WHERE id=?',(50,3))
# c.execute('SELECT * FROM book')
# print(c.fetchall())
#
# con.commit()
# con.close()

#c.execute('DROP TABLE book')