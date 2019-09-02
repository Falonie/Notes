# num=int(input('please input a number:'))
# def func(num):
#     a = []
#     for i in range(1,num+1):
#         if num % i != 0 and i / 1 == i:
#             a.append(i)
#         else:
#             pass
#     return a
# print(func(num))

def func(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)


# func('caren', 4, 3, 'u', age='27')