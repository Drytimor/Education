"""
class Person:
    name = 'Jared'
    age = 30


print(Person.age) # 30
print(getattr(Person, 'name')) # Jared
print(Person.__dict__)
# {'__module__': '__main__', 'name': 'Jared', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

print(hasattr(Person, 'name')) #True
Person.name = "Misha"
print(Person.name) #Misha
Person.money = 100
print(Person.money) # 100
setattr(Person, 'name', 'Ivan')
print(Person.name)
del Person.money
delattr(Person, 'age')
"""
from typing import Dict, Any

"""
class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


lst = list(map(str, input().split()))

for i in lst:
    flag = hasattr(Person, i.lower())
    if flag:
        print(f'{i}-YES')
    else:
        print(f'{i}-NO')
"""
"""
class SuperHero:
    pass

batman = SuperHero()
superman = SuperHero()

batman.can_fly = False
batman.damage = 175

superman.can_fly = True
superman.damage = 285
superman.alter_ego = 'Кларк Кент'
"""
"""
class Config:
    pass

def create_instance(n: int) -> Config:
    obj = Config()
    for n in range(1, n+1):
        setattr(obj, f'attribute{n}', f'value{n}')
    return obj

config_2 = create_instance(4)
print(isinstance(config_2, Config))
"""
"""
class Car:
    model = "BMW"
    engine = 1.6

    @staticmethod
    def drive():
        print('lets go')
"""
"""
class Cat:
    breed = 'pers'

    def hello(self):
        print(f'Hello world from {self.name}')


    def show_breed(self):
        print(f'my breed is {self.breed}')

    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('nothing')

    def set_value(self, name, age=0):
        self.name = name
        self.age = age
"""
"""
class Robot:

    def set_name(self, name):
        self.name = name

    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')
"""
"""
class Counter:

    def start_from(self, count=0):
        self.count = count

    def increment(self):
        self.count += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.count}')

    def reset(self):
        self.count = 0

"""
"""
class Constructor:

    def add_atribute(self, name: str, value):
        setattr(self, name, value)

    def display(self):
        print(self.__dict__)
"""
"""
from math import sqrt

class Point:
    def set_coordinates(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_distance(self, value):
        if isinstance(value, Point):
            pfg = sqrt((self.x - value.x)**2 + (self.y-value.y)**2)

            return pfg

        print('Передана не точка')

p1 = Point()
p2 = Point()
p1.set_coordinates(1,2)
p2.set_coordinates(4,6)
d = p1.get_distance(p2)
print(d) # 5.0
"""
"""
class Cat:

    def __init__(self, name='Cat', breed='pers', age=0, color='black'):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage




class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years"


class Laptop:

    def __init__(self, brand=None, model=None, price=None):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'


class SoccerPlayer:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

        self.goals = 0
        self.assists = 0

    def score(self, increase=1):
        self.goals += increase

    def make_assists(self, increase=1):
        self.assists += increase

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')


class Zebra:

    def __init__(self):
        self.color1 = 'Полоска белая'
        self.color2 = 'Полоска черная'
        self.count = 1

    def which_stripe(self):
        # print(self.color1 if self.count % 2 == 1 else self.color2)
        # self.count += 1
        self.color1, self.color2 = self.color2, self.color1

"""
"""
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name}{self.first_name}'


    def is_adult(self):
        return True if self.age >= 18 else False


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2




class Stack:

    def __init__(self):
        self.values = []


    def push(self, item):
        self.values.append(item)


    def pop(self):
        if len(self.values) == 0:
             print('Empty Stack')
        else:
            return self.values.pop()


    def peek(self):
        if len(self.values) == 0:
            print('Empty Stack')
            return None
        else:
            return self.values[-1]


    def is_empty(self):
        return False if len(self.values) > 0 else True


    def size(self):
        return len(self.values)

"""
"""
class Worker:

    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print(f'Worker {self.name}; passport-{self.passport}')

persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
]

worker_object = [Worker(*i) for i in persons]

for i in worker_object:
    i.get_info()
"""
"""
class CustomLabel:

    def __init__(self, text, **kwargs):
        self.text = text
        self.config(**kwargs)


    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

a = CustomLabel("hello", a=1)
a.config(a=2)
# {'text': 'hello', 'a': 2}
print(a.__dict__)

"""
"""
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:

    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.comoany_name}, {self.location}')


class Employee:

    def __init__(self, name, age, company_name, location):
        self.personal_data = Person(name, age)
        self.work = Company(company_name, location)

"""
"""
class Task:

    def __init__(self, name, description, status=False):
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        print(f"{self.name} {'Сделана' if self.status else 'Не сделана'}")


class TaskList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


class TaskManager:

    def __init__(self, TaskList):
        self.task_list = TaskList

    def mark_done(self, Task):
        Task.status = True

    def mark_undone(self, Task):
        Task.status = False

    def show_tasks(self):
        for i in self.task_list.tasks:
            Task.display(i)
"""
"""
class Cat:
# Моносостояние для всех объектов
    __shared_attr = {
        'name': 'Tom',
        'age': 10
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr

cat1 = Cat()
cat2 = Cat()

cat1.name = 'Jery'

print(cat2.__dict__)
# {'name': 'Jerry', 'age': 10}

"""
"""
class WeatherStation:

    __sheared_attr = {
        'temperature': 0,
        'humidity': 0,
        'pressure': 0
    }

    def __init__(self):
        self.__dict__ = WeatherStation.__sheared_attr

    def update_data(self, temper, hum, pres):
        self.__sheared_attr['temperature'] = temper
        self.__sheared_attr['humidity'] = hum
        self.__sheared_attr['pressure'] = pres



    def get_current_data(self):
        return self.__sheared_attr['temperature'], self.__sheared_attr['humidity'], self.__sheared_attr['pressure']
"""
"""
class BankAccount:

    def __init__(self, name, balance, passport):
        # приватные атрибуты
        self.__name = name
        self.__balance = balance
        self.__passport = passport


    def print_protected_data(self):
        # разрешенные атрибуты через метод
        print(self.__name, self.__balance, self.__passport)

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

ac1 = BankAccount('dry', 123, '394023')

print(ac1.__dict__)
print(ac1._BankAccount__name)
print(ac1._BankAccount__balance)
# {'_BankAccount__name': 'dry', '_BankAccount__balance': 123, '_BankAccount__passport': '394023'}
# dry
# 123
"""
"""
class Student:

    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}, Возраст: {self.__age}, Направление: {self.__branch}', sep='\n')

    def access_private_method(self):
        self.__display_details()


class BankDeposit:

    def __init__(self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self):
        return self.balance * (self.rate / 100)

    def get_balance_with_profit(self):
        return self.balance + self.__calculate_profit()
"""
"""
class Library:

    def __init__(self, books: list):
        self.__books = books

    def ___check_availability(self, name_book):
        return True if name_book in self.__books else False

    def search_book(self, name_book):
        return self.__check_availability(name_book)

    def return_book(self, name_book):
        self.__books.append(name_book)

    def _checkout_book(self, name_book):
        if self.__check_availability(name_book):
            self.__books.remove(name_book)
            return True
        return False
"""
"""
class Employee:

    def __init__(self, name, position, hours_worked, hourly_rate):
        self.name = name
        self.__position = position
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    def __calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate


    def _set_position(self, name):
        self.__position = name

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__calculate_salary()


    def get_employee_details(self):
        return f"Name: {self.name}, Position: {self.__position}, Salary: {self.__calculate_salary()}"

"""
"""
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Должно быть числом')
        self.__balance = value

    def del_balance(self):
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)

"""
"""
class BankAccount:

    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account(self):
        return self._account_cumber

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value

"""
"""
class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    def __set_salary(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__salary = value
        else:
            raise ValueError(f'ErrorValue:{value}')

    title = property(fget=__get_name)

    reward = property(fget=__get_salary, fset=__set_salary)
"""
"""
import re

class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if isinstance(value, str):
            reg = r'\w+[@]\w*[.]\w+'
            match = re.fullmatch(reg, value)
            if match:
                self.__email = value
            else:
                print(f"ErrorMail:{value}")


    email = property(fget=get_email, fset=set_email)
"""
"""
class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Not integer')
        else:
            self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        del self.__balance
"""
"""
class Notebook:

    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        for num, val in enumerate(self._notes, 1):
            print(f'{num}.{val}')
"""
"""
class Square:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = float(value)

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, value):
        self.side = value ** 0.5
"""
"""
class Money:

    def __init__(self, dollars, cents):
        self.total_cents = 100*dollars + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = self.cents + value*100
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 <= value < 100:
            self.total_cents = self.dollars * 100 + value
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'


    def add_money(self, Money):
        return self.total_cents + Money.total_cents
"""
"""
class Square:

    def __init__(self, side):
        self.__side = side
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.side**2
        return self.__area

"""
"""
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.__area = None


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if isinstance(value, (int, float)):
            self.__length = value
            self.__area = None
        else:
            raise ValueError('Enter the number')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, (int, float)):
            self.__width = value
            self.__area = None
        else:
            raise ValueError('Enter the number')


    @property
    def area(self):
        if self.__area is None:
            self.__area = self.length * self.width
            return self.__area
        return self.__area

"""

"""
from datetime import date

class Date:

    def __init__(self, day, month, year):
        self.__date = date(year, month, day)

    @property
    def date(self):
        return self.__date.strftime('%d/%m/%Y')

    @property
    def usa_date(self):
        return self.__date.strftime('%m-%d-%Y')
"""
"""
class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


    @property
    def date(self):
        return f'{self.day:02}/{self.month:02}/{self.year:04}'

    @property
    def usa_date(self):
        return f'{self.month:02}-{self.day:02}-{self.year:04}'
"""
"""
class Password:

    def __init__(self, password):
        self.password = password

    @property
    def strength(self):
        if len(self.password) < 8:
            return 'Weak'
        elif len(self.password) >= 12:
            return 'Strong'
        return 'Medium'
"""
"""
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(C):
        return C*9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(F):
        return (F-32) * 5/9

"""
"""
class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color

    @classmethod
    def get_red_car(cls, model):
        return cls(model, 'red')

car = Car.get_red_car('BMW')
"""
"""
class Circle:

    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @classmethod
    def from_diameter(cls, radius):
        return cls(radius/2)


    @staticmethod
    def is_positive(radius):
        return True if radius > 0 else False

    @staticmethod
    def area(radius):
        return 3.14 * radius**2
"""
"""
class DepartamentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info_1(self):
        print(DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)

    @classmethod
    def info_2(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    @property
    def info_prop(self):
        return self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV

    @staticmethod
    def info_static():
        print(DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)

    @staticmethod
    def hiring_pyt_dev():
        DepartamentIT.PYTHON_DEV += 1
"""
"""
class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self):
        self.instance_attribute = "I am an instance attribute"

    @classmethod
    def create_attr(cls, attr_name, attr_value):
        setattr(cls, attr_name, attr_value)


    def instance_attr(self, attr_name, attr_value):
        setattr(self, attr_name, attr_value)


example_1 = MyClass()
example_2 = MyClass()
example_3 = MyClass()

example_1.create_attr('new_attr', "Hello world")
"""
"""
class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print(f'Робот {self.name} был создан')
        Robot.population += 1

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} был уничтожен')

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя особь человеческого рода')

    @classmethod
    def how_many(cls):
        print(f'{cls.population} вот сколько нас еще осталось')
"""
"""
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Access:

    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        return True if role in Access.__access_list else False

    # @staticmethod
    # def get_access(user):
    #     if isinstance(user, User):
    #         if user.role in Access.__access_list:
    #             if Access.__check_access(user.role):
    #                 print(f'User {user.name}: success')
    #         else:
    #             print('AccessDenied')
    #     else:
    #         print('AccessTypeError')
    @staticmethod
    def get_access(user):
        if isinstance(user, User):
            print(['AccessDenied', f'User {user.name}: success'][Access.__check_access(user.role)])
        else:
            print('AccessTypeError')
"""
"""
class BankAccount:
    bank_name = 'Tinkoff Bank'
    address = 'Москва, ул. 2-я Хуторская, д. 38А'

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, balance):
        return cls(name, balance)

    @classmethod
    def bank_info(cls):
        return f'{cls.bank_name} is located in {cls.address}'
"""
"""
from my_module.search import search_file
import re
class R:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @login.setter
    def login(self, new_login):
        if isinstance(new_login, str):
            if new_login.count('@') != 1:
                raise ValueError
            elif new_login.count('.') < 1:
                raise ValueError
            elif new_login.index('@') > new_login.index('.'):
                raise ValueError
            else:
                self.__login = new_login
        else:
            raise TypeError

    @password.setter
    def password(self, new_password):
        if isinstance(new_password, str):
            if 5 > len(new_password) > 11:
                raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
            elif not R.is_include_digit(new_password):
                raise ValueError('Пароль должен содержать хотя бы одну цифру')
            elif not R.is_include_all_register(new_password):
                raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
            elif not R.is_include_only_latin(new_password):
                raise ValueError('Пароль должен содержать только латинский алфавит')
            elif R.check_password_dictionary(new_password):
                raise ValueError('Ваш пароль содержится в списке самых легких')
            else:
                self.__password = new_password
        else:
            raise TypeError('Пароль должен быть строкой')

    @staticmethod
    def is_include_digit(new_password):
        reg = r'[0-9]'
        match = re.search(reg, new_password)
        return True if match else False

    @staticmethod
    def is_include_all_register(new_password):
        reg = r'[A-Z]+[a-z]+|[a-z]+[A-Z]+'
        match = re.search(reg, new_password)
        return True if match else False

    @staticmethod
    def is_include_only_latin(new_password):
        reg = r'[A-Za-z\d]+'
        match = re.fullmatch(reg, new_password)
        return True if match else False

    @staticmethod
    def check_password_dictionary(new_password):
        with open('easy_passwords.txt') as file:
            for elem in file.readlines():
                if elem.strip() == new_password:
                    return True
            return False

"""

"""
class File:

    def __init__(self, name):
        self.is_deleted = False
        self.in_trash = False
        self.name = name

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            print(f"ErrorReadFileDeleted({self.name})")
        elif self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
        else:
            print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            print(f"ErrorWriteFileDeleted({self.name})")
        elif self.in_trash:
            print(f"ErrorWriteFileTrashed({self.name})")
        else:
            print(f"Записали значение {content} в файл {self.name}")


class Trash:

    content = []

    @staticmethod
    def add(*args):
        for elem in args:
            if isinstance(elem, File):
                Trash.content.append(elem)
                elem.in_trash = True
            else:
                print('В корзину добавлять можно только файл')

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for elem in Trash.content:
            elem.remove()
        Trash.content.clear()


        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for elem in Trash.content:
            elem.restore_from_trash()
        Trash.content.clear()

        print('Корзина пуста')
"""
"""
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:

    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, check: int):
        self.__balance += check

    def payment(self, check: int):
        if check > self.__balance:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.__balance -= check
            return True

class Cart:


    def __init__(self, user, goods={}):
        self.user = user
        self.goods = goods
        self.__total = 0

    def add(self, product, total=1):
        self.goods.setdefault(product, total)
        self.__total += product.price * total

    def remove(self, product, total=1):
        if total > self.goods[product]:
            self.__total -= product.price * self.goods[product]
            del self.goods[product]
        else:
            self.goods[product] -= total
            self.__total -= product.price * total

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print('Заказ оплачен')
        else:
            print("Проблемы с оплатой")

    def print_check(self):
        print("---Your check---")
        for product, total in sorted(self.goods.items(), key=lambda x: x[0].name):
            print(f"{product.name} {product.price} {total} {product.price * total}")
        print(f"---Total: {self.total}---")
"""
"""
class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender == "female" or gender == 'male':
            self.gender = gender
        else:
            self.gender = 'male'
            print(f"Не знаю, что вы имели ввиду? Пусть это будет мальчик!")

    def __str__(self):
        if self.gender == 'female':
            return f'Гражданка {self.surname} {self.name}'
        else:
            return f'Гражданин {self.surname} {self.name}'
"""
"""
class Vector:

    def __init__(self, *args):
        self.values = [n for n in args if type(n) == int]

    def __str__(self):
        if len(self.values) > 0:
            return f"Вектор{tuple(sorted(self.values))}"
        else:
            return f'Пустой вектор'
"""
"""
class GroceryItem:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nQuantity{self.quantity}"

    def __repr__(self):
        return f"GroceryItem({self.name}, {self.price}, {self.quantity})"



"""
"""
class Hero:
    def __len__(self):
        return len(self.__dict__)

    def __str__(self):

        if len(self.__dict__) == 0:
            return ''
        else:
            attr = ''
            for key, value in sorted(self.__dict__.items()):
                attr += f"{key}: {str(value)}\n"
            return attr.rstrip('\n')
"""
"""
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        return Rectangle(self.width+other.width, self.height+other.height)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"
"""
"""
class Order:

    def __init__(self, cart: list, customer):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):

        return Order(self.cart + [other], self.customer)

    def __radd__(self, other):
        return Order([other] + self.cart, self.customer)

    def __sub__(self, other):
        if other in self.cart:
            new_cart = [i for i in self.catr]
            new_cart.remove(other)
            return Order(new_cart, self.cusomer)
        return self

    def __rsub__(self, other):
        return self.__sub__(other)

"""
"""
class Vector:

    def __init__(self, *args):
        self.values = sorted(n for n in args if type(n) == int)

    def __str__(self):
        if len(self.values) > 0:
            return f"Вектор{tuple(self.values)}"
        return f"Пустой вектор"


    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[n+other for n in self.values])
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*[i+j for i, j in zip(other.values, self.values)])
            print('Сложение векторов разной длины недопустимо')
        print('Вектор нельзя сложить с {other}')


    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*[n*other for n in self.values])
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*[i*j for i,j in zip(other.values, self.values)])
            print('Умножение векторов разной длины недопустимо')
        print(f'Вектор нельзя умножить с {other}')
"""
"""
class Fruit:

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    def __eq__(self, other):
        print('__eq__')
        if isinstance(other, Fruit):
            return self.price == other.price
        if isinstance(other, (int, float)):
            return self.price == other

    def __lt__(self, other):
        print('__lt__')
        if isinstance(other, Fruit):
            return self.price < other.price
        if isinstance(other, (int, float)):
            return self.price < other

    def __gt__(self, other):
        print('__gt__')
        if isinstance(other, Fruit):
            return self.price > other.price
        if isinstance(other, (int, float)):
            return self.price > other


    def __le__(self, other):
        print('__le__')
        if isinstance(other, Fruit):
            return self.price < other.price or self.price == other.price
        if isinstance(other, (int, float)):
            return self.price < other or self.price == other

    def __ge__(self, other):
        print('__ge__')
        if isinstance(other, Fruit):
            return self.price > other.price or self.price == other.price
        if isinstance(other, (int, float)):
            return self.price > other or self.price == other

    def __hash__(self):
        return hash(self.price)
"""
"""
class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        elif isinstance(other, ChessPlayer):
            return self.rating == other.rating
        return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        elif isinstance(other, ChessPlayer):
            return self.rating < other.rating
        return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        elif isinstance(other, ChessPlayer):
            return self.rating > other.rating
        return 'Невозможно выполнить сравнение'
"""
"""
from functools import total_ordering

@total_ordering
class Account:

    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.balance == other.balance
        elif isinstance(other, (int, float)):
            return self.balance == other
        return 'Невозможно выполнить сравнение'


    def __lt__(self, other):
        if isinstance(other, Account):
            return self.balance < other.balance
        elif isinstance(other, (int, float)):
            return self.balance < other
        return 'Невозможно выполнить сравнение'
"""
"""
from functools import total_ordering

@total_ordering
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, int):
            return self.area == other
        if isinstance(other, Rectange):
            return self.area == other.area

    def __lt__(self, other):
        if isinstance(other, int):
            return self.area < other
        if isinstance(other, Rectange):
            return self.area < other.area
"""
"""
class City:

    def __init__(self, name: str):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return True if self.name[-1] in 'aeiou' else False
"""
"""
class Quadrilateral:

    def __init__(self, width, height=None):
        self.width = width
        self.height = (width if height is None else height)

    def __str__(self):
        return f'Квадрат размером {self.width}х{self.height}' if self.width == self.height else\
            f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return True if self.width == self.height else False
"""
"""
class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f"Вызывался {self.counter} раз")
        
    def average(self):
    return self.summa / self.length
"""
"""
from time import perf_counter

class Timer:

    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"Вызывается функция {self.fn.__name__}")
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f"Функция отработала за {finish - start}")
        return result

@Timer
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr *= i
    return pr

def gen_fib(n):
    fib = [1, 1]
    for i in range(n):
        fib.append(fib[i] + fib[i+1])
    return fib
"""
"""
class Logger:

    def __init__(self, log_file):
        self.log_file = log_file

    def __call__(self, message):
        with open(log_file, "a") as f:
            f.write(massage + '\n')


from datetime import datetime

logger = Logger('file.txt')

def get_information():
    logger(f'Start work {datetime.now()}')
    # work code
    logger(f"Finished work {datetime.now()}")
"""
"""
class QuadraticFunction:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c
"""
"""
class Addition:

    def __call__(self, *args):
        s = 0
        for i in args:
            if isinstance(i, (int, float)):
                s += i
            else:
                continue
        return f"Сумма переданных значений = {s}"


class Addition:
    
    def __call__(self, *args):
        res = sum([i for i in args if isinstance(i, (int, float))])
        return f"Сумма переданных значений = {res}"
"""
"""
from time import perf_counter

class Timer:

    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        res = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Время работы программы {finish-start}')
        return res

@Timer
def calculate():
    for i in range(10000000):
        2**100

calculate()
"""
"""
class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__area = None

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, (int, float)):
            self.__width = value
            self.__area = None

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, (int, float)):
            self.__height = value
            self.__area = None


    @property
    def get_area(self):
        if self.__area is None:
            self.__area = self.__width * self.__height
            return self.__area
        return self.__area


class Square:

    def __init__(self, width):
        self.__width = width
        self.__area = None

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, (int, float)):
            self.__width = value
            self.__area = None

    @property
    def get_area(self):
        if self.__area is None:
            self.__area = self.width * self.width
            return self.__area
        return self.__area


class Circle:

    def __init__(self, radius):
        self.__radius = radius
        self.__area = None

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if isinstance(value, (int, float)):
            self.__radius = value
            self.__area = None


    @property
    def get_area(self):
        if self.__area is None:
            self.__area = 3.14 * self.radius**2
            return self.__area
        return self.__area
"""
"""
class UnitedKingdom:

    @staticmethod
    def get_capital():
        print('London is the capital of Great Britain')

    @staticmethod
    def get_language():
        print('English is the primary language of Great Britain')

class Spain:

    @staticmethod
    def get_capital():
        print('Madrid is the capital of Spain')

    @staticmethod
    def get_language():
        print('Spanish is the primary language of Spain')
"""
"""
class Building:

    def __init__(self, floor):
        self.floor = {}
        for num in range(floor):
            self.floor[num] = None

    def __setitem__(self, key, value):
        self.floor[key] = value

    def __getitem__(self, item):
        return self.floor[item]

    def __delitem__(self, key):
        self.floor[key] = None
"""
"""
class Song:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:

    def __init__(self, songs=[]):
        self.songs = songs

    def __getitem__(self, item):
        return self.songs[item]

    def __setitem__(self, key, Song):
        self.songs.insert(key, Song)

    def add_song(self, Song):
        self.songs.append(Song)

"""
"""
class ShoppingCart:

    def __init__(self, items={}):
        self.items = items

    def __getitem__(self, item):
        return self.items.get(item, 0)

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        del self.items[key]


    def add_item(self, name, count=1):
        if name in self.items:
            self.items[name] += count
        else:
            self.items.setdefault(name, count)

    def remove_item(self, name, count=1):
        if name in self.items:
            if self.items[name] <= count:
                del self.items[name]
            else:
                self.items[name] -= count
"""
"""
class User:

    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, (int, float)):
            self.__balance = value

    def payment(self, summa):
        if summa > self.__balance:
            return 'Not many'
        self.__balance -= summa
        return 'paid'


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name}'



class Cart:

    def __init__(self, user, cart={}):
        self.user = user
        self.cart = cart
        self.__total = 0

    def add(self, product, count=1):
        if isinstance(product, Product):
            if product in self.cart:
                self.cart[product] += count
            else:
                self.cart[product] = count
            self.__total += product.price * count


    def remove(self, product, count=1):
        if isinstance(product, Product):
            if product in self.cart:
                if self.cart[product] > count:
                    self.cart[product] -= count
                else:
                    del self.cart[product]
            self.__total -= product.price * count


    @property
    def order(self):
        return self.__total


    @property
    def get_product(self):
        return self.cart


    def payment_cart(self, user):
        if isinstance(user, User):
            return user.payment(self.order)

"""
"""
class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        print('call iter')
        return iter(self.marks)

igor = Student('igor', 'Nikolaev', [1, 2, 3, 4, 5])

for i in igor:
    print(i)
"""
"""
class Mark:

    def __init__(self, value):
        self.value = value
        self.index = 0

    def __next__(self):
        print('call next')
        if self.index >= len(self.value):
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter

    def __iter__(self):
        return self



class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        print('call iter')
        self.index = 0
        return self.marks

    def __next__(self):
        if self.index >= len(self.marks):
            raise StopIteration
        letter = self.marks[self.index]
        self.index += 1
        return letter

m = Mark([1, 2, 3, 4, 5])

igor = Student('igor', 'Nikolaev', m)

for i in igor:
    print(i)
"""
"""
class FileReader:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self.file

    def __next__(self):
        self.file.readline().strip()


for line in FileReader('lorem.txt'):
    print(line)
"""
"""
class Mark:
    def __init__(self, *args):
        self.mark = args

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.mark):
            raise StopIteration
        letter = self.mark[self.index]
        self.index += 1
        return letter

for i in Mark(1,2,3,4):
    print(i)
"""
"""
class Countdown:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 0:
            raise StopIteration
        letter = self.num
        self.num -= 1
        return letter


for i in Countdown(3):
    print(i)
"""
"""
class PowerTwo:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start > self.num:
            raise StopIteration
        letter = pow(2, self.start)
        self.start += 1
        return letter


for i in PowerTwo(4):
    print(i)
"""
"""
class InfinityIterator:

    def __iter__(self):
        self.start = 0
        self.step = 10
        return self

    def __next__(self):
        start = self.start
        self.start += self.step
        return start

a = iter(InfinityIterator())
print(next(a))
"""
"""
class Iter:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step >= 0:
            if self.start > self.stop:
                raise StopIteration
            letter = self.start
            self.start += self.step
            return letter

        else:
            if self.start < self.stop:
                raise StopIteration
            letter = self.start
            self.start -= abs(self.step)
            return letter


for i in Iter(10, 0, -2):
    print(i)
"""
"""
class Person:

    def can_breathe(self):
        print('я могу дышать')

    def can_walk(self):
        print('я могу ходить')


class Doctor(Person):

    def can_cure(self):
        print('я могу лечить')


class Orthopedist(Doctor):
    pass


class Architector(Person):

    def can_build(self):
        print('я могу построить здание')
        
print(issubclass(Orthopedist, Person))
"""
"""
class Vehicle:
    pass

class Car(Vehicle):
    pass

class Plane(Vehicle):
    pass

class Boat(Vehicle):
    pass

class RaceCar(Car):
    pass
"""
"""
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    @staticmethod
    def display_info():
        print(f"Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")

class Bus(Vehicle):
    pass
"""
"""
class Person:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):

    def is_employee(self):
        return True


emp1 = Person('vasya')
print(emp1.get_name(), emp1.is_employee())
emp2 = Employee('dry')
print(emp2.is_employee())
"""
"""
class NewInt(int):

    def repeat(self, n=2):
        return int(f"{self}"*n)

    def to_bin(self):
        return int(f'{self:b}')

a = NewInt(9)
print(a.repeat())

print(a.to_bin())
"""
"""
class Square:
    def get_value(self, a):
        return a * a

class Cube(Square):
    def get_value(self, a):
        return pow(a, 3)

class Power4(Square):
    def get_value(self, a):
        return pow(a, 4)
"""
"""
class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def breathe(self):
        print('Человек дышит')

    def __str__(self):
        return f"Person {self.name} {self.surname}"

    def info(self):
        print('Parent class')
        print(self)



class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def breathe(self):
        # super().breathe()
        print('Доктор дышит')

    def __str__(self):
        return f"Doctor {self.name} {self.surname} {self.age}"


p = Person('dry', 'drytimor')
d = Doctor('doc', 'doctimor', 30)

d.breathe()
d.info()
"""
"""
class Person:

    def __init__(self, name, passport):
        self.name = name
        self.passport = passport

    def display(self):
        print(f"{self.name}: {self.passport}")



class Employee(Person):

    def __init__(self, name, passport, salary, department):
        super().__init__(name, passport)
        self.salary = salary
        self.department = department
"""
"""
class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def display(self):
        print(f"Total {self.name} fare is: {self.fare()}")



class Bus(Vehicle):

    def __init__(self, name, mileage, capacity=50):
        super().__init__(name, mileage, capacity)

    def fare(self):
        return super().fare() + super().fare()*0.10


class Taxi(Vehicle):

    def __init__(self, name, mileage, capacity=4):
        super().__init__(name, mileage, capacity)

    def fare(self):
        return super().fare() + super().fare() * 0.35
"""
"""
class Transport:

    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"

class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue, kind='Car'):
        super().__init__(brand, max_speed, kind)
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f"Осталось бензина {self.__gasoline_residue} л"

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue += value
            print(f"Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л")
        else:
            print('Ошибка заправки автомобиля')


class Boat(Transport):

    def __init__(self, brand, max_speed, owners_name, kind='Boat'):
        super().__init__(brand, max_speed, kind)
        self.owners_name = owners_name

    def __str__(self):
        return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"


class Plane(Transport):

    def __init__(self, brand, max_speed, capacity, kind='Plane'):
        super().__init__(brand, max_speed, kind)
        self.capacity = capacity

    def __str__(self):
        return f"Самолет марки {self.brand} вмещает в себя {self.capacity} людей"
"""
"""
from functools import total_ordering

@total_ordering
class Person:

    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        if isinstance(other, int):
            return self.age == other
        elif isinstance(other, Person):
            return self.age == other.age
        return

    def __lt__(self, other):
        if isinstance(other, int):
            return self.age < other
        elif isinstance(other, Person):
            return self.age < other.age
        return


class Bob(Person):

    def __init__(self, age):
        super().__init__(age)


class Rob(Person):

    def __init__(self, age):
        super().__init__(age)


bob = Bob(10)
rob = Rob(20)
"""

"""
from functools import total_ordering

@total_ordering
class Initialization:

    def __init__(self, capacity: int, food: list):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print('Количество людей должно быть целым числом')

    def __eq__(self, other):
        if isinstance(other, int):
            return self.capacity == other
        if isinstance(other, Initialization):
            return self.capacity == other.capacity
        return f'Невозможно сравнить количество {self} с {other}'


    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        if isinstance(other, Initialization):
            return self.capacity < other.capacity
        return f'Невозможно сравнить количество {self} с {other}'


class Vegetarian(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"


class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"


class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}"

rob = Vegetarian(10, 'as')
bob = MeatEater(20, 'asd')
rob = SweetTooth(30, 'tre')
"""
"""
class Doctor:

    def __init__(self, name, degree):
        self.name = name
        self.degree = degree


    @property
    def graduate(self):
        return 'я доктор'

    @property
    def can_work(self):
        return 'я умею лечить'


class Builder:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def graduate(self):
        return 'я строитель'

    @property
    def can_work(self):
        return 'я умею строить'


class Person(Doctor, Builder):
    def __init__(self, name, degree, rank):
        super().__init__(name, degree)
        Builder.__init__(self, name, rank)

    @property
    def graduate(self):
        return Builder.graduate(self)

    def __str__(self):
        return f"Я человек и {self.can_work}, {self.graduate}"
"""
"""
class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_info(self):
        return f"Имя пользователя: {self.name}"


class Authentication:

    def authenticate(self, name, password):
        return True if self.name == name and self.password == password else False


class AuthenticatedUser(Authentication, User):
    pass
"""
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Person: {self.name}, {self.age}")

class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f"Company: {self.company_name}, {self.location}")


class Employee(Person, Company):
    def __init__(self, name, age, company_name, location):
        super().__init__(name, age)
        Company.__init__(self, company_name, location)
"""
"""
class O: ...
class A(O): ...
class B(O): ...
class C(O): ...
class D(O): ...
class E(O): ...
class K1(C, A, B): ...
class K2(A, D): ...
class K3(B, D, E): ...
class Z(K1, K2, K3): ...
print(Z.mro())
"""
"""
class First(object):
    def __init__(self):
        print("First(): entering")
        super(First, self).__init__()
        print("First(): exiting")


class Second(object):
    def __init__(self):
        print("Second(): entering")
        super(Second, self).__init__()
        print("Second(): exiting")


class Third(First, Second):
    def __init__(self):
        print("Third(): entering")
        super(Third, self).__init__()
        print("Third(): exiting")


Third()
"""
"""
class BasePizza:

    BASE_PRICE = 20

    def __init__(self, name, price=BASE_PRICE):
        self.name = name
        self.price = price
        self.toppings = ['cheese']

    def __str__(self):
        return f"{self.name} with {self.toppings}, ${self.price:.2f}"


class PepperoniMixin:
    def add_pepperoni(self):
        self.price += 3
        self.toppings += ['pepperoni']
        print('Adding pepperoni!')


class MushroomMixin:
    def add_mushrooms(self):
        self.price += 5
        self.toppings += ['mushroom']
        print('Adding mushroom!')


class OnionMixin:
    def add_onion(self):
        self.price += 8
        self.toppings += ['onion']
        print('Adding onion!')


class PepperoniPizza(BasePizza, PepperoniMixin):

    def __init__(self):
        super().__init__('Колбасятина')
        self.add_pepperoni()

pizza = PepperoniPizza()
print(pizza)
"""
"""
class HamMixin:
    def add_ham(self):
        print('Adding ham!')
        self.price += 7
        self.toppings += ['ham']

class PepperMixin:
    def add_pepper(self):
        print('Adding pepper!')
        self.price += 3
        self.toppings += ['pepper']

class Chicken:
    def add_chicken(self):
        print('Adding chicken!')
        self.price += 5
        self.toppings += ['chicken']
"""
"""
class PermissionMixin:
    def __init__(self):
        self.permission = set()

    def grant_permission(self, permission):
        self.permission.add(permission)

    def revoke_permission(self, permission):
        self.permission.discard(permission)

    def has_permission(self, permission):
        return True if permission in self.permission else False

class User(PermissionMixin):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email
"""
"""
class DictMixin:

    def to_dict(self):
        d = {}
        for key, value in self.__dict__.items():
            if isinstance(value, DictMixin):
                d[key] = value.__dict__
            elif isinstance(value, list):
                d[key] = [DictMixin.to_dict(i) for i in value]
            else:
                d[key] = value
        return d

class DictMixin2:
    def __repr__(self):
        return str(self.__dict__)

    def to_dict(self):
        return eval(self.__repr__())

class Phone(DictMixin2):
    def __init__(self, number):
        self.number = number


class Person(DictMixin2):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address(DictMixin2):
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Company(DictMixin2):
    def __init__(self, name, address):
        self.name = name
        self.address = address

address = Address("123 Main St", "Albuquerque", "NM", "987654")
walter = Person("Walter White", 30, address)
walter_phone = Phone("555-1234")
walter.phone = walter_phone

jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
jesse.phone = Phone("555-5678")

fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
fring.friends = [walter, jesse]
print(fring.to_dict())
"""
"""
class Person:

    __slots__ = ['first_name', 'last_name', 'age']

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"
print(dry.name)
"""
"""
class Rectangle:

    __slots__ = '__width', 'height'

    def __init__(self, x, y):
        self.width = x
        self.height = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value


    @property
    def area(self):
        return self.__width * self.height

a = Rectangle(2,2)
a.width = 3
print(a.width)
print(a.area)
"""
"""
class Device:

    __slots__ = '_name', '_location', '_status'

    def __init__(self, name, location, status='ON'):
        self._name = name
        self._location = location
        self._status = status

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def turn_on(self):
        self._status = 'ON'

    def turn_off(self):
        self._status = 'OFF'


class Light(Device):
    __slots__ = '_brightness', '_color'

    def __init__(self, brightness, color, name, location):
        super().__init__(name, location)
        self._brightness = brightness
        self._color = color


    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        self._brightness = value

    @property
    def color(self):
        return self._color


class Thermostat(Device):
    __slots__ = '_current_temperature', '_target_temperature'

    def __init__(self, current_temperature, target_temperature, name, location):
        super().__init__(name, location)
        self._current_temperature = current_temperature
        self._target_temperature = target_temperature

    @property
    def current_temperature(self):
        return self._current_temperature

    @current_temperature.setter
    def current_temperature(self, value):
        self._current_temperature = value

    @property
    def target_temperature(self):
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, value):
        self._target_temperature = value


class SmartTV(Device):
    __slots__ = '_channel'

    def __init__(self, channel, name, location):
        super().__init__(name, location)
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
"""
"""
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class SalariedEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary
"""
"""
from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass


class MySQLDatabase(Database):

    def connect(self):
        print('Connecting to MySQL database...')

    def disconnect(self):
        print('Disconnecting from MySQL database...')

    def execute(self, query):
        print(f"Executing query '{query}' in MySQL database...")


class PostgreSQLDatabase(Database):

    def connect(self):
        print('Connecting to PostgreSQL database...')


    def disconnect(self):
        print('Disconnecting from PostgreSQL database...')


    def execute(self, query):
        print(f"Executing query '{query}' in PostgreSQL database...")
"""
"""
class Wallet:

    def __init__(self, currency: str, balance: int):

        if not isinstance(currency, str):
            raise TypeError('Неверный тип валюты')
        if len(currency) != 3:
            raise NameError('Неверная длина названия валюты')
        if not currency.isupper():
            raise ValueError('Название должно состоять только из заглавных букв')

        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")
        if self.currency != other.currency:
            raise ValueError('Нельзя сравнить разные валюты')
        else:
            return self.balance == other.balance

    def __add__(self, other):
        if isinstance(other, Wallet):
            if self.currency == other.currency:
                new_balance = self.balance + other.balance
                return Wallet(self.currency, new_balance)
        raise ValueError('Данная операция не разрешена')

    def __sub__(self, other):
        if isinstance(other, Wallet):
            if self.currency == other.currency:
                new_balance = self.balance - other.balance
                return Wallet(self.currency, new_balance)
        raise ValueError('Данная операция не разрешена')
"""
"""
try:
    a + b
except Exception as ex:
    print(ex.__class__.__name__)
"""
"""
try:
    a = int(input())
    b = int(input())
except ValueError:
    print('Введите корректные значения')
else:
    try:
        print(f"Результат деления a на b: {a/b}")
    except ZeroDivisionError:
        print('Введите корректные значения')
"""
"""
try:
    a = int(input())
    b = int(input())
    print(f"Результат деления a на b: {a/b}")
except (ValueError, ZeroDivisionError):
    print("Введите корректные значения")
"""
"""
try:
    a = int(input())
    b = int(input())
    print(f"Результат деления a на b: {a/b}")
except ValueError:
    print('Введите целое число')
except ZeroDivisionError:
    print("Делитель не должен быть равен нулю")
"""
"""
try:
    file = open('pentagon_secrets.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print('Эх, не судьба тайны пентагона узнать')"""
"""
try:
    def func(phrase):
       func(phrase)
    func('Это рекурсия, детка!')
except RecursionError:
    print('Кто-то должен остановить это безумие')

"""
"""
class CustomButton:

    def __init__(self, text, **kwargs):
        self.text = text
        self.config(**kwargs)

    def config(self, **kwargs):
        self.__dict__.update(kwargs)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print('Кнопка не настроена')
        except TypeError:
            print('Кнопка сломалась')
"""
"""
class Customer:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(value):
        if not isinstance(value, (int, float)):
            raise TypeError('Банк работает только с числами')


    def withdraw(self, value):
        self.check_type(value)
        if self.balance >= value:
            self.balance -= value
        else:
            raise ValueError('Сумма списания превышает баланс')

    def deposit(self, value):
        self.check_type(value)
        self.balance += value
"""
"""
def sum_numbers(numbers: list):
    if not isinstance(numbers, list):
        raise TypeError('Аргумент numbers должен быть списком')
    if len(numbers) <= 0:
        raise ValueError("Пустой список")
    any(not isinstance(n, (int, float)) for n in numbers)

"""
"""
from dataclasses import dataclass, field

@dataclass(order=True)
class Person:

    name: str = field(compare=False)
    age: int

a = Person('name', 10)
c = Person('dry', 11)

print(a > c)
"""















