import asyncio, threading


# @asyncio.coroutine
# def hello():
#     print('Hello world! {}'.format(threading.currentThread()))
#     r = yield from asyncio.sleep(1)
#     print("Hello again! {}".format(threading.currentThread()))

async def hello():
    print('Hello world! {}'.format(threading.current_thread()))
    r = await asyncio.sleep(1)
    print('Hello again! {}'.format(threading.current_thread()))

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# @asyncio.coroutine
# def wget(host):
#     print('wget {}...'.format(host))
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHOST:{}\r\n\r\n'.format(host)
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('{} header > {}'.format(host, line.decode('utf-8').rstrip()))
#     writer.close()
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.close()