from copy import copy,deepcopy

d={}
d['name']='A'
d['score']='95'
print(d)

a={'name':'Eric','age':'20','course':['mathmatics']}
b=copy(a)
b['age']='25'
d=deepcopy(a)
a['name']='Wolf'
a['course'].append('Science')
b['course'].append('Biology')
print(a)
print(b)
print(d)
print(a.get('gender'))
print(a.popitem())
print(a)
# del a['name']
# print(a)
# print(a.popitem())
# a.clear()

e={'gender':'male','score':'90'}
z=dict(list(a.items())+list(e.items()))
y=copy(a)
print(z)