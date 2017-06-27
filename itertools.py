import itertools

x=itertools.accumulate(range(10))
print(list(x))

x=itertools.chain(range(5),range(3))
print(list(x))