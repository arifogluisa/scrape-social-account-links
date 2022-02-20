from bs4 import BeautifulSoup
import requests
import re
from .utils import link_setter


def dogecoin_scrapper():
    url = 'https://dogecoin.com/'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    first_item = soup.find('a', class_='btn btn-outline-light btn-social mx-1')
    parent = first_item.parent
    links = parent.findAll(href=re.compile("https"))

    return link_setter(links, url)
