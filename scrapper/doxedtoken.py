from bs4 import BeautifulSoup
import requests
import re
from .utils import link_setter


def doxedtoken():
    url = 'https://doxedtoken.com/'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    parent_item = soup.find('div', class_='et_pb_code_inner')
    links = parent_item.findAll(href=re.compile("https"))

    return link_setter(links, url)
