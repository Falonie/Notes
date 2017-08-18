import string, re, math

a = 'wer./:;<=>?'
print(string.punctuation)
print(a.strip(string.punctuation))
print(a.split(" "))
b = '123abc'
print(b.strip('12c'))
c = 'a,  b, c '
print(re.split('[\s\,]+', c))
print(c.split(','))

name = 'Ason'
print('My name is %s.' % name)
print('My name is {name}.'.format(name=name))

print('{:.1f}'.format(3.111111112412))
number = math.pi
print('{pi:.4f}'.format(pi=number))

d = b'\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2\xe5\x92\x8c\xe7\xbc\x96\xe7\xa0\x81'
print(d.decode(encoding='utf-8'))
print('中国')
print('中国'.encode(encoding='utf-8'))
print('中国'.encode(encoding='utf-8').decode(encoding='utf-8'))
print('中国'.encode(encoding='gbk'))
print('中国'.encode(encoding='gbk').decode(encoding='gbk'))
e = b'\xe4\xb8\xad\xe5\x9b\xbd'
print(e.decode(encoding='utf-8'))