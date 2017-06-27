class Animal(object):
    def run(self):
        print('Animal is running.')
class Dog(Animal):
    def run(self):
        print('Dog is running.')
class Husky(Dog):
    def run(self):
        print('Husky is running.')

n=Dog()
m=Animal()
o=Husky()
print(n.run())
print(isinstance(n,Dog),isinstance(n,Animal))
print(isinstance(o,Animal),isinstance(o,Dog))
print(isinstance(m,Animal),isinstance(m,Dog))