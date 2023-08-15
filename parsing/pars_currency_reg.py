import re
import requests
import sqlite3 as sq
from my_module import download_file as df
import xml.etree.ElementTree as ET



def pars_currency():
    """Парсит XML и записывает в БД"""
    regex = re.compile(r"<CharCode>(.+?)</CharCode>.*?<Value>(.+?)</Value>")

    with open("../package_1/xml_currency.xml", "r") as file:
        dict_currency = {elem[0]: float(elem[1].replace(',', '.')) for elem in regex.findall(file.read())}
        try:
            with sq.connect("../package_1/currency.bd") as con:
                cur = con.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS currency (
                id_name INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                value REAL
                )""")
                cur = con.cursor()
                for name, value in dict_currency.items():
                    cur.execute(f"INSERT INTO currency (name, value) VALUES ('{name}', {value})")
        except:
            print("Error BD")



def read_xml(path: str):
    """Читает документ и возвращает словарь с данными"""
    regex = re.compile(r'<Valute ID\=\"([\dA-Z]+)\">.+?<CharCode>(.+?)</CharCode>.+?<Value>(.+?)</Value>')
    dict_currency = {}
    try:
        with open(path, "r") as file:
            for elem in regex.findall(file.read()):
                res = {
                    elem[1]: {
                        "Valute": elem[0],
                        "name": elem[1],
                        "value": elem[2]
                    }
                }
                dict_currency = dict_currency | res

    except:
        print("Error file_1")
    finally:
        return dict_currency


def write_xml(dict_: dict):
    """Принимает словарь и создает новый XML документ"""
    try:
        with open("../package_1/currency.xml", 'w') as file:

            valcurs = ET.Element("ValCurs")
            valcurs.set("Date", "07.07.2023")
            valcurs.set("name", "my_xml_currency")
            for name, value in dict_.items():
                valute = ET.SubElement(valcurs, "Valute")
                valute.set("ID", f"{value['Valute']}")
                name = ET.SubElement(valute, 'name').text = f"{value['name']}"
                value = ET.SubElement(valute, 'value').text = f"{value['value']}"
                data = ET.tostring(valcurs, encoding='unicode')
            file.write(data)

    except:
        print("Error file_2")





if __name__ == "__main__":
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v16128205146 t2375925855354670132 athfa3c3975 altpub cvcv=2 smf=0"}
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    path = df.get_download_xml(url, headers, "../package_1", "xml_currency.xml")
    dict_currency = read_xml(path)
    write_xml(dict_currency)








