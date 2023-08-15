"""
with open(r"/Users/andrejoveskov/PycharmProjects/dictionar/Чтение файлов/venv/package_1", "r") as file:
    text = file.read()
    name = []
    city = []
    reg = r"(?:<name>|<city>)(.+)(?:</name>|</city>)"
    match = re.findall(reg, text)
    print(match)
"""
"""
with open(r"/Users/andrejoveskov/PycharmProjects/dictionar/Чтение файлов/venv/package_1", "r") as file:
    name = []
    city = []
    reg = r"(?:<name>)(?P<name>.+)(?:</name>)"
    reg2 = r"(?:<city>)(?P<city>.+)(?:</city>)"
    for text in file:
        match_name = re.search(reg, text)
        match_city = re.search(reg2, text)
        if match_name:
            dict_name = match_name.groupdict()
        if match_city:
            dict_city = match_city.groupdict()
            if "city" in dict_city and "name" in dict_name:
                name.append(dict_name["name"])
                city.append(dict_city["city"])
print(city, name)
"""
"""
with open(r"/Users/andrejoveskov/PycharmProjects/dictionar/Чтение файлов/venv/package_1", "r") as file:
    text = file.read()
    reg_name = r"(?:<name>)(.*)(?:</name>)"
    reg_city = r"(?:<city>)(.*)(?:</city>)"
    name = re.findall(reg_name, text)
    city = re.findall(reg_city, text)
    print(name, city)
"""
"""
def create_file_with_numbers(n: int) -> None:
    file = open(f"range_{n}.txt", "a", encoding="utf-8")
    for elem in range(1, n+1):
        file.write(f"{elem}\n")
create_file_with_numbers(3)
"""
"""
from string import punctuation
import re
def longest_word_in_file(file_name: str) -> str:
    file = open(file_name, 'r', encoding="utf-8")
    reg = fr"[{punctuation}\n]"
    replace = r" "
    text = file.read()
    text = re.sub(reg, replace, text).split(replace)
    text = sorted(text, key=lambda x: len(x))
    return text[-1]
print(longest_word_in_file(r"/Users/andrejoveskov/PycharmProjects/dictionar/Чтение файлов/venv/lib/Text_1"))
"""
"""
import re
html_file = "/Users/andrejoveskov/PycharmProjects/dictionar/Чтение файлов/package_1/html_file.html"
with open(html_file, "r", encoding="utf-8") as file:
    text = file.read()
    reg = r"<p.*?>(.*?)</p>"
    match = re.findall(reg, text)
    if match:
        for elem in match:
            print(elem)
"""
"""
def link_split(link_file: str):

    with open(link_file, "r", encoding="utf-8") as file:

        reg = r"(http[s]?)+://([a-z.]+)/[a-z\d\-_/]*(\?[a-z=&\d]*)*(#[a-z]*)*"
        text = file.read()

        for match in re.finditer(reg, text):
            print(f"Полная ссылка: {match[0]} Протокол: {match[1]} | Домен: {match[2]} | Параметры: {match[3]} | Якорь: {match[4]}")

link_split("/Users/andrejoveskov/PycharmProjects/dictionar/Чтение файлов/package_1/txt_file.txt")
"""
"""
def search_teg(link_file: str):
    with open(link_file, "r") as file:
        reg = r""
        text = file.read()
        match = re.findall(reg, text)
        print(match)


link_file = input()
search_teg(link_file)
"""




