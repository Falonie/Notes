a={'name':'Shake','age':20,'gender':'male'}
#a={'a':1,'b':2,'c':3}
#a=['name','age','gender']
#for i in a.items():
for i,m in a.items():
#for i in a.values():
    #print(i)
	print(i,m)
for i in enumerate(a):
    print(i)	
from collections import Iterable
print(isinstance(a,Iterable)) 