import math

a=int(input('please enter a numeber for a:'))
b=int(input('please enter a numeber for b:'))
c=int(input('please enter a numeber for c:'))

def quadratic(a,b,c):
    d=b**2-4*a*c
    if d < 0:
        return ('none')
    else:
        s=((-b+math.sqrt(d))/(2*a))
        x=((-b-math.sqrt(d))/(2*a))
        return s,x
print(quadratic(a,b,c))