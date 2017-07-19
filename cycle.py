l = ('Bart','Lisa','Adam')
for name in l:
    print('Hello,%s!' % name)

n = 1
while n <= 100:
    if n > 10:
        break
    n += 1
    print(n)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum)