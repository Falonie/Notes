s='awesome'
print(len(s),s.__len__())
b=s.encode('utf8')
print(b)
print(s.encode('utf8'))
print(s.encode('utf8').decode('utf8'))