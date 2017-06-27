class Student(object):
    def set_age(self, age): 
        self.age = age
s = Student()
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 测试结果