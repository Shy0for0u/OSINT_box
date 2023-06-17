import requests
from requests.exceptions import *


def get_robot_txt(url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
    try:
        if url[-1] == '/':
            page = requests.get(url + 'robots.txt', headers=head, timeout=2)
        else:
            page = requests.get(url + '/robots.txt', headers=head, timeout=2)
        assert page.status_code != 404
    except AssertionError:
        return 'File "robots.txt" not found!'
    except (HTTPError, MissingSchema, ConnectionError, ConnectTimeout) as error:
        return f"Error: {error}"
    else:
        return page.text


# https://ctftime.org
