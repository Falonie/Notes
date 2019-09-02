a = {'name': 'Shake', 'age': 20, 'gender': 'male'}
for i, m in a.items():
    print(i, m)

for i in enumerate(a):
    print(i)
from collections import Iterable

print(isinstance(a, Iterable))