import requests
from bs4 import BeautifulSoup
from time import sleep
"""
list_card_url = []
headers = {"User-Agent": "macOS"}

# цикл для 7 страниц сайта
for count in range(1, 8):

    sleep(1)
    # url страницы со счетчиком count для каждой страницы
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
# с помощью get получаем HTML код каждой страницы
    response = requests.get(url, headers=headers)
# разбираем ее парсером
    soup = BeautifulSoup(response.text, "lxml")
# получаем список из HTML кодов каждой карточки товара
    data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
# проходим по всем ссылкам карточек товара и заносим в список
    for elem in data:
# получаем список из ссылок на карточки товаров
        card_url = "https://scrapingclub.com" + elem.find("a").get("href")
        list_card_url.append(card_url)


# получаем HTML код каждой карточки
for card_url in list_card_url:
    response = requests.get(card_url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find("div", class_="card mt-4 my-4")

    name = data.find("h3", class_="card-title").text
    price = data.find("h4").text
    text = data.find("p", class_="card-text").text
    url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
    print(name+"\n"+price+"\n"+text+"\n"+url_img+"\n")
"""
# все отзывы <div id="editorReviews">
# все карточки отзывов <div class="jrReviewListDetail">
# карточка <div class="jr-layout-outer jrEditorReviewPanel">
# текст отзыва <p>

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36 RuxitSynthetic/1.0 v1314323690 t416736650546360688 athccb4ad0b altpub cvcv=2 smf=0"
  }

response = requests.get("http://httpbin.org/headers", headers=headers)
print(response.text)
