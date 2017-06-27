import json
#d=dict(name='Caseny',salary=18000)
#json.dumps(d)
#f='{'name':'kitty','age':20}'
#json.loads(f)

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
def studentdict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
s=Student('kitty',20,90)
#print(json.dump(s,default=studentdict()))