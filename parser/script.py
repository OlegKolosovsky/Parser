import requests
from bs4 import BeautifulSoup

URL = 'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
           'accept': 'text/css,*/*;q=0.1'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='catalog-product')

    smartphones = []
    for item in items:
        smartphones.append({
            'title': item.find('a', class_='catalog-product__name').get_text(strip=True),
        })

    print(smartphones)


def parce():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Не удаётся установить соединение с сайтом.')


parce()
