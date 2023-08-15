import urllib.request
import xml.etree.ElementTree as ET
import re
from lxml import etree



def get_download_file(url_xml: str):
    xml_file = urllib.request.urlopen(url_xml).read()
    try:
        with open("../package_1/xml_currency.xml", "wb") as file:
            file.write(xml_file)
    except:
        print("Error file")
        pass


def get_currency_dict(name):
    currency_dict = {}
    tree = ET.parse(name)
    root = tree.getroot()

    for elem in root.findall("Valute"):
        value = elem.findtext("Value")
        charCode = elem.findtext("CharCode")
        currency_dict.setdefault(charCode, float(value.replace(',', '.')))
    return currency_dict

def reg_search():
    dict_currency = {}
    text = input()
    reg_1 = r"<CharCode>(.+?)</CharCode>.+?<Value>(.+?)</Value>"
    name = re.findall(reg_1, text)
    name = dict(name)

    return name




if __name__ == "__main__":
    url_xml = "http://www.cbr.ru/scripts/XML_daily.asp"
    name_file = "../package_1/xml_currency.xml"
    # get_download_file(url_xml)
    print(reg_search())


















