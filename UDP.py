import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))

print('Bind UDP on 9999...')
while True:
    #receive data
    data,addr=s.recvfrom(1024)
    print('Receive from %s:%s.'%addr)
    s.sendto(b'Hello,%s!'%data,addr)