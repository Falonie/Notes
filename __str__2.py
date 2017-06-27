class Employee(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Employee object(name:%s)'%self.name
    #def get(self):
        #return self.name
n=Employee('Caren')
print(n)
print(n.__str__())
#print(n.get())
print(Employee('Aollen'))

