import requests
from bs4 import BeautifulSoup
from requests.exceptions import *


def get_page_data(html):
    try:
        res = BeautifulSoup(html.text, 'xml')
        line = res.find_all("loc")
    except (ConnectionError, Exception) as error:
        return f"Error: {error}"
    else:
        return '\n'.join([i.text for i in line])


def page_to_text(html):
    for elem in html.text.split():
        # и то я тут много пропускаю вариантов, можно еще больше найти
        if "sitemap.xml" in elem:
            return elem
    else:
        return False


def get_robot_txt(url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
    try:
        if url[-1] == '/':
            page = requests.get(url + 'robots.txt', headers=head, timeout=2)
        else:
            page = requests.get(url + '/robots.txt', headers=head, timeout=2)
        assert page.status_code != 404
    except (AssertionError, HTTPError, MissingSchema, ConnectionError, ConnectTimeout):
        return False
    else:
        return page_to_text(page)


def sitemap(url):
    try:
        sitemap_name = get_robot_txt(url)   # на примере https://cyber-ed.ru видна необходимость парсить имя
        page = requests.get(sitemap_name, timeout=2)
        if page.status_code == 404:
            if url[-1] == '/':
                sitemap_name = url + "sitemap.xml"
            else:
                sitemap_name = url + "/sitemap.xml"
            page = requests.get(sitemap_name, timeout=2)
        assert page.status_code == 200
    except (AssertionError, HTTPError, MissingSchema, ConnectionError, ConnectTimeout):
        return "File 'sitemap.xml' not found!"
    else:
        get_page_data(page)


# https://ctftime.org https://cyber-ed.ru
