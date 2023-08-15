"""def rec(x):
    if x < 4:
        print(x)
        rec(x+1)
        print(x)
rec(1)
1 стек вызовов
2
3
3
2
1
"""
# import os

"""
def fact(n: int):
    if n == 1:
        return 1
    return fact(n-1) * n
fact(4) = fact(3) * 4 - 6*4 = 24
        ↓               ↑
fact(3) = fact(2) * 3 - 2*3 = 6
        ↓               ↑
fact(2) = fact(1) * 2 - 1*2 = 2
        ↓               ↑
    n == 1 return 1

print(fact(4)) 24
"""

"""Fibonacci = 0,1,1,2,3,5,8
def fib(n: int):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(5)) 3"""

"""def palindrom(s: str):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])
print(palindrom("asa"))"""

"""def print_from(n: int) -> None:
    if n == 0:
        return 1
    print(n)
    return print_from(n-1)

print_from(2)"""

"""def print_from(n: int) -> None:
    if n > 0:
        print(n)
        print_from(n-1)
print_from(4)"""

"""def print_to(n: int):
    if n > 0:
        print(n)
        print_to(n-1)
        print(n)

print_to(5)"""

"""n = int(input())
mas = list(map(int, input().split()))
def get_reverse(n):
    if n > 0:
        print(mas[n-1], end=' ')
        get_reverse(n-1)
get_reverse(n)"""

"""def double_fact(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return double_fact(n-2) * n
print(double_fact(4))"""

"""def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(int(input())))"""

"""def tri_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return tri_fib(n-1) + tri_fib(n-2) + tri_fib(n-3)
print(tri_fib(int(input())))"""

"""def get_combin(n, k):
    if k == 0:
        return 1
    if k == n:
        return 1
    return get_combin(n-1, k) + get_combin(n-1, k-1)
print(get_combin(6,3))"""

"""def ackermann(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m-1,1)
    if m > 0 and n > 0:
        return ackermann(m-1, ackermann(m,n-1))

print(ackermann(3,2))"""

"""
j = 0
def list_sum(mas: list, n=1):
    mas[0] = mas[0] + mas[n]
    global j
    j += 1
    if j < len(mas)-1:
        list_sum(mas, n+1)
    return mas[0]

print(list_sum(list(map(int, input().split()))))
"""

"""
def sum_list(mas: list):
    if len(mas) == 1:
        return mas[0]
    return mas[0] + sum_list(mas[1:])
print(sum_list(list(map(int, input().split()))))"""

"""def flatten(mas: list) -> list:
    if not mas:
        return []
    if isinstance(mas[0], list):
        return flatten(mas[0] + flatten(mas[1:]))
    return mas[:1] + flatten(mas[1:])

print(flatten([1, [2, 3, [4]], 5]))
"""

"""
def search_space(text: str) -> int:
    if len(text) == 0:
        return 0
    count = 0
    if text[0] == " ":
        count = 1
    return count + search_space(text[1:])


def test_search():
    print("Test_case_1: ", end='')
    test_text = search_space("Hello world and Python")
    result = 3
    print("Ok" if test_text == result else "Fail")

test_search()
"""

"""
def get_rec_N(N):
    if N == 0:
        return 1
    get_rec_N(N-1)
    print(N)
get_rec_N(8)
"""

"""
def get_rec_sum(mas: list):
    if len(mas) == 1:
        return mas[0]
    return mas[0] + get_rec_sum(mas[1:])
print(get_rec_sum(list(map(int, input().split()))))
"""

"""
N = int(input())
def fib_rec(N, f=[1,1]):
    if len(f) < N:
        f.append(f[-1] + f[-2])
        return fib_rec(N, f)
    return f

print(fib_rec(N))"""

"""
def fact_rec(n):
    if n == 1:
        return 1
    return fact_rec(n-1) * n
print(fact_rec(4))"""

"""
d = [1, 2, [True, False],
     ["Москва", "Уфа", [100, 101],
      ['True', [-2, -1]]], 7.89]
def get_line_list(d, a=[]):
    if not d:
        return []
    if isinstance(d[0], list):
        return get_line_list(d[0] + get_line_list(d[1:]))
    return d[:1] + get_line_list(d[1:])
print(get_line_list(d))"""

"""
def get_space(text: str):
    if len(text) == 0:
        return 0
    count = 0
    if text[0] == " ":
        count = 1
    return count + get_space(text[1:])

print(get_space("Hello word"))"""

"""
d = [1,2, [True, False],
     ["Москва", "Уфа", [100, 101],
      ['True', [-2, -1]]], 7.89]

def get_line_list(d,a=[]):
    if len(d) > 0:
        if isinstance(d[0], list):
            get_line_list(d[0])
        else:
            a.append(d[0])
        get_line_list(d[1:], a)
    return a
print(get_line_list(d))"""

"""
def get_path(n:int):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return get_path(n-1) + get_path(n-2)
print(get_path(7))"""

"""
def merge_two_list(array_1: list, array_2: list) -> list:
Сортировка слиянием => N*log2N
    sort_array = []
    ind_1 = ind_2 = 0
    n = len(array_1)
    m = len(array_2)
    while ind_1 < n and ind_2 < m:
        if array_1[ind_1] < array_2[ind_2]:
            sort_array.append(array_1[ind_1])
            ind_1 += 1
        else:
            sort_array.append(array_2[ind_2])
            ind_2 += 1
    sort_array += array_1[ind_1:] + array_2[ind_2:]
    return sort_array

def merge_sort(mas: list) -> list:
    if len(mas) == 1:
        return mas
    middle = len(mas)//2
    left = merge_sort(mas[:middle])
    rigth = merge_sort(mas[middle:])
    return merge_two_list(left, rigth)
"""

"""
def quick_sort(array: list) -> list:
Быстрая сортировка Хоара => N*log2N
    if len(array) <= 1:
        return array
    elem = array[0]
    left_mas = [n for n in array if n < elem]
    center_mas = [n for n in array if n == elem]
    right_mas = [n for n in array if n > elem]
    return quick_sort(left_mas) + center_mas + quick_sort(right_mas)

print(quick_sort([19, 4, 5, 17, 1]))
"""

"""
def merge_sort(array: list):
Принимает неотсортированный список и возвращает тот же
отсортированный список
    Сложность == N*log2N
    if len(array) > 1:
    Рекурсия
        С помощью рекурсии разбивает список на левую и правую часть
        пока не останется список из 1 элемента    
        left_array = merge_sort(array[:len(array)//2])
        right_array = merge_sort(array[len(array)//2:])

    Слияние:
        Получает на вход два списка, сравнивает их между собой
        и наименьший элемент вставляет в наш список
        ind_left = ind_right = ind_sort = 0
        n = len(left_array)
        m = len(right_array)
        while ind_left < n and ind_right < m:
            if left_array[ind_left] < right_array[ind_right]:
                array[ind_sort] = left_array[ind_left]
                ind_left += 1
            else:
                array[ind_sort] = right_array[ind_right]
                ind_right += 1
            ind_sort += 1
        while ind_left < n:
            array[ind_sort] = left_array[ind_left]
            ind_left += 1
            ind_sort += 1
        while ind_right < m:
            array[ind_sort] = right_array[ind_right]
            ind_right += 1
            ind_sort += 1
    return array

array = [6, 8, 2, 9, 3, 6, 1, 3, 4, 5]
print(merge_sort(array))
"""

"""
def power(n: int, m: int):
    if m == 0:
        return 1
    if m < 0:
        return 1/power(n, -m)
    if m%2 == 0:
        return power(n, m//2) * power(n, m//2)
    else:
        return power(n, m-1) * n

print(power(2,-1))
"""

"""
def get_list(array: list):
    if len(array) == 0:
        return []
    if isinstance(array[0], list):
        return get_list(array[0] + get_list(array[1:]))
    return array[:1] + get_list(array[1:])

print(get_list([1, [2, 3, [4]], 5]))
"""

"""
array = [1, 2, [True, False],
         ["Москва", "Уфа", [100, 101],
          ['True', [-2, -1]]], 7.89]
def get_arr(array: list, array_2=[]):
Проверяет, если первый элемент лист
то снова вызывает функцию от этого элемента,
если первый элемент не лист,
то вставляет его в новый список и
вызывает функцию от второго элемента 
и так пока длина изначального списка не будет равна 1
затем вернет новый список
    if len(array) > 0:
        if isinstance(array[0], list):
            get_arr(array[0])
        else:
            array_2.append(array[0])
        get_arr(array[1:], array_2)
    return array_2

print(get_arr(array))
"""

"""[0, 4, 4, 9, 16, 25, 36]"""
"""array = [-4, -2, 0, 2, 3, 5, 6]
def sort_array(array: list) -> list:
    if len(array) > 1:
        left_array = sort_array(array[:len(array)//2])
        right_array = sort_array(array[len(array)//2:])

        n = len(left_array)
        m = len(right_array)
        left_ind = right_ind = sort_ind = 0
        while left_ind < n and right_ind < m:
            if left_array[left_ind] < right_array[right_ind]:
                array[sort_ind] = left_array[left_ind]
                left_ind += 1
            else:
                array[sort_ind] = right_array[right_ind]
                right_ind += 1
            sort_ind += 1

        while left_ind < n:
            array[sort_ind] = left_array[left_ind]
            left_ind += 1
            sort_ind += 1
        while right_ind < m:
            array[sort_ind] = right_array[right_ind]
            right_ind += 1
            sort_ind += 1
    return array
print(sort_array(array))

"""
"""
import os
path = "/Users/andrejoveskov/Desktop/Фильмы"
def rec_file(path: str):
    for i in os.listdir(path):
        if os.path.isdir(path+"//"+ i):
            print("Спускаемся", path+"//"+ i)
            rec_file(path+"//"+ i)
            print("Возвращаемся", path+"//"+ i)
rec_file(path)
"""

"/Users/andrejoveskov/Desktop"

"""
a = ['1', '2', '3', '4']

def rec_dict(lst: list):
    d = {}
    if len(lst) == 1:
        return lst[0]
    d[lst[0]] = rec_dict(lst[1:])
    return d

print(rec_dict(a))

"""






































