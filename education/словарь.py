"""
Словарь изменяемый объект
Ключ у словаря может быть только неизменяемый объект
целые числа(int, float), строки(str), None, кортежи(tuple),
неизменяемые множества(frozenset)
_dict = {} Словарь
_dict = dict() Словарь


_dict = dict(name="Dry", surname="Oveshkov")
{'name': 'Dry', 'surname': 'Oveshkov'}


array = [["name", "Dry"],["age",25]]
_dict = dict(array)
{'name': 'Dry', 'age': 25}


array = dict(name="Dry", surname="Oveshkov")
print(array["name"])
Dry
array["age"] = 25
print(array)
{'name': 'Dry', 'surname': 'Oveshkov', 'age': 25}


array["age"] = 555
print(array)
{'name': 'Dry', 'surname': 'Oveshkov', 'age': 555}
del array["age"]
{'name': 'Dry', 'surname': 'Oveshkov'}

n = int(input())
_dict = {n: n**2 for n in range(1,n+1)}
print(_dict)

_dict = {'name': 'Dry', 'surname': 'Oveshkov', 'age': 25}
array = list(_dict)
print(array)
['name', 'surname', 'age']

# print("name" in _dict)True
# print("name" not in _dict)False


dict_1 = {"name": "Dry", "surname": "Oveshkov"}
dict_2 = {"age": 25}
dict_3 = dict_1 | dict_2
print(dict_3)
{'name': 'Dry', 'surname': 'Oveshkov', 'age': 25}


dict_ = {'name': 'Dry', 'surname': 'Oveshkov', 'age': 25}
dict_1 = dict_.get("city", "Not city")
print(type(dict_1), dict_1)
<class 'str'> Not city
dict_1 = dict_.get("age", "Not city")
print(type(dict_1), dict_1)
<class 'int'> 25


dict_ = {'name': 'Dry', 'surname': 'Oveshkov', 'age': 25}
dict_.setdefault("city", "Vladimir")
print(dict_)
{'name': 'Dry', 'surname': 'Oveshkov', 'age': 25, 'city': 'Vladimir'}
"""
"""
n = int(input())
d = {}
array = []
for elem in range(n):
    name = input()
    array.append(name)
    count = array.count(name)-1
    if name not in d:
        print(d.setdefault(name, "OK"))
    else:
        print(d.setdefault(name+f"{count}", name+f"{count}"))
"""

"""
n = int(input())
database = {}
for elem in range(n):
    name = input()
    if name in database:
        database[name] += 1
        database[f'{name}{database[name]}'] = 0
        print(f"{name}{database[name]}")
    else:
        database[name] = 0
        print(f'OK')
"""
"""
countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

def search_city(countries: dict, city: str):
    for key, value in countries.items():
        if city in value:
            return f"INFO: {city} is a city in {key}"
    return f"ERROR: Country for {city} not found"
city = input()
print(search_city(countries, city))
"""


"""
array = [1, 2, 3]
def rec_dict(array: list):
    if len(array) > 2:
        return {array[0]: rec_dict(array[1:])}
    return dict([array])

print(rec_dict(array))
"""


"""
def rec_dict(array:list):
    return {array[0]: rec_dict(array[1:])} \
        if len(array) > 2 else dict([array])
array = list(map(int, input().split()))
print(rec_dict(array))
"""


"""
def count_letter(line:str):
    return {line[elem]: line.count(line[elem]) for
            elem in range(len(line)) if line[elem].isalpha()}
print(count_letter("aabbbc"))
"""


"""
def anagram(line_1: str, line_2: str):
    dict_1 = {line_1[elem]: line_1.count(num) for elem in range(len(line_1))
              for num in line_1}
    dict_2 = {line_2[elem]: line_2.count(num)
              for elem in range(len(line_2)) for num in line_2}
    return "YES" if dict_1 == dict_2 else "NO"
line_1 = input()
line_2 = input()
print(anagram(line_1, line_2))
"""

"""
persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119')
    ]

def data_persons(array: list):
    return {elem[0]: dict(salary=elem[1], gender=elem[2], passport=elem[3]) for elem in persons}
print(data_persons(persons))
"""

"""
vector = [
    [1, 2, 3], [4, 5, 6],
    [7, 8, 9], [10, 11, 12],
    [13, 14, 15], [16, 17, 18]
]
a = [i for j in vector for i in j]
print(a)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
"""
"""
def phone_book(book_d={}):
    for elem in range(int(input())):
        number, name = input().split()
        book_d.setdefault(name, []).append(number)
    for elem in range(int(input())):
        name = input()
        print(*book_d.setdefault(name, ["Неизвестный номер"]))

phone_book()
"""
"""
def birthday(dict_name={}):
    for elem in range(int(input())):
        name, num, month = input().split()
        dict_name.setdefault(month, []).append(name)
    print(dict_name)
    for elem in range(int(input())):
        name = input()
        print(*dict_name.get(name, ["Нет данных"]))



birthday()
"""


horoscope_dict = {
    'fire': {
        "aries": ("aries", "Овен - первый знак зодиака, планета Марс", {3: (21, 32), 4: (1, 21)}),
        "leo": ("leo", "Лев - пятый знак зодиака, солнце", {7: (23, 32), 8: (1, 24)}),
        "sagittarius": ("sagittarius", "Стрелец - девятый знак зодиака, планета Юпитер", {11: (23, 31), 12: (1, 22)}),
    },
    'earth': {
        "taurus": ("taurus", "Телец - второй знак зодиака, планета Венера", {4: (21, 31), 5: (1, 22)}),
        "virgo": ("virgo", "Дева - шестой знак зодиака, планета Меркурий", {8: (25, 32), 9: (1, 23)}),
        "capricorn": ("capricorn", "Козерог - десятый знак зодиака, планета Сатурн",  {12: (22, 32), 1: (1, 21)}),
    },
    'air': {
        "gemini": ("gemini", "Близнецы - третий знак зодиака, планета Меркурий", {5: (22, 32), 6: (1, 22)}),
        "libra": ("libra", "Весы - седьмой знак зодиака, планета Венера", {9: (23, 31), 10: (1, 24)}),
        "aquarius": ("aquarius", "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн", {1: (21, 32), 2: (1, 19)}),
    },
    'water': {
        "cancer": ("cancer", "Рак - четвёртый знак зодиака, Луна", {6: (22, 31), 7: (1, 23)}),
        "scorpion": ("scorpion", "Скорпион - восьмой знак зодиака, планета Марс", {10: (24, 32), 11: (1, 23)}),
        "pisces": ("pisces", "Рыбы - двенадцатый знак зодиака, планеты Юпитер", {2: (19, 29), 3: (1, 21)}),
    },
}

a = 2
c = 2
response = ''
x = 'pisces'
for i in horoscope_dict.values():
    info = i.get(x)
print(info)









