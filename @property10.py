class Employee(object):
    @property
    def salary(self):
        return self._salary
		
    @salary.setter  #turn method salary.setter into properties
    def salary(self,amount):
    #def set_salary(self,amount):
        if not isinstance(amount,int):
            raise ValueError('Error')
        if amount<5000:
            raise ValueError('Error')
        self._salary=amount
n=Employee()
#n.set_salary(15000)
#n.set_salary=15000
#n.amount=16000
n.salary=15000
print(n.salary)
#print(n.salary())
#print(n.set_salary)
#print(n.amount)