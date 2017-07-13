import sqlite3

connection = sqlite3.connect('test1.db')

# try:
# with sqlite3.connect('test1.db').cursor() as cursor:
#     for row in cursor.execute('select * from book'):
#         print(row)
#     connection.commit()

with sqlite3.connect('test1.db') as conn:
    c = conn.cursor()
    for row in c.execute('select * from book'):
        print(row)
    conn.commit()