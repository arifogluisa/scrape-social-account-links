from bs4 import BeautifulSoup
import requests
import re
from .utils import link_setter


def markmeta():
    url = 'https://markmeta.finance/'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    first_item = soup.find('div', class_='col-lg-12 d-flex')
    links = first_item.findAll(href=re.compile("https"))

    return link_setter(links, url)
