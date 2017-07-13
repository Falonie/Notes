from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

#namedtuple
point=namedtuple('a',['x','y'])
p=point(1,2)
print(p.x)
circle=namedtuple('circle',['x','y','r'])
a=circle(2,2,3)
print(a.r)

#deque
a=deque(['a','b','c',3])
a.append(False)
a.pop()
a.appendleft(True)
a.popleft()
a.insert(1,1)
a[0]=0
print(a)

#defaultdict
a=defaultdict(lambda:'N/A')
a['key1']=1
print(a['key1'],a['key2'])

#OrderedDict
d=dict([('a',1),('b',2),('c',3)])
print(d)
e=OrderedDict([('a',1),('b',2),('c',3)])
print(e)

#Counter
b=Counter()
for a in 'Python Developer':
    b[a]=b[a]+1
print(b)