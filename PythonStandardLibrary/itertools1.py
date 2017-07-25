import itertools

#1
#a=itertools.count(1)
#for b in a:
#    print(b)
#2
# b=itertools.cycle('ABBC')
# for c in b:
#    print(c)
#3
#for d in itertools.repeat('S',9):
#    print(d)
#4
#d=itertools.count(1)
#m=itertools.takewhile(lambda x:x<10,d)
#print(list(m))
#5 chain()
#for f in itertools.chain('ABC','123'):
#    print(f)
#6 groupby()

animals=['lion','panda','tiger','goose','zbra','whale','shark']
for key,group in itertools.groupby(animals,key=len):
        print(key,list(group))