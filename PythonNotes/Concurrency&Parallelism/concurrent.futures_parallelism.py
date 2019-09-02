import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


numbers = [(1963309, 2265973), (2030677, 3814172),
           (1551645, 2229620), (2039045, 2020802)]


def thread_sing():
    start = time.time()
    results = list(map(gcd, numbers))
    end = time.time() - start
    return end


def thread_pool():
    start = time.time()
    with ThreadPoolExecutor(max_workers=2) as executor:
        r = list(executor.map(gcd, numbers))
    end = time.time() - start
    return end


def process_pool():
    start = time.time()
    with ProcessPoolExecutor(max_workers=2) as executor:
        r = list(executor.map(gcd, numbers))
    # pool = ProcessPoolExecutor()
    # results = list(pool.map(gcd, numbers))
    end = time.time() - start
    return end


def multiprocessing_pool():
    start = time.time()
    with multiprocessing.Pool() as pool:
        p = pool.map(gcd, numbers)
    end = time.time() - start
    return p,end

# print(thread_sing())
print(thread_pool())
# print(process_pool())
# print(multiprocessing_pool())