import requests
from bs4 import BeautifulSoup
import time
import re
"""
response = requests.get(url='http://httpbin.org/')
print(type(response))
# <class 'requests.models.Response'>
"""
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"
  }

response = requests.get(url='http://httpbin.org/user-agent', headers=headers)
print(response.text)

# {
#   "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"
# }
"""
"""
from random import choice

url = 'http://httpbin.org/user-agent'
# подбор случайного 'user-agent' с помощью random
with open('../package_1/user_agent.txt') as file:
    lines = file.read().split('\n')
    headers = {'user-agent': choice(lines)}
    response = requests.get(url=url, headers=headers)
    print(response.text)
    
# "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 OPR/74.0.3911.107"
"""
"""
# библиотека случайных "user-agent"
from fake_useragent import UserAgent
name = UserAgent()
headers = {'user-agent': name.random}
print(headers)
# {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
"""
"""
from fake_useragent import UserAgent
url = 'http://httpbin.org/user-agent'
ua = UserAgent()
fake_ua = {'user-agent': ua.random}
response = requests.get(url=url, headers=fake_ua)
print(response.text)
"""
"""
from random import choice

url = 'http://httpbin.org/ip'

with open('../package_1/proxy.txt') as file:
    proxy_file = file.read().split('\n')
    for _ in range(1000):
        try:
            ip = choice(proxy_file).strip()
            proxy = {
                'http': f'http://{ip}',
                'https': f'https://{ip}'
            }
            response = requests.get(url=url, proxies=proxy)
            print(response.json(), 'Success connection')
        except Exception as _ex:
            continue
"""
"""
proxy = r'../package_1/proxy.txt'
filter_proxy = r'../package_1/filter_proxy.txt'
url = 'http://httpbin.org/ip'
# фильтрует нерабочие proxy
with open(proxy) as pr, open(filter_proxy, 'w') as fpr:
    for ip in pr.readlines():
        test_pr = {
            'http': f'http://{ip.strip()}',
            'https': f'https://{ip.strip()}'
        }
        try:
            response = requests.get(url, proxies=test_pr, timeout=1)
            print(f'status {ip.strip()}: OK')
            fpr.write(f'{test_pr}\n')
        except:
            print(f'status {ip.strip()}: False')
"""
"""
url = 'https://parsinger.ru/video_downloads/'

response = requests.get(url=url)

soup = BeautifulSoup(response.text, "lxml")

movie_url = url + soup.find('video').get('src')

response = requests.get(url=movie_url)

with open("../package_1/file.mp4", 'wb') as file:
    file.write(response.content)
"""
"""
url = 'http://httpbin.org/'
response = requests.get(url)
if response.status_code != 200:
    time.sleep(60)
else:
    print("continue execute code")
"""
"""
for i in range(1,501):
    response = requests.get(f'https://parsinger.ru/task/1/{i}.html')
    if response.status_code == 200:
        print(response.url)
    else:
        print('404')
"""
"""
response = requests.get(url='https://jsonplaceholder.typicode.com/todos/')
print(response.text)
"""
"""
for i in range(1,161):
    response = requests.get(f'https://parsinger.ru/img_download/img/ready/{i}.png')
    with open(f"../package_1/{i}file.png", 'wb') as file:
        file.write(response.content)
"""
"""
with open('/Users/andrejoveskov/PycharmProjects/main_file/index.html') as file:
    soup = BeautifulSoup(file, 'lxml')
    print(soup)
"""
"""
url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('div','item').find_all('li')
for elem in div:
    print(elem.text)
"""
"""
url = 'http://parsinger.ru/html/headphones/5/5_32.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('p', id='p_header').text
print(div)
"""
"""
url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
response.encoding = 'utf-8'
data = soup.find('div', class_='item_card').find_all('div', class_='item')
"""

























