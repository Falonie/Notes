print(type('123'),type(123),type(True))
print(isinstance(123,int))

class Object(object):
    def __init__(self):
        self.name='caren'
n=Object()
print(hasattr(n,'name')) #判断存在属性'name'
print(setattr(n,'score',95)) #设定属性'score'
print(getattr(n,'name')) #获取属性‘name’