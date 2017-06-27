import functools
int2=functools.partial(int,base=2)
int3=functools.partial(int,base=16)
print(int2('0101010'))
print(int3('233AE'))

max10 = functools.partial(max, 10,233,8)
print(max10(1,2,3,4,5,600))
max1=functools.partial(max,10)
print(max1(2,11,80))

# max2 = functools.partial(max, 10)
# print(max2(5, 6, 7))