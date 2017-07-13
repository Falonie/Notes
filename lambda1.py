#1
def fuc(a,b):
    return lambda: a ** 2 + b ** 2
f=fuc(1,2)
print(f())

#2
def fuc2():
    return lambda c, d: c ** 2 + d ** 2
f2=fuc2()
print(f2(3,4))

#3
def fuc3(x,y):
    def g():
        return x ** 2 + y ** 2
    return g
f3=fuc3(5,6)
print(f3())
print(fuc3(3,4)())

#4
def func():
    def h(m,n):
        return m ** 2 + n ** 2
    return h
f4=func()
print(f4(7,8))

#5
def i(m,n):
    return m ** 2 + n ** 2
print(i(2,3))

#6
print(tuple(map(lambda x:x**2,range(10))))
print(list(filter(lambda x:x%2==0,range(10))))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s,str)]
print(L2)