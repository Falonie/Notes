def s(n):
    if n == 1:
        return 1
    return n * s(n - 1)
print(s(6))

l = ['A','B','C']
for x in l:
    print('hello:',x)

l = []
n = 0
while n <= 100:
    l.append(n)
    n = n + 1
print(l)