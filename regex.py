import re

print('a b   c'.split(' '))
print(re.split(r'[\s\;]+', 'a, b;  c    d'))
print(re.split(r'[\s\,\;]+', 'a,b,;  c     d'))

f = re.match(r'^(\d{4})-(\d{4,9})$', '0580-6369353')
print(f.groups())
print(f.group(0), f.group(1), f.group(2))

print(re.match(r'^(\d+?)(0*)$', '10010').groups())

re_telephone = re.compile(r'^(\d{4})(\d{0,8})$')
print(re_telephone.match('10086').groups())
# note:\d,\w,\d{5},\d+,\s,\s+,\d{0,9},\-
# [0-9a-zA-Z\_],[0-9a-zA-Z\_]+,[a-zA-Z\_][0-9a-zA-Z\_]*
# A|B,^\d,\d$