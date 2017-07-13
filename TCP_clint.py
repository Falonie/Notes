#clint
import socket
#create a socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#create connection
s.connect(('www.zhihu.com',80))
#send data
s.send(b'GET / HTTP/1.1\r\nHost: www.zhihu.com\r\nConnection: close\r\n\r\n')
#receive data
buffer=[]
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
#close connection
s.close()

header,html=data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('zhihu.html','wb') as f:
    f.write(html)