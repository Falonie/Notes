def pos(*num):
    s = 0
    for m in num:
        s = s + m ** 2
    return s


print(pos(1, 2, 4, 6))