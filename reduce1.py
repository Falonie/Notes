from functools import reduce 
def str2float(x,y):
    return x * 10 + y
def fun(s):
    return{'1':1,'2':2,'3':3,'4':4,'5':5,'6':6}[s]
print(reduce(str2float,map(fun,'123456')))
#print(list(map(fun,'123456')))
#print(list(map(int,'123456')))

def fuc(x,y):
    return x*y
print(reduce(fuc,[2,3,4,5]))

def prod(x,y):
    return x*y
print(reduce(prod,[2,3,4,5,6]))