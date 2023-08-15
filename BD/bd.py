import sqlite3 as sq


"""
# тип данных

NULL значение NULL 
INTEGER целое число
REAL вещественное число
TEXT строка
BLOB двоичные данные (изображения)

# команды
con = sq.connect() # Создание БД # name.bd

cur = con.cursor() # Класс курсор для работы с БД

cur.execute("""""") запрос для работы с БД

"CREATE TABLE IF NOT EXISTS users" создание таблицы и имя (если она не существует)
    name TEXT,
    sex INTEGER,
    old INTEGER,
    score INTEGER

"DROP TABLE IF EXISTS users" удаление таблицы если она существует

INSERT INTO users (name, sex, old, score) VALUES ("andrey", 1, 25, 100)  # добавление записи в таблицу

SELECT name, sex, old, score FROM users   # выборка данных из таблиц
WHERE score < 100  # условие
WHERE old > 25 AND score < 100
AND
OR
NOT
IN
NOT IN

ORDER BY сортировка по возсростанию + DESC по убыванию

LIMIT ограничение LIMIT 5, LIMIT 3, 5  # 5 после первых 3
# ограничители

NOT NUll поле должно быть заполнено
DEFAULT 1 поле заполняется по умолчанию = 1
PRIMARY KEY содержит уникальное значение

"""



with sq.connect("currency.bd") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    sex INTEGER,
    old INTEGER,
    score INTEGER
    )""")
    cur.execute("INSERT INTO users VALUES ('andrey', 1, 25, 100)")



with sq.connect("currency.bd") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    for elem in result:
        print(elem)

        # ('andrey', 1, 25, 100)
        # ('andrey', 1, 25, 100)
        # ('andrey', 1, 25, 100)


