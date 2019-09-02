import random

a = [1, 3, 'r', True, 'k']
print(random.choice(a))

a = [1, 2, 3]
a += [4, 5]
print(a)
print(a.__getitem__(2))
a.__setitem__(0,False)
a.__delitem__(0)
print(a)