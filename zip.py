a = [1, 2, 3]
b = ['a', 'b', 'c']
for m, n in zip(a, b):
    print(m, n)

print(tuple(zip(a, b)))
print(list(zip([2, 3, 4], ['u', 'i', 'o'])), '\n')

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
print(A0)
print([A0[s] for s in A0], '\n')

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)
print(a == b)
print(a is c, a == c)