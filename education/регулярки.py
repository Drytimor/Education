import re
"""
line = r"Последовательность \n используется для переноса строк"
print(line) Последовательность \n используется для переноса строк
"""
"""
a, b = int(input()), int(input())
print(rf"{a}\n + \n{b}\n = \n{a+b}")
"""
"""
r = r"[A-Za-zА-Яа-яёЁ]{2,}"
МГИМО ВШЭ ХГФ
"""
"""
r = r"[авекмнорстух][\d]{3}[авекмнорстух]{2}[\d]{2,3}\b"

r = r"-?\d{1,3}.\d+ -?\d{1,3}.\d+$"

"""
"""
coord = r"-?\b\d{1,3}\.\d+"

regex = fr"{coord} {coord}" 16.874124 -24.984161
"""
"""
regex = r"0x[A-Fa-f\d] {40}"
"""
"""
r = r"http[s]?"
"""
"""
r = r"[IVXLCDM]+"

r = r"[:8;¦=][\^-]?[|\\0()/PODIC]"

r = r"\d+?"

r = "[1-9]+?[02468]"

r = r"\[.\]*?"

r = r"[A-Za-zА-Яа-яёЁ].*?[A-Za-zА-Яа-яёЁ]"

r = r'\".+?\"'

r = "<img.*?>"

r = r"(?P<three>\d{3})(?P=three)"

r = r"(?P<repeat>[а-яёЁ]-?P=repeat"

r = r"([a-z]{4})\1"

r = r"(?<two>[A-Za-zА-Яа-яёЁ]{2})(?P=two)"

r = r"/d{2}\1"
"""

"""
r = r"^(<)?(?(1)if|)?(?(1)>|)"
r = r'^(<)?if(?(1)>|)$'

r = r"(?<=\[\^START\]).*?(?=\{\(END\.\)\})"

r = r"(?<!/)/+?(?!/)"

r = r"(?<!x)(?:[x]{2})(?!x)"

r = r"\b(?:xx)+\b"

r = r"(?<=[^\.]\s)[А-ЯЁ][а-яё]+"

r = r"(-)?(?(1)|\d)"
"""
"""
r = r"JavaScript|C\+\+|Python"

r = r"\b([Дд]а|[Нн]ет|[Нн]аверное)\b"

r = r"(?:Привет|Пока), (?:Олег|Григорий)"

r = r"(1|3|bc1)[A-Za-z1-9]{24,34}"

r = r"(я|ты|он|он[аи]|мы|вы|)|(готов готов[аы])"

r = r"\b(?<!\.)1(?!\.)\b|\b(0\.)?(?(1)\d{1,2}\b|(?<!\.)0(?!\.))\b"

r = r"\b[а-яА-ЯёЁ]*а+[а-яА-ЯёЁ]*\b"

r = r"[а-яА-ЯёЁ]*\S+[а-яА-ЯёЁ]*"

r = "^[а-яА-ЯёЁ\-]*"

r = r"^(n|N)[A-Za-z]"

r = r"(?<=[a-z])[a-z]+"
"""

"""
text = "Еда, беду, победа"
match = re.findall(r"[еЕ]д[ау]", text)
print(match)
['Еда', 'еду', 'еда']
"""
"""
text = "Еда, беду, 55, победа"
match = re.findall(r"[\d]+", text)
print(match)
['55']
"""
"""
text = "Еда, беду, 55, победа"
match = re.findall(r"[\d]{1}", text)
print(match)
"""
"""
text = "author=Пушкин А.С.; title = Евгений Онегин; " \
       "price =200; year= 2001"
match = re.findall(r"(\w+)\s*=\s*([^;]*)", text)
print(match)
[('author', 'Пушкин А.С.'), ('title', 'Евгений Онегин'), 
 ('price', '200'), ('year', '2001')]
"""
"""
text = "<p>Картинка <img scr='bg.jpg'> в тексте</p>"
match = re.findall(r"<img.*?>", text)
print(match)
["<img scr='bg.jpg'>"]
"""
"""
text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text)
print(match)
["<img src='bg.jpg'>"]
"""
"""
r = r"П.+?т"
text = 'Привет, как тебя зовут?'
match = re.match(r, text)
print(match)
<re.Match object; span=(0, 6), match='Привет'>
"""
"""
r = r"П.+?т"
text = 'Привет, как тебя зовут?'
match = re.match(r, text)
print(match.group(0))Привет
print(match[0])Привет
print(match.start(0)) 0
print(match.end(0)) 6
print(match.span(0)) (0, 6)
"""
"""
r = r"П.+?т"
text = 'Привет, как тебя зовут?'
match = re.match(r, text)
print(match.pos)  # pos - это позиция, с которой функция начинает искать совпадения.
print(match.endpos)  # endpos - это позиция, до которой функция ищет совпадения.
print(match.re) #re.compile('П.+?т')
print(match.string) Привет, как тебя зовут?
"""
"""
def hashtag(line: str):
    match = re.search(r"#[a-z]+", line)
    if match:
        print(match.group(0))
line = input()
hashtag(line)
"""
"""
def password():
    reg = r"[Кк]од"
    for elem in range(1,5):
        match = re.search(reg, input())
        if match:
            return f"{elem} {match.start()}"
    return "код не найден"
print(password())
"""
"""
def key():
    reg = r"(?<=Activation key:)\s([A-Z\d]{5}-){4}[A-Z\d]{5}"
    match = 0
    while not match:
        match = re.search(reg, input())
    print(match.group(0))
key()
"""
"""
def json():
    reg = r"t=0[\d.+]+"
    match = re.search(reg, input())
    if match:
        print(match.group(0))
json()
"""
"""
def one_word():
    reg = r"[A-Z-a-z]+"
    match = re.match(reg, input())
    if match:
        print(f"Первое слово в предложении: {match.group(0)}")
one_word()
"""
"""
def seed_phrase(line: str):
    reg = r"\b([a-z]+\s){11}[a-z]+\b"
    match = re.match(reg, line)
    if match:
        print("возможно, это seed-фраза")

line = input()
seed_phrase(line)
"""
"""
def mail(address: str):
    reg = r"(\w*)[^@]"
    match = re.match(reg, address)
    if match:
        print(match.group(0))

address = input()
mail(address)
"""
"""
def card_number(num:str):
    reg = r"[\d]{13,}"
    match = re.fullmatch(reg, num)
    if match:
        print(match.group(0)==num)
    else:
        print(False)
num = input()
card_number(num)
"""
"""
def check_password(password: str):
    reg = r"[a-zA-Z\d@#$%^&*()_+!?-]{8,}"
    match = re.fullmatch(reg, password)
    if match:
        print(True)
    else:
        print(False)
password = input()
check_password(password)
"""
"""
def num_phone(num: str):
    reg = r"\+?[\d]{1,3}\s{0,2}\(?[\d]{3}\)?\s{0,2}[\d]{3}[\s\-]{0,2}[\d]{2}[\s\-]{0,2}[\d]{2}[\s\-]{0,2}"
    reg1 = r'^(?:[87]|\+7)(?:[ \-()]*\d){10}'
    match = re.fullmatch(reg, num)
    print(True if match else False)
num = input()
num_phone(num)
"""
"""
def get_count(sentence):
    reg = r"[aeiou]"
    match = re.findall(reg, sentence)
    return len(match)
sentence = input()
print(get_count(sentence))
"""
"""
def iter_reg(word: str):
    rex = r"[\w][^\s\.\W]*"
    match = re.finditer(rex, word)
    for elem in match:
        print(elem.group())
word = input()
iter_reg(word)
"""
"""
def five_letter(line: str):
    reg = r"\b[A-Za-zА-Яа-яёЁ]{5}\b"
    match = re.finditer(reg, line)
    for elem in match:
        print(elem.group())
line = input()
five_letter(line)
"""
"""
def pars_bank(line:str):
    reg = r"[\d\,]+ ₽"
    match = re.finditer(reg, line)
    for elem in match:
        print(elem.group())
line = input()
pars_bank(line)
"""
"""
def personal_files(line: str):
    reg = r"https://imgur.com/[a-zA-z\d]{7}"
    match = re.findall(reg, line)
    for elem in match:
        print(elem)
line = input()
personal_files(line)
"""
"""
def mail_search(line: str):
    reg = r"\b[a-zA-Z\d\_\-]+@[a-zA-Z\d]+\.[ru|com]\b"
    match = re.findall(reg, line)
    for elem in match:
        print(elem)
line = input()
mail_search(line)
"""
"""
def date_search(line: str):
    reg = r"\d{2}([./])\d{2}\1\d{4}|\d{4}([./])\d{2}\2\d{2}"
    match = re.finditer(reg, line)
    for elem in match:
        print(elem.group())
line = input()
date_search(line)
"""
"""
def date_search(line: str):
    reg = r"([\d]{2}(?P<a>[/.])[\d]{2}(?P=a)[\d]{4}|[\d]{4}(?P<b>[/.])[\d]{2}(?P=b)[\d]{2})"
    match = re.findall(reg, line)
    for elem in match:
        print(elem[0])
line = input()
date_search(line)
"""
"""
def valid_time(line:str):
    reg = r"[0-2]\d(?<!2[4-9]):\d(?<![6-9])\d"
    for elem in re.findall(reg, line):
        print(elem)
line = input()
valid_time(line)
"""
"""
def teg_a(line: str):
    reg = r"<a.+?a>"
    reg1 = r"(?<=href=[\"\']).+?(?=[\"\'])"
    for match in re.findall(reg, line):
        print(*re.findall(reg1, match))
line = input()
teg_a(line)
"""
"""
def teg_a(line: str):
    reg = r"<a.+?href=\"(.+?)\""
    for match in re.findall(reg, line):
        print(match)
line = input()
teg_a(line)
"""
"""
def sentence(line: str):
    reg = r"[.!?]"
    print(re.split(reg, line))
line = input()
sentence(line)
"""
"""
def split_words(line: str):
    reg = r"[.?!,\s]"
    print(re.split(reg, line))
line = input()
split_words(line)
"""
"""
def data_base(line: str):
    reg = r"Категория:\s[а-яА-Я\s]+\\n"
    print(re.split(reg, line))
line = input()
data_base(line)
"""
"""
def data_base(line: str):
    reg = r"Категория:\s[А-Яа-я\s\\n]+([A-Za-z\s\d\\n]+)"
    for match in re.findall(reg, line):
        print(match)
line = input()
data_base(line)
"""
"""
def remove_vowels(line: str):
    reg = r"[aeioyuAEIOUауоыиэяюёеАУОЫИЭЯЮЁЕ]"
    replase = "!"
    print(re.sub(reg, replase, line))
line = input()
remove_vowels(line)
"""
"""
def remove_tag(line: str):
    reg = r"<.+?>"
    replace = ""
    print(re.sub(reg, replase, line))
line = input()
remove_tag(line)
"""
"""
def replace_name():
    surname, name, och = map(lambda x: x[:-1], input().split())
    print(surname, name, och)
    line = input()
    print(surname, name, och)
    reg = fr"({surname}[а-я]* {name[0]}. {och[0]}.)|({surname}[а-я]* {name}[а-я]* {och}[а-я]*)"
    replace = "ФИО"
    print(re.sub(reg, replace,line))
replace_name()
"""
"""
def remove_text(line):
    reg = r"[.?!,:]"
    replace = ''
    print(re.subn(reg, replace, line)[1])
line = input()
remove_text(line)

def remove_text(line):
    reg = r"\d"
    replace = 'X'
    print(re.subn(reg, replace, line))
line = input()
remove_text(line)
"""
"""
reg = r"<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !"#$%&\'()*+,-./0123456789:;"
print(re.escape(reg))
"""
"""
def search_teg(line: str):
    reg = r"<p.*?>([\w\W]*?)</p>"
    match = re.findall(reg, line)
    for elem in match:
        print(elem)
line = input()
search_teg(line)
"""

"""
def divide(line):
    reg = r"http[s]*.?\S+"
    reg1 = r"(http[s]*)://([a-z\.]*)[a-z\d\-_/]*(\?[a-z=&\d]*)*(#[a-z]*)*"
    match = re.findall(reg, line)
    for elem in match:
        match = re.search(reg1, elem)
        print(f""""Полная ссылка: {elem}"
"Протокол: {match[1]} | Домен: {match[2]} | Параметры: {match[3]} | Якорь: {match[4]}"
"""")
line = input()
divide(line)
"""
"""
def divide(line):
    reg1 = r"(http[s]?)+://([a-z.]+)/[a-z\d\-_/]*(\?[a-z=&\d]*)*(#[a-z]*)*"
    for match in re.finditer(reg1, line):
        print(f""""Полная ссылка: {match[0]}"
"Протокол: {match[1]} | Домен: {match[2]} | Параметры: {match[3]} | Якорь: {match[4]}"
"""")
line = input()
divide(line)
"""

email = r"[\w\d]*[._-]*[\w\d]*@{1}\w+\.{1}[\w]{2,6}"

number = r"^(\+7|8)+[\s\-\(]*[\d]{3}[\)\-\s]*[\d]{3}[\-\s]*[\d]{2}[\s\-]*[\d]{2}$"
















