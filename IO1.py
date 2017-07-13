f=open('C:/python/python.txt','r',encoding='gbk')
print(f.read())
f.close()

with open('C:/python/python1.txt','r',encoding='gbk') as f:
    print(f.read())
	
f=open('C:/python/python.txt','w')
print(f.write('python engineer'))
f.close()

with open('C:/python/python1.txt','w') as f:
    print(f.write('python developer'))