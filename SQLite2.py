import sqlite3

with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE user (login VARCHAR (8),userid INTEGER )')
    cursor.execute('INSERT INTO user VALUES ("John",100)')
    cursor.execute('INSERT INTO user VALUES ("Jane",110)')
    #print(cursor.rowcount)
    #for eachUser in cursor.fetchall():
    #    print(eachUser)
    cursor.execute('SELECT * FROM user')
    values=cursor.fetchall()
    print(values)
    #cursor.execute('DROP TABLE user')
    cursor.close()
    conn.commit()