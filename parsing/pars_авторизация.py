from requests import Session
from bs4 import BeautifulSoup

headers = {"User-Agent": "CrookedHands/2.0 (EVM x8), CurlyFingers20/1;p"}

work = Session()


work.get(r"http://quotes.toscrape.com/", headers=headers)

response = work.get(r"http://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")
token = soup.find("form").find("input").get("value")

data = {"csrf_token": token, "username": "nona me", "password": "password"}

result = work.post(r"http://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)


"""
result = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")

if len(result) != 0:
    #проверка пустой страницы
else:
    break
"""


