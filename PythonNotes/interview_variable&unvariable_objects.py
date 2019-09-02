from copy import copy

a = 2
b = 2
c = a + 0
c += 0
print(id(a), id(b), id(c))
print()

print('string')
astr = 'dada'
bstr = 'dada'
cstr = 'dada' + ''
print(astr is bstr)
print(id(astr), id(bstr), id(cstr))
astr += 'a'
print(id(astr))

atuple = (1, 2, 3)
btuple = (1, 2, 3)
print(id(atuple), id(btuple), id((1, 2, 3)))
atuple += ()
print(id(atuple))

alist = [1, 2, 3]
blist = [1, 2, 3]
print(id(alist), id(blist), id([1, 2, 3]))
print(alist is blist)
clist = alist
print(id(alist), id(blist), id(clist))
clist.append(4)
print(id(alist), id(blist), id(clist))
print()

print('set')
aset = {1, 2, 3}
bset = {1, 2, 3}
cset = aset
aset.add(4)
print(id(aset), id(bset), id(cset))
print()

alist = [1, 2, 3, 4]
blist = alist[::]
clist = alist.copy()
print(id(alist), id(blist), id(clist))
blist.append(True)
print(id(alist), id(blist), id(clist))
