from io import StringIO

n = StringIO()
n.write('I want to be a python engineer!')
print(n.getvalue())

f = StringIO('Hello python engineer!')

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())