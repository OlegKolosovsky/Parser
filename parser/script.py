import requests
from bs4 import BeautifulSoup

URL = 'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
           'accept': 'text/css,*/*;q=0.1'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def parce():
    html = get_html(URL)
    if html.status_code == 200:
        parce
    else:
        print('Не удаётся установить соединение с сайтом.')


parce()
