# создание копии списка и
# присвоении ему новой переменной
# это будет два разный списка
# a = [n for n in range(4)]
# b = list(a)
# [0, 1, 2, 3] 4445558144 [0, 1, 2, 3] 4445557568
# b = a[:]
# [0, 1, 2, 3] 4353857024 [0, 1, 2, 3] 4353942080

# b = sorted(a)
# [2, 4, 1, 3] 4452505216 [1, 2, 3, 4] 4452590336
# b = sorted(a, reverse=True)
# [2, 4, 1, 3] 4393440704 [4, 3, 2, 1] 4393525952
# a.sort(reverse=True)
# [4, 3, 2, 1] 4451489216
# print(a, id(a), b, id(b))

# a = [n for n in range(4)]
# b = []
# for i in range(len(a)-1,-1,-1):
#     b.append(i)
# [0, 1, 2, 3] 4522353344 [3, 2, 1, 0] 4522284544
# b = [i for i in range(len(a)-1,-1,-1)]
# [0, 1, 2, 3] 4552843968 [3, 2, 1, 0] 4552775168
# print(a, id(a), b, id(b))

# Создание новой переменной с использованием
# раннее созданной копии списка
# a = [n for n in range(4)]
# b = [n for n in range(len(a)-1, -1,-1)]
# print(a, id(a), b, id(b))
# [0, 1, 2, 3] 4441531072 [3, 2, 1, 0] 4441462272

# def invert_list(lst: list) -> list:
#     new_invert_list = [n for n in range(len(lst), -1, -1)]
#     return new_invert_list
# print(invert_list([1, 2, 3, 4, 5]))


# def sort_dict(dict_: dict) -> dict:
#     copy_dict = sorted(dict_)
#     new_sorted_dict = {}
#     for i in copy_dict:
#         new_sorted_dict[i] = dict_[i]
#     return new_sorted_dict
# print(sort_dict({'inversed': 8, 'house': 5,'car': 3}))

# def sort_dict(dict_: dict) -> dict:
#     return {i: dict_[i] for i in sorted(dict_)}
# print(sort_dict({'inversed': 8, 'house': 5, 'car': 3}))
# {'car': 3, 'house': 5, 'inversed': 8}

# вставка в список элемента с использованием счетчика индексов
# a = [1,2,3,4,5,6]
# n = 0
# for i in range(len(a)):
#     n += 1
#     if n == 3:
#         a[i] = 7
# print(a) [1, 2, 7, 4, 5, 6]


# a = [1, 7, 3, 2, 5, 4, -1]
# N = len(a)
# for i in range(1, N):
#     for j in range(0, N-i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a) #[-1, 1, 2, 3, 4, 5, 7]

# def insert_sort(A):
#     """ Сортировка списка А вставками """
#     N = len(A)
#     for top in range(1, N):
#         k = top
#         while k > 0 and A[k-1] > A[k]:
#             A[k], A[k - 1] = A[k - 1], A[k]
#             k -= 1
#
#
# def choice_sort(A):
#     """ Сортировка списка А выбором """
#     N = len(A)
#     for pos in range(0, N-1):
#         for k in range(pos+1, N):
#             if A[k] < A[pos]:
#                 A[k], A[pos] = A[pos], A[k]
#
#
# def bubble_sort(A):
#     """ Сортировка списка А методом пузырька """
#     N = len(A)
#     for pos in range(1, N):
#         for k in range(0, N-pos):
#             if A[k] > A[k+1]:
#                 A[k], A[k+1] = A[k+1], A[k]
#
#
# def test_sort(sort_algorithm):
#     print("Тестируем: ", sort_algorithm.__doc__)
#     print("testcase #1: ", end='')
#     A = [4, 2, 5, 1, 3]
#     A_sorted = [1, 2, 3, 4, 5]
#     sort_algorithm(A)
#     print("Ok" if A == A_sorted else "Fail")
#
#     print("testcase #2: ", end='')
#     A = list(range(10, 20)) + list(range(0, 10))
#     A_sorted = list(range(20))
#     sort_algorithm(A)
#     print("Ok" if A == A_sorted else "Fail")
#
#     print("testcase #3: ", end='')
#     A = [4, 2, 4, 2, 3]
#     A_sorted = [2, 2, 3, 4, 4]
#     sort_algorithm(A)
#     print("Ok" if A == A_sorted else "Fail")
#
#
# if __name__ == "__main__":
#     test_sort(insert_sort)
#     test_sort(choise_sort)
#     test_sort(bubble_sort)

# def count_algorithm(A):
#     """Сортировка списка А методом подсчета"""
#     N = len(A) + 1
#     B = [0] * N
#     for i in A:
#         B[i] += 1
#     A[:] = []
#     for num in range(N):
#         A += [num] * B[num]
#
# def test_count_algorithm(sort_algorithm):
#     print("Тестируем: ", count_algorithm.__doc__)
#     print("Testcase #1: ", end='')
#     A = [6, 4, 2, 5, 3, 1, 4, 1, 3, 5, 6]
#     A_sorted = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6]
#     sort_algorithm(A)
#     print("Ok" if A == A_sorted else "Fail")
#
# test_count_algorithm(count_algorithm)
# Тестируем:  Сортировка списка А методом подсчета
# Testcase #1: Ok


# def bubble_sort(A: list):
#     """Сортировка списка А пузырьковым методом"""
#     N = len(A)
#     for pos in range(1, N):
#         for i in range(0, N-pos):
#             if A[i] > A[i+1]:
#                 A[i], A[i+1] = A[i+1], A[i]
#     return A
#
# def test_sort(sort_algorithm):
#     print("Testcase #1 : ", end='')
#     A = [8, 5, 3, 1, 4, 7, 9]
#     A_sort = [1, 3, 4, 5, 7, 8, 9]
#     sort_algorithm(A)
#     print("Ok" if A == A_sort else "Fail")
#
# test_sort(bubble_sort)

# def insert_sort(A):
#     """Сортировка списка А методом вставки"""
#     N = len(A)
#     for pos in range(1, N):
#         k = pos
#         while k > 0 and A[k] < A[k-1]:
#             A[k], A[k-1] = A[k-1], A[k]
#             k -= 1
#
#
# def test_sort(sort_algorithm):
#     print("Testcase #1 : ", end='')
#     A = [5, 4, 2, 15, 6, 6]
#     A_sort = [2, 4, 5, 6, 6, 15]
#     sort_algorithm(A)
#     print("OK" if A == A_sort else "Fail")
#
# test_sort(insert_sort)

# lst = [(1, 10), (2, 20), (3, 30)]
# for tup in lst:
#     angle, lenght = tup
#     print(angle, lenght)
#     1   10
#     2   20
#     3   30

#
# lst = [(1, 10), (2, 20), (3, 30)]
# for angle, lenght in lst:
#     print(angle, lenght)
#     1   10
#     2   20
#     3   30
#
# lst = [(1, 10), (2, 20), (3, 30)]
# for i, x in enumerate(lst):
#     print(i,x)
#     0(1, 10)
#     1(2, 20)
#     2(3, 30)


# lst = [(1, 10), (2, 20)]
# d = dict(lst)
# print(d) {1: 10, 2: 20}


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
def merge_sort(arr):
# Сортировка слиянием одного массива без создания нового массива
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #  Рекурсия
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Слияние
        n = len(left_arr)
        m = len(right_arr)
        left_ind = right_ind = k = 0
        while left_ind < n and right_ind < m:
            if left_arr[left_ind] < right_arr[right_ind]:
                arr[k] = left_arr[left_ind]
                left_ind += 1
            else:
                arr[k] = right_arr[right_ind]
                right_ind += 1
            k += 1

        while left_ind < n:
            arr[k] = left_arr[left_ind]
            left_ind += 1
            k += 1
        while right_ind < m:
            arr[k] = right_arr[right_ind]
            right_ind += 1
            k += 1
    return arr

array_test = [6, 8, 2, 9, 3, 6, 1, 3, 4, 5]

print(merge_sort(array_test))
"""

"""
array_1 = [9, 7, 5, 3, 1]
array_1.sort()
array_2 = [8, 6, 4, 2, 0]
array_2.sort()
def sort_mas(array_1: list, array_2: list):
Принимает два отсортированных списка и 
возвращает новый отсортированный список
    n = len(array_1)
    m = len(array_2)
    sort_array = [0] * (n+m)
    ind_1 = ind_2 = ind_sort = 0
    while ind_1 < n and ind_2 < m:
        if array_1[ind_1] <= array_2[ind_2]:
            sort_array[ind_sort] = array_1[ind_1]
            ind_1 += 1
        else:
            sort_array[ind_sort] = array_2[ind_2]
            ind_2 += 1
        ind_sort += 1

    while ind_1 < n:
        sort_array[ind_sort] = array_1[ind_1]
        ind_1 += 1
        ind_sort += 1
    while ind_2 < m:
        sort_array[ind_sort] = array_2[ind_2]
        ind_2 += 1
        ind_sort += 1

    return sort_array

print(sort_mas(array_1, array_2))
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
def sort_array(array: list) -> list:
    # Сложность O(N)
    # Принимает отсортированный массив
    # и возвращает новый массив из элементов в квадрате
    # в отсортированном виде
    n = len(array)
    sort_array = [0] * n
    sort_ind = 0
    # Нахожу первое отрицательно число и
    # первое положительное число
    for index, value in enumerate(array):
        if value >= 0:
            right_ind = index
            break
        else:
            left_ind = index
    # Правый индикатор с отрицательным числом идет по массиву
    # в право пока не будет равен нулю
    # Правый индикатор с положительным числом идет влево
    # пока не дойдет до конца длины массива
    # Возвожу в квадрат и сравниваю их между собой
    while left_ind >= 0 and right_ind < n:
        right_pos = array[right_ind] ** 2
        left_pos = array[left_ind] ** 2
        # Вставляю в новый массив наименьшее из них
        if right_pos < left_pos:
            sort_array[sort_ind] = right_pos
            right_ind += 1
        else:
            sort_array[sort_ind] = left_pos
            left_ind -= 1
        sort_ind += 1
    while right_ind < n:
        sort_array[sort_ind] = right_pos
        right_ind += 1
        sort_ind += 1
    while left_ind > 0:
        sort_array[sort_ind] = left_pos
        left_ind -= 1
        sort_ind += 1
    return sort_array

# array = [-6, -4, -2, 0, 3, 5, 7]
print(sort_array(list(map(int, input().split()))))
"""

"""
def sort_merge(array: list):
    if len(array) > 1:
        left_array = sort_merge(array[:len(array)//2])
        right_array = sort_merge(array[len(array)//2:])

        left_ind = right_ind = sort_ind = 0
        n = len(left_array)
        m = len(right_array)
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
# array_1 = [-6, -4, -2, 0, 3, 5, 7]
# array = [elem**2 for elem in array_1]
print(sort_merge(array = [elem**2 for elem in list(map(int, input().split()))]))

"""
"""
def left_bound(array: list, key):
    n = len(array)
    left_ind = -1
    right_ind = n
    while right_ind - left_ind > 1:
        middle = (left_ind + right_ind) // 2
        if array[middle] < key:
            left_ind = middle
        else:
            right_ind = middle
    return left_ind


def right_bound(array: list, key):
    n = len(array)
    left_ind = -1
    right_ind = n
    while right_ind - left_ind > 1:
        middle = (left_ind + right_ind) // 2
        if array[middle] <= key:
            left_ind = middle
        else:
            right_ind = middle
    return right_ind


def bin_search(array: list, key):
    left_side = left_bound(array, key)
    right_side = right_bound(array,key)
    if right_side - left_side > 1:
        return array[left_side+1:right_side]
    return "Key not found"

array = [1, 3, 3, 3, 3, 6, 7, 9]

print(bin_search(array, 3))
"""

"""
def bin_search(array, key):
    if key in array:
        def left_bound(array, key):
            n = len(array)
            left_ind = -1
            right_ind = n
            while right_ind - left_ind > 1:
                middle = (left_ind + right_ind) // 2
                if array[middle] < key:
                    left_ind = middle
                else:
                    right_ind = middle
            return left_ind

        def right_bound(array, key):
            n = len(array)
            left_ind = -1
            right_ind = n
            while right_ind - left_ind > 1:
                middle = (left_ind + right_ind) // 2
                if array[middle] <= key:
                    left_ind = middle
                else:
                    right_ind = middle
            return right_ind

        left_side = left_bound(array, key)
        right_side = right_bound(array, key)
        if right_side - left_side > 1:
            return array[left_side+1:right_side]
    return "Key not found"

array = [1, 2, 3, 4, 5, 5, 6, 7]
print(bin_search(array, 5))
"""
"""
a = [-4, -10, -5, 0, 2, 7, 32, 9]
a = sorted(a, key=abs)
print(a) [0, 2, -4, -5, 7, 9, -10, 32]
"""
"""
a = [-45, -10, -53, 0, 2, 7, 32, 91]
a = sorted(a, key=lambda x: x%10)
print(a) [-10, 0, 91, 2, 32, -45, -53, 7]
"""
"""
a = ["AAA", "ZZZ", "EEE", "www", "aaa", "zzz"]
a = sorted(a, key=str.lower)
print(a) ['AAA', 'aaa', 'EEE', 'www', 'ZZZ', 'zzz']
"""
"""
a = ["AAA 23", "ZZZ 91", "EEE 22", "www 43", "aaa 56", "zzz 32"]
a = sorted(a, key=lambda x: int(x.split()[1]))
print(a) ['EEE 22', 'AAA 23', 'zzz 32', 'www 43', 'aaa 56', 'ZZZ 91']
"""
"""
a = ["AAA 22", "ZZZ 91", "EEE 22", "www 12", "aaa 12", "zzz 12"]
a = sorted(a, key=lambda x: (int(x.split()[1]), x.split()[0].lower()))
print(a) ['aaa 12', 'www 12', 'zzz 12', 'AAA 22', 'EEE 22', 'ZZZ 91']
"""

"""
subject_marks = [('English', 88), ('Science', 90),
                 ('Maths', 97), ('Physics', 93),('History', 82)]
def sort_list(array):
    for elem in range(len(array)):
        return array[1]
array = sorted(subject_marks, key=sort_list)
for elem in array:
    print(*elem)
"""
"""
def sort_array(array: list):
    def search_int(array):
        for elem in range(len(array)):
            return array[1]
    array = sorted(array, key=search_int)
    for elem in array:
        print(*elem)

subject_marks = [('English', 88), ('Science', 90),
                 ('Maths', 97), ('Physics', 93),('History', 82)]
sort_array(subject_marks)

"""
"""
def sort_array(array: list):
    array = sorted(array, key=lambda x: x[1])
    for elem in array:
        print(*elem)

subject_marks = [('English', 88), ('Science', 90),
                 ('Maths', 97), ('Physics', 93),('History', 82)]
sort_array(subject_marks)
"""
"""
subject_marks = [('English', 88), ('Science', 90),
                 ('Maths', 97), ('Physics', 93),('History', 82)]
for elem in sorted(subject_marks, key=lambda x: x[1]):
    print(*elem)
"""
"""
def sort_descending(array: list):
    for elem in sorted(array, key=lambda x: -x[1]):
        print(*elem)


subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
                 ('Physics', 93), ('History', 82), ('French', 78),
                 ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
sort_descending(subject_marks)
"""

"""
def sort_list(array:list):
    for elem in sorted(array, key=lambda x: (-x[1], x[0])):
        print(*elem)
subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
sort_list(subject_marks)
"""
"""
def sort_color(array: list):
    for elem in sorted(array, key=lambda x: x["color"]):
        print(f"Производитель: {elem['make']}, модель: {elem['model']}, цвет: {elem['color']}")
models = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
]
sort_color(models)
"""
"""
def price_product(dict_product={}):
    while True:
        product = input().split(": ")
        if product == ["end"]:
            break
        else:
            dict_product[product[0]] = int(product[1])
    for key, value in sorted(dict_product.items(), key=lambda x: -x[1]):
        print(key)
price_product()
"""
"""
array = [elem for elem in iter(input,"end")]
print(array)

"""
"""
def sort_price():
    price = [elem.split(": ") for elem in iter(input,"end")]
    for elem in sorted(price, key=lambda x: -int(x[1])):
        print(elem[0])
sort_price()
"""
"""
def oscar(num_oscar: int):
    actor = {}
    for elem in range(num_oscar):
        name = input()
        actor.setdefault(name, 0)
        if name in actor:
            actor[name] += 1
    array = [(key, value) for key, value in actor.items()]
    array = sorted(array, key=lambda x: (-x[1], x[0]))
    actor_victory = f"{array[0][0]}, {array[0][1]}"
    actor_failed = f"{array[-1][0]}, {array[-1][1]}"
    print(actor_victory)
    print(actor_failed)
num_oscar = int(input())
oscar(num_oscar)
"""
"""
def birthday(dict_name={}):
    for elem in range(int(input())):
        name, num, month = input().split()
        dict_name.setdefault(month, []).append(name)
    for key in dict_name:
        dict_name[key] = sorted(dict_name[key])
    for elem in range(int(input())):
        name = input()
        print(*dict_name.get(name, ["Нет данных"]))
birthday()
"""
"""
def rating(dict_name={}):
    while True:
        line = input().split(", ")
        if line == ["end"]:
            break
        else:
            name, grade = line[0], int(line[1])
            dict_name.setdefault(name, []).append(grade)

    def average_rating(array: list):
        for elem in array:
            return sum(array)/len(array)
    for key in dict_name:
        dict_name[key] = average_rating(dict_name[key])
    for key, value in sorted(dict_name.items(), key=lambda x: (-x[1], x[0])):
        print(key, value)

rating()
"""
"""
def rating(dict_name={}):
    for date in iter(input, "end"):
        name, grade = date.split(", ")
        dict_name.setdefault(name, []).append(int(grade))
    for key in dict_name:
        dict_name[key] = sum(dict_name[key])/len(dict_name[key])
    for key, value in sorted(dict_name.items(), key=lambda x: (-x[1], x[0])):
        print(key, value)
rating()
"""
"""
def date_comment():
    dict_comm = {"Дили": [], 'Били': [], 'Вили': []}
    for date in iter(input, "end"):
        name, comment = date.split(": ")
        if comment not in dict_comm[name]:
            dict_comm[name] += [comment]
        else:
            continue
    print(dict_comm)
    for key, value in sorted(dict_comm.items(), key=lambda x: -len(x[1])):
        print(f"Количество уникальных комментаторов у {key} - {len(value)}")
date_comment()
"""
"""
def date_comment():
    dict_comm = {"Дили": set(), "Били": set(), "Вили": set()}
    for date in iter(input, "end"):
        name, comment = date.split(": ")
        dict_comm.setdefault(name, set()).add(comment)
    for key, value in sorted(dict_comm.items(), key=lambda x: -len(x[1])):
        print(f"Количество уникальных комментаторов у {key} - {len(value)}")
date_comment()
"""





















