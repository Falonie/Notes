from collections import Iterator

print(isinstance(iter({'name': 'abc', 'gender:': 'female'}), Iterator))
print(isinstance(iter([1, 2, 3]), Iterator))
print(isinstance(iter('acs'), Iterator))
print(isinstance(iter(x * x for x in tuple(range(100))), Iterator))