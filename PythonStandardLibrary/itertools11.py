from itertools import accumulate
from operator import mul

a = [3, 4, 6, 2, 1, 9, 1, 7, 5, 8]

print(list(accumulate(a, max)))

print(list(accumulate(a,min)))

print(list(accumulate(a)))

print(list(accumulate(a,mul)))