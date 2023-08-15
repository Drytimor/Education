"""
import requests
from bs4 import BeautifulSoup
from time import sleep
from transliterate import translit"""
"""
headers = {
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v16128205146 t2375925855354670132 athfa3c3975 altpub cvcv=2 smf=0"
  }


def translates():
    name_film_ascii = translit(input("Назови фильм: ").replace(" ", "-"), reversed=True)
    return name_film_ascii


def gets_page_url():

    url = "https://www.megacritic.ru/film/" + translates()

    response = requests.get(url, headers=headers)

    return response


def parsing_page():
    soup = BeautifulSoup(gets_page_url().text, "lxml")
    sleep(3)
    data = soup.find_all("div", class_="jr-layout-outer jrEditorReviewPanel")
    for review_iter in data:
        yield review_iter



def result():
    for elem in parsing_page():
        sleep(3)
        name = elem.find("div", class_="jrReviewTitle").text
        sleep(3)
        review = elem.find("div", class_="description jrReviewComment").text
        review_source = elem.find("a").get("href")
        print(f"{name}\n{review}\n{review_source}")
        get_input = input()
        if get_input == "+":
            continue

    print("Это все что есть")
    result()

result()
"""
"""
import requests

url = 'https://scrapingclub.com/exercise/ajaxdetail/'
response = requests.get(url).json()

print(response['title'])
print(response['price'])
print(response['description'])
"""
"""
from requests import Session
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import random


ua = UserAgent()
base_url = 'https://scrapingclub.com/exercise/list_infinite_scroll/'

headers = {'user-agent': ua.random}


def main(base_url:str):
    s = Session()
    s.headers.update(headers)
    count = 1
    pagination = 0

    while True:

        if count > 1:
            url = base_url + f'?page={count}'

        else:
            url = base_url
        response = s.get(url)
        # with open('data.html', 'a', encoding='utf-8') as f:
        #     f.write(response.text)
        soup = BeautifulSoup(response.text, 'lxml')

        if count == 1:
            pagination = int(soup.find('ul', class_="pagination invisible").find_all('li', class_='page-item')[-2].text)

        cards = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")

        for card in cards:
            name = card.find('h4', class_='card-title').text
            price = card.find('h5').text
            print(name, price)

        print(count)
        time.sleep(random.choice([5, 7, 9]))
        if count == pagination:
            break
        else:
            count += 1

"""


import json
dict_ = {
    'name': 'andrey',
    'gendr': 'men',

}

dict_1 = {
    'param': 123
}

with open('../package_1/chern.json', 'a') as file:
    json.dump(dict_1, file, indent=4, ensure_ascii=False)