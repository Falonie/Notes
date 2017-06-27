def _odd_iter(n):
    n = 1
    while True:
        n = n + 2
        yield n
print(_odd_iter(n))