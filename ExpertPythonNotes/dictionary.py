print(dict((['a', 1], ['b', 2])))

print(dict(zip('ab', range(2))))
# print(dict(map(None,'abc',range(2))))

print({k: v for k, v in zip('abc', range(3))})

d = {'a': 1, 'b': 2}
d.setdefault('a', 100)
print(d)

d.setdefault('c', 200)
print(d)
