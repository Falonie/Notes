import re
import time
from functools import wraps
from multiprocessing import Process, Pool


def even_number(number):
    even_number_list = []
    for _ in range(1, number):
        if _ % 2 == 0:
            even_number_list.append(_)
    return even_number_list


def even_number2(number):
    even_number_list = []
    if number % 2 == 0:
        return number
    else:
        pass


def run_pool():
    t0 = time.time()
    even_numbers = []
    with Pool() as pool:
        # p=[_ for _ in pool.map(even_number2,list(range(1,100000001))) if _]
        p = pool.map(even_number2, list(range(1, 100000001)))
        print(p)
    print(time.time() - t0)


def even_number3(number):
    if number % 2 == 0:
        print(number)
        # return number
    else:
        pass


# even_number_list = []
# for i in range(1,101):
#     p=Process(target=even_number3,args=(i,))
#     even_number_list.append(p)
#     p.start()
#     p.join()

def filter_markup():
    s = "[lol]你好，帮我把这些markup清掉，[smile]。谢谢！"
    pattern = re.compile('\[\w*\]')
    print(pattern.sub('', s))


# filter_markup()

def log(text=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(f"<function name: {f.__name__}>")
            t0 = time.time()
            print("<function call begin>")
            result = f(*args, **kwargs)
            # print(result)
            print("<function call end>")
            print(f"[timecosts: {time.time()-t0}s]")
            return result
        return wrapper
    return decorator


@log()
def hello(name):
    print(f"hello, {name}")
    # return "hello, %s" % name


# hello("Falonie")
# print(hello("Falonie"))

def transform_string(s):
    sl = []
    for i in s[1::]:
        if i.isupper():
            sl.extend(["_", i])
        else:
            sl.extend(i)
    return s[0] + "".join(_ for _ in sl)


# print(transform_string('GetItem'))

def num_list():
    # global start
    start = 1
    end = 20
    for i in range(end - 4):
        # for i in range(end - start):
        nums = []
        print(f"Before: {start}")
        for _ in range(start, start + 5):
            if start == _:
                nums.extend([_, "*"])
            nums.append(_)
        print(nums)
        start += 1
        print(f"After: {start}")

# num_list()
