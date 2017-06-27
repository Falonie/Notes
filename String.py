import string,re

a='wer./:;<=>?'
print(string.punctuation)
print(a.strip(string.punctuation))
print(a.split(" "))
b='123abc'
print(b.strip('12c'))
c='a,  b, c '
print(re.split('[\s\,]+',c))
print(c.split(','))

name='Ason'
print('My name is %s.'%name)
print('My name is {name}.'.format(name=name))