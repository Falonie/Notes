import math

def quadratic(a,b,c):
    d=b**2-4*a*c
    if d < 0:
        print('none')
    else:
        x1=((-b+math.sqrt(d))/(2*a))
        x1=((-b-math.sqrt(d))/(2*a))
print(quadratic(5,4,3))
print(quadratic(5,2,7))