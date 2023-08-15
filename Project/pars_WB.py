import requests
from fake_useragent import UserAgent
import json


ua = UserAgent()

headers = {'User-Agent': ua.random}


def get_url(url: str):
    response = requests.get(url, headers=headers).json()
    try:
        with open('../package_1/apple.json', 'w') as file:
            json.dump(response, file, indent=4, ensure_ascii=False)
    except:
        print('Error apple')

def get_param_json():
    param_apple = {}
    try:
        with open('../package_1/apple.json') as file:
            param = json.load(file)
            for elem in param['data']['products']:

                param_apple[elem['id']] = {
                    'id': elem['id'],
                    'brand': elem['brand'],
                    'name': elem['name'],
                    'price': elem['salePriceU']/100,
                    'rating': elem['reviewRating'],
                    'colors': elem['colors'][0]['name']
                }

        try:
            with open('../package_1/apple.json', 'w') as file:
                json.dump(param_apple, file, indent=4, ensure_ascii=False)
        except:
            print('Error param apple.json')

    except:
        print('Error param apple')





if __name__ == '__main__':
    url = 'https://catalog.wb.ru/catalog/electronic22/catalog?page=1&fbrand=6049&dest=-1257786'
    # get_url(url)
    # get_param_json()
