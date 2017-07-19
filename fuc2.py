def my_str(x):
    if not isinstance(x(str)):
        raise TypeError('error')
    else:
        return x
print(my_str('323'))
print(my_str(31))

def a_abs(a):
    return a if a >= 0 else -a
    # if a>=0:
    #     return a
    # else:
    #     return -a
print(a_abs(-99))

def m_abs(s):
    if not isinstance(s, (int, float)):
        raise TypeError('error,please enter again')
    elif s >= 0:
        return s
    else:
        return -s

