# def print_():
#     print("It's my first function")
# print_()

# def input_():
#     name, surname = tuple(map(str, input().split()))
#     print(f"Уважаемый, {name} {surname}! "
#           f"Вы верно выполнили это задание")
# input_()

# name, surname = tuple(map(str, input().split()))
# print(name, surname) Андрей Овешков

# def weight_x(x):
#     print(f"Предмет имеет вес: {x} кг.")
# weight_x(float(input()))

# def math_list(x: list) -> str:
#     v_min, v_max, v_sum = min(x), max(x), sum(x)
#     print(f"Min = {v_min},max = {v_max}, sum = {v_sum}")
# math_list(list(map(int, input().split())))

# def perimetr_rectangle(width: int, height: int):
#     res_perimetr = 2 * (width + height)
#     print(f"Периметр прямоугольника, равен {res_perimetr}")
# perimetr_rectangle(*tuple(map(int, input().split())))
# Периметр прямоугольника, равен 10


# from string import punctuation


# alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# punctuation = "!\"#$%&\'()*+,-/:;<=>?[\]^`{|}~"

# def correct_mail(email: str):
#     good_mail = True
#     if "@" not in email or "." not in email:
#         good_mail = False
#     for index, el in enumerate(email):
#         if el in punctuation:
#             good_mail = False
#         if el.isalpha():
#             if el not in alpha:
#                 good_mail = False
#         if el == " ":
#             good_mail = False
#         if email[0].isdigit() or email[-1].isdigit():
#             good_mail = False
#     if email.count("@") >= 2:
#         good_mail = False
#     if email.index("@") > email.index("."):
#         good_mail = False
#     print("ДА" if good_mail else "НЕТ")
# correct_mail(input())

# def get_max(x: int, z: int):
#     max_ = x if x > z else z
#     return max_
#
# print(get_max(3, get_max(5, get_max(6, 9)))) 9

# def get_max_2(a: int, b: int):
#     max_2 = a if a > b else b
#     return max_2
#
#
# def get_max_3(a, b, c):
#     max_3 = get_max_2(a, get_max_2(b, c))
#     return max_3
#
#
# x, y, z = 1, 2, 3
#
# print(get_max_3(x, y, z))


# def square_num(x: float):
#     return x**2
# print(square_num(float(input())))

# def is_triangle(x: int, y: int, z: int):
#     return True if x+y > z or y+z > x or x+z > y else False
# print(is_triangle(3,4,5))

# def is_large(line: str) -> bool:
#     return True if len(line) > 3 else False


# def chet_num(x: int) -> bool:
#     return True if x%2 == 0 else False
#
# x = None
# while x != 1:
#     x = int(input())
#     if chet_num(x):
#         print(x)

# def odd_num(x: int) -> bool:
#     return True if x%2 != 0 else False
#
# array = list(map(int, input().split()))
# lst = [num for num in array if odd_num(num)]
# print(*lst)


# tp = input()
# if tp == "RECT":
#     def get_sq(x: int, y: int) -> int:
#         return x*y
# else:
#     def get_sq(x: int) -> int:
#         return x*x

#
# def lenght_line(line: str) -> bool:
#     return True if len(line) >= 6 else False
#
# array = list(map(str, input().split()))
# lst = [line for line in array if lenght_line(line)]
# print(*lst)


# def tuple_line(line: str) -> tuple:
#     return line, len(line)
#
#
# array = list(map(str, input().split()))
#
# d ={tuple_line(elem)[0]: tuple_line(elem)[1] for elem in array}
# a = sorted(d, key=lambda x: d[x])
# print(*a)

# num = list(map(int, input().split()))
# def work_min_max(x: int, y: int) -> int:
#     return x * y

# print(work_min_max(min(num), max(num)))
#
# import time
# def get_nod(a: int, b: int) -> int:
#     """
#     Вычеслется НОД для натуральных чисел a и b
#     по быстрому алгоритму Евклида
#     :param a: первое натуральное число
#     :param b: второе натуральное число
#     :return: НОД
#     """
#     if a < b:
#         a, b = b, a
#     while b != 0:
#         a, b = b, a%b
#     return a
#
# def test_nod(func):
#     print("Testcase #1: ", end='')
#     a = 28
#     b = 35
#     res = func(a,b)
#     print("OK" if res == 7 else "Fail")
#
#     print("Testcase #2: ", end='')
#     a = 100
#     b = 1
#     res = func(a,b)
#     print("OK" if res == 1 else "Fail")
#
#     print("Testcase #3: ", end='')
#     a = 2
#     b = 100000000
#     start_time = time.time()
#     res = func(a, b)
#     end_time = time.time()
#     data_time = start_time - end_time
#     print("OK" if res == 2 and data_time < 1 else "Fail")
#
# test_nod(get_nod)


# def get_nod(a: int, b: int) -> int:
#     if a < b:
#         a, b = b, a
#     while b != 0:
#         a, b = b, a % b
#     return a
# print(get_nod(15, 121050))

#
# def get_line(a: str, b: str, reg=False, trim=True) -> bool:
#     if reg:
#         a = a.lower()
#         b = b.lower()
#     if trim:
#         a = a.strip()
#         b = b.strip()
#
#     return a == b
#
# print(get_line("python", "PYTHON", True))
#
# def add_value(value, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(value)
#     return lst
#
# l = add_value(1)
# l = add_value(2,l)
# l = add_value(3, l)
# print(l) # [1, 2, 3]


# def get_rect_value(x: int, y: int, type=0):
#     if type == 0:
#         return x + y
#     return x * y

# def check_password(password: str, chars="$%!?@#") -> str:
#     intersection = set(password) & set(chars)
#     return True if len(intersection) > 0 and len(password) >= 8 else False
#
# print(check_password("12382343432!"))

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# def get_translates(line: str, sep='-') -> str:
#     for elem in line:
#         if elem == " ":
#             line = line.replace(" ", sep)
#         if elem in t:
#             line = line.replace(elem, t[elem])
#
#     return line
#
# line_input = input().lower()
# print(get_translates(line_input))
# print(get_translates(line_input, sep="+"))

# def get_tag(line: str, tag="h1") -> str:
#     return f"<{tag}>{line}</{tag}>"
# input_line = input()
# print(get_tag(input_line))
# print(get_tag(input_line, "div"))

# def get_tag(line: str, tag="h1", up=True) -> str:
#     if up:
#         tag = tag.upper()
#     return f"<{tag}>{line}</{tag}>"
# input_line = input()
# print(get_tag(input_line, "div"))
# print(get_tag(input_line, "div", False))

# def os_path(*args):
#     # Произвольное число аргументов
#     path = "\\".join(args)
#     return path
#
# p = os_path("F:\\", "stepik",
#             "Python", "Functions",
#             )
# print(p) F:\\stepik\Python\Functions


#
# def os_path(*args, sep="\\", **kwargs):
#     print(kwargs) # Произвольное число именованных аргументов
#     {'trim': True}
#     path = "\\".join(args)
#     return path
#
# p = os_path("F:\\", "stepik",
#             "Python", "Functions",
#             sep='/', trim=True)
# print(p)


# def os_path(disk, *args, sep='\\', **kwargs):
#     args = (disk, ) + args
#     if "trim" in kwargs and kwargs["trim"]:
#         args = [x.strip() for x in args]
#     path = sep.join(args)
#     return path
#
# p = os_path("F:", "stepik",
#             "Python", "Functions",
#             sep='/', trim=True)
# print(p)

# def fool(line: str, x: int):  # Фактические параметры
#     pass
# def fool_(line="Hello", x=4):  # Формальные параметры
#     pass
# def fool__(*args):  # Произвольное число параметров
#     pass
# def fool___(**kwargs):  # Произвольное число именованных параметров
#     pass
# fool("Hello", 5)  # Позиционные аргументы
# fool(x=5, line="Hello")  # Именованные аргументы

# def get_even(*args: int) -> list:
#     array = [n for n in args if n%2 == 0]
#     return array
#
# print(get_even(1,2,3))


# def get_biggest_city(*args: str) -> str:
#     array = [elem for elem in args]
#     n = len(array)
#     for elem in range(1,n):
#         for i in range(0, n-elem):
#             if len(array[i]) > len(array[i+1]):
#                 array[i],array[i+1] = array[i+1],array[i]
#     return array[-1]
# print(get_biggest_city("москва", "питер", "воронеж", "самара"))

# def get_biggest_city(*args: str) -> str:
#     big_city = ''
#     for city in args:
#         big_city = city if len(city) > len(big_city) else big_city
#     return big_city
# print(get_biggest_city("москва", "питер", "воронеж", "самара"))

# import sys
# s = sys.stdin.readlines()
# input_matrix = [list(map(int, x.strip().split())) for x in s]
# def is_isolate(matrix: list):
#     n = len(matrix)
#     for row in range(n-1):
#         for col in range(n-1):
#             if matrix[row][col] + matrix[row][col+1] + \
#                     matrix[row+1][col] + matrix[row+1][col+1] > 1:
#                 return False
#     return True
#
# print(is_isolate(input_matrix))
# print(input_matrix)


# def get_data_fig(*args, **kwargs):
#     sum = 0
#     for i in args:
#         sum += i
#     perimetr = (sum,)
#     if "type" in kwargs:
#         perimetr += (kwargs["type"], )
#     if "color" in kwargs:
#         perimetr += (kwargs["color"], )
#     if "closed" in kwargs:
#         perimetr += (kwargs["closed"], )
#     if "width" in kwargs:
#         perimetr += (kwargs["width"], )
#     return perimetr
# print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))

#
# def str_min(line_1: str, line_2: str):
#     if line_1 < line_2:
#         return line_1
#     return line_2
#
# def str_min3(line_1: str, line_2: str, line_3: str):
#     if line_1 < str_min(line_2, line_3):
#         return line_1
#     return str_min(line_2, line_3)
#
# def str_min4(line_1: str, line_2: str, line_3: str, line_4: str):
#     if line_1 < str_min3(line_2, line_3, line_4):
#         return line_1
#     return str_min3(line_2, line_3, line_4)
#
# print(str_min4("asdc","asdc","asd","asdf"))


# def get_nod(a: int, b: int) -> int:
#     if a < b:
#         a, b = b, a
#     while b != 0:
#         a, b = b, a%b
#     return a
#
# print(get_nod(10,4))

"""
def get_nod(a: int, b: int):
    return a if b == 0 else get_nod(b, a%b)
print(get_nod(10,4))
"""
"""import re"""

"""def calculate(x: float, y: float, operation: str="a") -> None:

    def addition():
        print(x + y)

    def subtraction():
        print(x - y)

    def division():
        print("На ноль делить нельзя!" if y == 0 else x / y)

    def multiplication():
        print(x * y)

    match operation:
        case "a":
            addition()
        case "s":
            subtraction()
        case "d":
            division()
        case "m":
            multiplication()
        case _:
            print("Ошибка. Данной операции не существует")

    return operation

calculate(10, 2, "w")
"""
#  Замыкания
"""
def main_func(name):
    def inner_func():
        print("Hello", name)

    return inner_func

b = main_func("ivan")
v = main_func("andrey")
print(b())
Hello ivan
None
print(v())
Hello andrey
None
"""
"""
def adder(value):
    def inner(a):
        return value + a
    return inner

b = adder(2)
print(b(2))  # 4
"""
"""
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

a = counter()
print(a())
print(a())  # 1, 2
"""
"""
def create_accumulator():
    count = 0
    def summator(n):
        nonlocal count
        count += n
        return count
    return summator
a = create_accumulator()
print(a(1))  # 1
print(a(5))  # 6
print(a(2))  # 8
"""
"""
def create_accumulator(n=0):
    def summator(x):
        nonlocal n
        n += x
        return n
    return summator
a = create_accumulator(100)
print(a(1))  # 101
"""
"""
def multiply(n):
    def result(x):
        nonlocal n
        return n*x
    return result
a = multiply(3)
print(a(2))  # 6
"""
"""
def average_numbers():
    numbers = []
    def inner(num):
        numbers.append(num)
        print(numbers)
        return sum(numbers) / len(numbers)
    return inner

b = average_numbers()
print(b(10))  # 10.0 [10]
print(b(5))  # 7.5 [10, 5]
"""
"""
def average_num():
    count = 0
    summa = 0
    def inner(number):
        nonlocal count
        nonlocal summa
        summa += number
        count += 1
        return summa / count
    return inner

a = average_num()
print(a(10))  # 10
print(a(20))  # 15
 """
"""
from time import perf_counter
def timer():
    start = perf_counter()

    def inner():

        return perf_counter() - start

    return inner

a = timer()
print(a())  # 2.382999809924513e-06
print(a())  # 4.8377999519289006e-05
print(a())  # 5.596800019702641e-05
"""
"""
def add(a,b):
    return a+b

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функция {func.__name__} вызывалась {count} раз")
        return func(*args, **kwargs)
    return inner

a = counter(add)
print(a(1,2))
Функция add вызывалась 1 раз
3
"""
"""
def create_dict():
    count = 0
    dict_ = {}

    def inner(*args):
        nonlocal count, dict_
        count += 1
        dict_.setdefault(count, *args)
        return dict_
    return inner

a = create_dict()
print(a(100))  # {1: 100}
print(a("ad"))  # {1: 100, 2: 'ad'}
print(a("asd"))  # {1: 100, 2: 'ad', 3: 'asd'}
"""
"""
def create_counter():
    count = 0

    def increment(value: int = 1):
        nonlocal count
        count += value
        return count

    def decrement(value: int = 1):
        nonlocal count
        count -= value
        return count

    return increment, decrement

inc_1, dec_1 = create_counter()
print(inc_1(5))  # 5
print(inc_1(5))  # 10
print(dec_1(2))  # 8
print(dec_1(2))  # 6
"""
"""
def decorator(func):

    def inner():
        print("start decorator...")
        func()
        print("finish decorator...")

    return inner


def say():
    print("hello world")

a = decorator(say)
a()
# start decorator...
# hello world
# finish decorator...
"""

# Декоратор
"""
def decorator(func):

    def inner(*args, **kwargs):
        print("start decorator...")
        func(*args, **kwargs)
        print("finish decorator...")

    return inner


def say(name, age):
    print("hello", name, age)

say = decorator(say)
say("ivan", 20)

# start decorator...
# hello ivan 20
# finish decorator...
"""
"""
def header(func):

    def inner(*args, **kwargs):
        print("<h1>")
        func(*args, **kwargs)
        print("</h1>")

    return inner


def table(func):

    def inner(*args, **kwargs):
        print("<table>")
        func(*args, **kwargs)
        print("</table>")

    return inner

@header  # say = header(say)
@table  # say = table(say)
# say = table(header(say))
def say(name, age):
    print("hello", name, age)

say('ivan', 20)
# <h1>
# <table>
# hello ivan 20
# </table>
# </h1>
"""
"""
def text_decor(func):

    def inner(*args):
        print("Hello")
        func(*args)
        print("Goodbye")
    return inner

@text_decor
def simple_func(*args):
    print(*args)

simple_func("asa")
# Hello
# asa
# Goodbye
"""
"""
def repeater(func):

    def inner(*args):
        func(*args)
        func(*args)
    return inner
@repeater
def multiply(*args):
    print(*args)
"""

# from functools import wraps
# @wraps(func) сохраняет имя и док строку в декорируемой функции
"""
from functools import wraps

def add_args(func):

    @wraps(func)
    def inner(*args):
        return func("begin", *args, "end")
    return inner


@add_args
def concatenate(*args):
    #Возвращает конкатенацию переданных строк
    return ', '.join(args)
@add_args
def find_max_word(*args):

    #Возвращает слово максимальной длины

    return max(args, key=len)

print(find_max_word('my'))  # begin
print(concatenate('hello', 'world'))  # begin, hello, world, end"""
"""
from string import Template

values = {'one': 'Привет', 'copter': 'Квадракоптер'}

t = Template("
Ну что, мои хорошие, всем $one
Это шаблонная строка
В нее можно вставлять значения по ключам
Хочу сюда вставлю слово $copter, хочу сюда $copter
")

print(t.substitute(values))"""
# Ну что, мои хорошие, всем Привет
# Это шаблонная строка
# В нее можно вставлять значения по ключам
# Хочу сюда вставлю слово Квадрокоптер, хочу сюда Квадрокоптер

"""
def text_decor(func):
    def inner(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)
        print("Goodbye!")
    return inner
@text_decor
def strings(*args):
    print(*args)

strings("World")
# Hello
# World
# Goodbye!
"""

# функции генераторы
# замораживает функцию, экономя при этом память
"""
def gen_f():
    for i in [1, 2, 3, 4]:
        yield i
res = gen_f()
print(next(res))  # 1
print(next(res))  # 2
print(next(res))  # 3
"""
"""
def gen_fact(n):
    pr = 1
    for i in range(1, n+1):
        pr *= i
        yield pr

for i in gen_fact(10):
    print(i, end=' ')
# 1 2 6 24 120 720 5040 40320 362880 3628800
# не используется память
"""
"""
n = int(input())
def gen_squares(n):
    for i in range(1, n+1):
        yield i**2
for i in gen_squares(n):
    print(i)
# 1
# 4
# 9
"""
"""
n = int(input())
def gen_fibonacci_numbers(n):
    fib_1, fib_2 = 1, 1
    for i in range(n):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1+fib_2
for i in gen_fibonacci_numbers(n):
    print(i)
# 1
# 1
# 2
# 3
# 5
"""
"""
def my_name(name):
    def bye_name():
        print(f"Bye, {name}")
    return bye_name

a = my_name("andrey")
a()  # Bye, andrey
b = my_name("alex")
b()  # Bye, alex
"""
"""
def func_show(func):
    def inner(*args, **kwargs):
        print(f"Площадь прямоугольника: {func(*args, **kwargs)}")
    return inner

@func_show
def get_sq(width: int, height: int):
    return width * height

get_sq(8,11)
# Площадь прямоугольника: 88
"""
"""
def show_menu(func):
    def inner(*args, **kwargs):
        count = 0
        for elem in func(*args, **kwargs):
            count += 1
            print(f"{count}. {elem}")
    return inner

s = input()
@show_menu
def get_menu(s: str):
    s = s.split(" ")
    return s

get_menu(s)
# asad asd asd
# 1. asad
# 2. asd
# 3. asd
"""
"""
def dec(func):
    def inner(*args,**kwargs):
        return sorted(func(*args, **kwargs))
    return inner

s = input()
@dec
def get_list(s: str):
    return [int(x) for x in s.split(" ")]

print(get_list(s))

# 1 21 53 12
# [1, 12, 21, 53]
"""
"""
line_1, line_2 = input(), input()

def dec_func(func):
    def inner(*args, **kwargs):
        line_1, line_2 = func(*args, **kwargs)
        d = {line_1[elem]: line_2[elem] for elem in range(len(line_1))}
        return sorted(d.items())
    return inner

@dec_func
def get_list(line_1: str, line_2: str):
    list_1 = line_1.split()
    list_2 = line_2.split()
    return list_1, list_2

print(*get_list(line_1, line_2))
"""
"""
from functools import wraps
s = input()
def dec_func(start=0):
    def dec_sum(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return start + func(*args, **kwargs)
        return inner
    return dec_sum

@dec_func(start=5)
def sum_func(line: str):
    res = [int(x) for x in line.split()]
    return sum(res)

print(sum_func(s))
"""
"""
s = input()
def dec_func(tag="div"):
    def get_dec(func):
        def inner(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return inner
    return get_dec

@dec_func(tag="div")
def get_lower(line: str):
    return line.lower()

print(get_lower(s))
"""
"""
import re

s = input().lower()
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def dec_func(chars=r"[?!]"):
    def get_transl(func):
        def inner(*args, **kwargs):
            line = func(*args, **kwargs)
            line = re.sub(chars, "-", line)
            line = re.sub(r"[-]+", "-", line)
            return line
        return inner
    return get_transl

@dec_func(chars="[?!:;,. ]")
def transl(line: str):
    for index, value in enumerate(line):
        if value.isascii():
            continue
        else:
            if value.isalpha():
                line = line.replace(value, t[value])
    return line

print(transl(s))
"""
"""
from functools import wraps

def dec_func(func):
    @wraps(func)
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        return inner


def sum_func(line: str):
    Функция для формирования списка целых значений
    res = [int(x) for x in line.split()]
    return sum(res)
"""

"""
from string import ascii_lowercase

gen = (x+i for x in ascii_lowercase for i in ascii_lowercase)
for i in range(10):
    print(next(gen),end=' ')
"""
"""
cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (x%len(cities) for x in range(1000000))
for i in range(20):
    print(cities[next(gen)], end=' ')
"""
"""
def get_sum(n):
    s = 0
    for n in range(1, n+1):
        s += n
        yield s
"""
"""
def trib(n):
    a = 1
    b = 1
    c = 1
    for i in range(n):
        if i < 3:
            yield 1
        else:
            yield a + b + c
            a, b, c = b, c, (a+b+c)

n = int(input())
for i in trib(n):
    print(i, end=' ')
"""
"""
def fib(n):
    a = 1
    b = 1
    for i in range(n):
        if i < 2:
            yield 1
        else:
            yield a + b
            a, b = b, a + b

n = int(input())
for i in fib(n):
    print(i, end=' ')
"""
"""
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr *= i
        yield pr
n = int(input())
for i in fact(n):
    print(i, end=' ')
"""
"""
from string import ascii_lowercase, ascii_uppercase
import random
random.seed(1)

def password(n):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    word = ''
    while True:
        for i in range(n):
            indx = random.randint(0, len(chars)-1)
            word += chars[indx]
        yield word

n = int(input())

for i in range(5):
    print(next(password(n)))
"""
"""
from string import ascii_uppercase, ascii_lowercase
import random
random.seed(1)
def mail(n):

    word = ''
    chars = ascii_lowercase + ascii_uppercase
    while True:
        for i in range(n):
            indx = random.randint(0, len(chars)-1)
            word += chars[indx]
        yield f"{word}@mail.ru"
"""
"""
line = map(float, input().split())
for i in range(3):
    print(next(line), end=' ')
"""
"""
line = list(map(int, input().split()))
lst = list(map(abs, line))
print(*lst)
"""
"""
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst2D = [list(map(int,x.split())) for x in lst_in]
"""
"""
lst = filter(lambda x: len(x) > 5, map(str, input().split()))
for i in range(3):
    print(next(lst), end=' ')
"""
"""
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

f = tuple(filter(lambda x: int(x[1]) > 500, (x.split('=') for x in tuple(lst_in))))
for i in f:
    print(i[0], end=' ')
"""
"""
lst_1 = list(map(int, input().split()))
lst_2 = list(map(int, input().split()))

g = (i*j for i, j in zip(lst_1, lst_2))
[print(next(g), end=' ') for i in range(3)]
"""
"""
a, b = ([*map(int, input().split())] for _ in ',,')
print(a, b)
[123] [123]
"""
"""
x = [1, 2]
y = [4, 5, 6]
zipped = zip(x, y, strict=True)
result = list(zipped)
print(result)
"""
"""
keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'One hundred']
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

dict_ = {keys: values for keys, values in zip(keys, values)}
print(dict_)
dict_ = {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50,
         'Sixty': 60, 'Seventy': 70, 'Eighty': 80, 'Ninety': 90, 'One hundred': 100}
"""
"""
employees = [
    'Pankratiy', 'Innokentiy', 'Anfisa', 'Yaroslava', 'Veniamin',
    'Leonti', 'Daniil', 'Mishka', 'Lidochka',
    'Terenti', 'Vladik', 'Svetka', 'Maks', 'Yura', 'Sergei'
]

identifiers = [77, 48, 88, 85, 76, 81, 62, 43, 5, 56, 17, 20, 37, 32, 96]


employees_data = {name: value for name, value in zip(sorted(identifiers), sorted(employees))}
print(employees_data)
"""
"""
a = [1,2,3]
b = [1,2,3]
c = [i+j for i, j in zip(a,b)]
print(c) #[2, 4, 6]

"""