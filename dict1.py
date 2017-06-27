from copy import copy,deepcopy
import copy,operator

def my_abs(x):
    return x if x > 0 else -x
print(my_abs(-9))

x={'name':'aaa','age':'19'}
y={'gender':'male'}
print(dict(list(x.items())+list(y.items())))
z=x.copy()
z.update(y)
print(z)
print(x)
print(sorted(z.items(),key=lambda x:x[0]))
print(sorted(z.items(),key=operator.itemgetter(1)))

def foo(a=[]):
    if not a:
        a.append(5)
    else:
        pass
    print(a)
foo()
foo()
foo()