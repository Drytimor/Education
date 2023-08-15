import requests
from bs4 import BeautifulSoup
from time import sleep
from transliterate import translit

headers = {
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v16128205146 t2375925855354670132 athfa3c3975 altpub cvcv=2 smf=0"
  }


def translates():
    name_film_ascii = translit(input("Назови фильм: ")
                               .replace(" ", "-").replace("ё", "yo")
                               .replace("я", "ya").replace("ю", "y")
                               .replace(".", "").replace("ц", "c")
                               .replace("й", "y").replace("ь", ""), reversed=True)
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



def main():
    result()

if __name__ == "__main__":
    main()













