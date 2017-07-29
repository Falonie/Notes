def normalize(name):
    return name[0:1].upper() + name[1::].lower()
l1=['adam','LISA','barT']
print(list(map(normalize,l1)))

def normalize(a):
    return a.capitalize()
l2=['adam','LISA','barT']
print(list(map(normalize,l2)))

def normalize(b):
    return b.title()
l3=['adam','LISA','barT']
print(list(map(normalize,l3)))
