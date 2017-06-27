import functools

name=['Aderson','Bob','James','Adams','Beson']
b=['Kevin']
p=name.pop(3)
print(p)
name.append('Shake')
name.append(['name'])
name.extend(b)
name.extend(['gender'])
name.insert(1,'Curry')
print(name)
p1=name.remove('Bob')
print(name)
name.remove(['name'])
#name.sort()
name.reverse()
print(name)
print(sorted(name))

a=(1,2,3,4,5,)
print(a)

print([x.lower() for x in name])
print([x.capitalize() for x in name])

def decrator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper
@decrator
def func(x,y):
    return '<h1>{0}</h2>'.format(x * y)

print(func(2,3))