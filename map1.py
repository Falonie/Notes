def fuc(x):
    return x*x
print(tuple(map(fuc,[1,2,3])))
print(list(map(lambda x:x**2,range(10))))
print(tuple(map(str,[1,2,3])))
print(list(map(int,['1','2','3','4'])),'\n')

print(list(map(lambda x,y:x*y,[2,3,5,6,9],[0,4,6,2,1])))
