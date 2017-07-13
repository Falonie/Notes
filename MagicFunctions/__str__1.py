class Employee(object):
    def __init__(self,name):
        self.name = name
    def get(self):
        return self.name

n=Employee('Caren')
print(n.get())