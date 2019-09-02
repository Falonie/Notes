import time
import functools
import threading
import pymysql

connection_local = pymysql.connect(host='localhost', user='root', password='1234', db='Falonie', charset='utf8mb4')


def decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func = f(*args, **kwargs)
        next(func)
        return func
    return wrapper


@decorator
def my_coroutine():
    while True:
        received = yield
        print('Received:', received)


it = my_coroutine()
it.send('First')
for _ in range(10):
    it.send(_)


def query_mysql_local2():
    with connection_local.cursor() as cursor:
        sql = "SELECT * FROM python_areas_province_city_county_name"
        # sql_insert = 'INSERT INTO python_areas_province_city_county_remove VALUES (%s)'
        # sql_insert = 'INSERT INTO python_areas_province_city_county_remove VALUES ("{}")'
        cursor.execute(query=sql)
        yield from cursor.fetchall()


# for _ in query_mysql_local2():
#     print(_)
def generate_mysql(f):
    # g = query_mysql_local2()
    g = f
    while True:
        try:
            n = g.send(None)
            print(n)
        except StopIteration:
            break


# generate_mysql(query_mysql_local2())
# generate_mysql(query_mysql_local2())
def start(f):
    threading.Thread(target=generate_mysql, args=(f,)).start()

# start(query_mysql_local2())
