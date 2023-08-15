"""import re
from my_module import search as s"""
"""
def teg_name(name: str):
    with open(s.search_file(name), "r") as file:
        reg = r"<[/]?([a-zA-Z\d]+)[\s\w\d\W]*?[>]+"
        text = file.read()
        match = re.findall(reg, text)
        print(match)

teg_name("html_file.html")
"""
"""
def token(name: str):
    with open(s.search_file(name), "r") as file:
        text = file.read()
        reg = r"([\d]+):([a-zA-Z\d]+):([a-z\d]+)"
        match = re.findall(reg, text)
        print(match)

token("txt_file.txt")
"""
"""
def remove_excess(name: str):
    with open(s.search_file(name), "r") as file:
        reg = r"[^\d]+([+:=*/-])[^\d]+"
        text = file.read()
        match = re.split(reg, text)
        print(match)
remove_excess("txt_file.txt")
"""
"""
def split_parameter(name: str):
    with open(s.search_file(name), "r") as file:
        text = file.read()
        reg = r"([?&])"
        match = re.split(reg, text)
        print(match)
split_parameter("txt_file.txt")
"""
"""
from functools import wraps
def validate_args(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if len(args) < 2:
            return "Not enough arguments"
        elif len(args) > 2:
            return "Too many arguments"
        elif not all(isinstance(arg, int) for arg in args):
            return "Wrong types"
        else:
            return func(*args, **kwargs)
    return inner

@ validate_args
def add_numbers(x,y):
    return x+y

print(add_numbers(4,5))
"""
"""
from functools import wraps
def memoize(func):
    date_fib = {}
    @wraps(func)
    def inner(*args):
        if args in date_fib:
            return date_fib[args]
        else:
            return date_fib.setdefault(args, func(*args))
    return inner

@memoize
def fibonacci(n):
    if n < 2:
        return 2
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))
"""
"""
def memoize(func):
    date_fib = {}
    def inner(*args):
        nonlocal date_fib
        return date_fib.get(*args) or date_fib.setdefault(args, func(*args))
    return inner
@memoize
def fibonacci(n):
    if n < 2:
        return 2
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))
"""
"""
from string import punctuation
def longest_word_in_file(name_file: str):
    with open(s.search_file(name_file), "r")as file:
        text = file.read()
        reg = fr"[{punctuation}\n\s]"
        match = re.split(reg, text)
        match = sorted(match, key=lambda x: -len(x))
        return match[0]

print(longest_word_in_file("txt_file.txt"))
"""
"""
with open(s.search_file("numbers.txt")) as file:
    text = file.read()
    reg_1 = r"[\d]{3}"
    reg_2 = r"[\d]{2}"
    # match = re.findall(reg_1, text)
    # print(match)
    # print(len(match))
    for elem in text:
        if len(elem) == 2:
            print(elem)
"""
"""
def find_lines_len_more_6(file_name: str) -> int:
    with open(s.search_file(file_name), "r", encoding="utf-8") as file:
        text = file.readlines()
        count = 0
        for elem in text:
            if len(elem.strip()) > 6:
                count += 1
    return count
print(find_lines_len_more_6("txt_file.txt"))
"""
"""
with open(s.search_file("txt_file.txt")) as file:
    text = file.read().lower()
    reg = r"[A-Za-z]+"
    match_ = re.findall(reg, text)
    unique_array = []
    n = len(match_)
    for elem_1 in range(0, n-1):
        for elem_2 in range(elem_1+1, n):
            if match_[elem_1] == match_[elem_2]:
                match_[elem_1] = None
                # match_[elem_2] = None
            else:
                continue
    print(match_)
    count = 0
    for i in match_:
        if isinstance(i, str):
            count += 1
    print(count)
"""
"""
with open(s.search_file("txt_file.txt"), "r") as file:
    text = file.read().lower()
    reg = r"[a-zA-Z]+"
    match = re.findall(reg, text)
    set_ = set()
    for elem in match:
        set_.add(elem)
    print(len(set_))
"""
"""
with open(s.search_file("txt_file.txt")) as file:
    words = {}
    text = file.read().upper()
    reg = r"[a-zA-Z]+"
    match = re.findall(reg, text)
    for elem in match:
        words[elem] = words.get(elem, 0)+1
    print(words)
"""
"""
with open(s.search_file("txt_file.txt"), "r") as file:
    text = file.readlines()
    set_ = set()
    for elem in text:
        set_.add(elem.upper().strip())
    array = sorted([i for i in set_ if i[-2:] == "ЕЯ"], key=lambda x: (len(x), x))
    for elem in array:
        print(elem)
"""
































