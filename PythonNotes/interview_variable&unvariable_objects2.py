a = 0
print('a', id(a))
a = 1
print('a', id(a))
print()

a = 1
print('a', id(a))
b = 1
print('b', id(b))
print(a == b, a is b)
c = 'python'
print('c', id(c))
d = 'python'
print('d', id(d))
print(c == d, c is d)
print()

m = [1, 2, 3]
print('m', m, id(m))
m[1] = 4
print('m', m, id(m))
m.append(5)
print('m', m, id(m))
