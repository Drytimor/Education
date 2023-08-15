from bs4 import BeautifulSoup
import urllib.request
import requests
import sqlite3 as sq

headers = {
    "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v16128205146 t2375925855354670132 athfa3c3975 altpub cvcv=2 smf=0"
}


def get_download_xml(url):
    """Получает URL и записывает текст файла в директорию"""
    response = requests.get(url, headers=headers).text
    try:
        with open("../package_1/html_file.html", "w") as file:
            file.write(response)
    except:
        print("Error file")


def pars_xml():
    try:
        with open("../package_1/xml_currency.xml", "rb") as file:
            xml_file = file.read()
            soup = BeautifulSoup(xml_file, "xml")
            parents = soup.find_all("Valute")
            dict_ = {}
            for elem in parents:
                name = elem.find("CharCode").text
                value = elem.find("Value").text
                dict_.setdefault(name, float(value.replace(",", ".")))
            return dict_
    except:
        print("Error file")


def get_bd():
    with sq.connect("../package_1/currency.bd") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS currency (
        name TEXT,
        Value REAL
        )""")
    pass

def bd_entry(dict_: dict):
    with sq.connect("../package_1/currency.bd") as con:
        cur = con.cursor()
        for name, value in dict_.items():
            cur.execute(f"INSERT INTO currency VALUES ('{name}', {value})")




if __name__ == "__main__":
    url = "http://www.vseinstrumenti.ru/product/akkumulyatornyj-gajkovert-aeg-bss-18c12z-li-402c-4935446456-757889/"
    name_file = "../package_1/xml_currency.xml"
    # get_download_xml(url)
    # get_bd()
    # bd_entry(pars_xml())



