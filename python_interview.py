import functools

#16 单例模式

# def SingleTon(cls,*args,**kwargs):
#     instances = {}
#     def _singleton():
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#             return instances[cls]
#         return _singleton
# @SingleTon
# class TestClass(object):
#     a=1
# test1=TestClass()
# test2=TestClass()
# print(test1.a,test2.a)

def decrator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return '{}:{}'.format(wrapper.__name__, result)
    return wrapper
@decrator
def func(x,y):
    return x * y
print(func(2,3))