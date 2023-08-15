"""
n = int(input())
def gen_fibonacci_numbers(n):
    fib = [1, 1]
    for i in range(n):
        fib.append(fib[i] + fib[i+1])
    return fib
print(gen_fibonacci_numbers(n))
"""
"""
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

for i in fib(5):
    print(i)

"""
"""
from time import perf_counter

class Timer:

    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        self.fn(*args, **kwargs)
        finish = perf_counter()
        res = finish - start
        print(res)
"""
"""
def rec_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return rec_fib(n-2) + rec_fib(n-1)

print('rec_fib')
timer = Timer(rec_fib)(40)

@Timer
def din_fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print('din_fib')
din_fib(40)
"""
"""
def pow_slow(a, n):
    if n == 0:
        return 1
    return pow_slow(a, n-1) * a

def pow_speed(a, n):
    if n == 0:
        return 1
    elif n%2 == 0:
        return pow_speed(a**2, n//2)
    return pow_speed(a, n - 1) * a


Timer(pow_slow)(2, 900)
Timer(pow_speed)(2,900)
"""
"""
from toolz import pipe
duble = lambda x: 2 * x
a = pipe(3, duble, str)
 # str(6)
print(a)
"""
"""
convert = lambda tup: tup[1].upper() + str(tup[0])
lazy = map(convert, enumerate(['a', 'b', 'c']))
print(tuple(lazy)) ('A0', 'B1', 'C2')
for el in lazy:
    print(el)
A0
B1
C2
"""
"""
import time
from itertools import islice

def timing(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time()
        print(f"{func.__name__} time: {finish-start}")
        return res
    return inner

@timing
def use_generator():
    return list(islice((time.sleep(x) for x in range(3)), 1))

@timing
def use_list():
    return list(islice([time.sleep(x) for x in range(3)], 1))

print(use_generator())
print(use_list())
"""