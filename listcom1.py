from functools import reduce

print([d + d for d in range(100)])
L = ['Hello', 'World', 18, 'Apple', None]
print([m.lower() for m in L if isinstance(m,str)])

L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])

#print(reduce((lambda x:x**2),range(1,10)))
print(reduce((lambda x, y: x + y), [1, 2, 3]))

numbers=list(range(50))
print([x**2 for x in numbers if x%2==0])

print(['%s * %s = %s'% (x,y,x*y) for x in range(1,10) for y in range(1,x+1)])