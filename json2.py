import json,sys
from imp import reload
reload(sys)

d=dict(name='Falonie',salary=18000)
a=json.dumps(d)
print(a,type(d),type(a))

f='{"name":"kitty","age":"20"}'
# f='{"first_name": "Guido", "last_name":"Rossum"}'
b=json.loads(f)
print(b['name'],type(b),b,type(f))
print('\n')

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return 'name:{} age:{} score:{}'.format(self.name,self.age,self.score)

def studentdict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

s=Student('kitty',20,90)
print(s,type(s))
s1=json.dumps(s,default=studentdict)
print(s1,type(s1))
s2=json.dumps(s,default=lambda x:x.__dict__)
print(s2,type(s2))

print('\n')
s3=json.loads(s2)
print(s3,type(s3))