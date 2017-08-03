def fuc(a, b, f):
    # return f(a) * f(b)
    # print(fuc(-4, -6, abs))
    return f(a) / f(b)

print(fuc(-5, -2, abs))