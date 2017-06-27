weight=float(input('please enter weight: '))
height=float(input('please enter height: '))
bmi=weight/(height**2)
if bmi < 18.5:
    print('too light')
elif 18.5 <= bmi <= 25:
    print('normal')
elif 25 <= bmi <= 28:
    print('a bit fat')	
elif 28 <= bmi <= 32:
    print('fat')
elif bmi > 32:
    print('too fat')