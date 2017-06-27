L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(list(sorted(L,key=lambda L:L[0])))
print(list(sorted(L,key=lambda L:L[1])))
print(list(sorted(L,key=lambda L:L[1],reverse=True)))

def fuc(t):
    return t[0].lower()
def fuc_score(t):
    return t[1]
print(sorted(L,key=fuc))
print(sorted(L,key=fuc_score))
print(sorted(L,key=fuc,reverse=True))