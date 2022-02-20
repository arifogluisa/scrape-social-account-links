from bs4 import BeautifulSoup
import requests
import re
from .utils import link_setter


def tether_scraper():
    url = 'https://tether.to/en/'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    parent_item = soup.find('div', class_="MuiGrid-root jss236 MuiGrid-container MuiGrid-spacing-xs-2")
    links = parent_item.findAll(href=re.compile("https"))

    return link_setter(links, url)
