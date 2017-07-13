s={1,2,3}
s.add(4)
print(s)

a=(2,3,4,2,3,)
print(set(a),frozenset(a))

s1=set(range(10))
s1.remove(7)
s1.pop()
print(s1)
s1.clear()
print(s1)

s2=frozenset(['e',4,'t'])
print(s2)

#s3=set(['e','r','h',3])
s3={'e','r','h',3}
print(s3.pop())

print(s2|s3)
print(s2&s3)
print(s3.update(s))

f=frozenset(['name'])
print(dict(f='caren'))

a={2,3,'t'}
print(type(a))
