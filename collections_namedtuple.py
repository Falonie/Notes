from collections import namedtuple

#bob=('Bob',30,'male')
Person=namedtuple('person','name age')
bob=Person(name='bob',age=30)
print(bob)

jane=Person(name='Jane',age=29)
print(jane.age)

for p in [bob,jane]:
    print('{} is {} yeas old.'.format(*p))

Point=namedtuple('point','x y')
p=Point(1,y=2)
print(p.x,p.y)