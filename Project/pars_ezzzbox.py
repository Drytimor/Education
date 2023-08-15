import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import time


ua = UserAgent()

headers = {'User-Agent': ua.random}
url = 'https://ezzzbox.ru'
def get_url():

    url_smart = 'https://ezzzbox.ru/catalog/smartfony/'

    response = requests.get(url_smart, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find('div', class_='row margin0 flexbox').find_all('a', class_="thumb")

    return [url+elem['href'] for elem in data][1]


"""
def link_huawei(link_p):

    response = requests.get(link_p[0], headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='catalog_block items row margin0 js_append ajax_load block flexbox')\
        .find_all('a', class_='thumb')

    return data
"""
def link_apple():
    for i in range(1, 4):
        response = requests.get(get_url() + f'?PAGEN_1={i}', headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_='catalog_block items row margin0 has-bottom-nav js_append ajax_load block flexbox')\
            .find_all('a', class_='thumb')

        yield data


def get_phone(name_file):
    main_data = []
    for elem in link_apple():
        for elem_1 in elem:
            url_aplle = url+elem_1['href']
            response = requests.get(url_aplle, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find('div', class_='properties__container properties')
            name = soup.find('h1', id='pagetitle').text.strip()
            param = data.find_all('div', class_='properties__title muted properties__item--inline')
            char = data.find_all('div', class_='properties__value darken properties__item--inline')
            dict_huawei = {
                "Модель": name,
                "Характеристики":
                    {param[n].text.strip(): char[n].text.strip() for n in range(len(param))}
            }
            main_data.append(dict_huawei)
    print(main_data)

    try:
        with open(name_file, 'a') as file:
            json.dump(main_data, file, indent=4, ensure_ascii=False)
    except:
        print('Error_file')







if __name__ == '__main__':
    link_p = get_url()
    # huawei = link_huawei(link_p)
    # get_phone(huawei, '../package_1/huawei.json')
    a = link_apple()
    get_phone('../package_1/apple.json')



