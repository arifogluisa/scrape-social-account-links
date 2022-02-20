from bs4 import BeautifulSoup
import requests
import re
from .utils import link_setter


def terra_money():
    url = 'https://www.terra.money/'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    first_item = soup.find('a', class_='menu__social-icon w-inline-block')
    parent = first_item.parent
    links = parent.findAll(href=re.compile("https"))

    return link_setter(links, url)
