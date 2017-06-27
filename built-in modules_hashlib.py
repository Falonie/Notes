import hashlib

md5=hashlib.md5()
md5.update('I love python!'.encode('utf-8'))
md5.update('I wanna to be python developer!'.encode('utf-8'))
print(md5.hexdigest())

sha1=hashlib.sha1()
sha1.update('6666666666666'.encode('utf-8'))
print(sha1.hexdigest)

sha256=hashlib.sha256()
sha256.update('2333p333333'.encode('utf-8'))
print(sha256.hexdigest)