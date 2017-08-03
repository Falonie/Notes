import pickle

d = dict(name='Caseny', salary=15000)
# d={'name':'Caseny','salary':15000}
d['salary'] = 18000

# pickling
print(pickle.dumps(d))

f = open('pickle.txt', 'wb')
pickle.dump(d, f)
f.close()

# unpickling
f = open('pickle.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)