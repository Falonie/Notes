import re
pattern=re.compile(r'([\w\_\-\.]+)@([gmail|microsoft])+(\.com)$')
#a=re.compile(r'[A-Za-z0-9\-\_\.]{2,10}@gmail|microsoft.com$')
#a=re.compile(r'[gmail|microsoft]$')
#b='541002901@gmail.com'
#b='541002901@qq.com'
#b='541002901@gmail.edu'
b=input('Please create a mail address:')
if pattern.match(b):
    print(pattern.match(b).groups())
else:
    print('Fail.')