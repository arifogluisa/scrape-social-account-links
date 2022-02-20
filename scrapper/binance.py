from bs4 import BeautifulSoup
import requests
import re
from .utils import link_setter


def binance_scraper():
    url = 'https://www.binance.com'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    parent_div = soup.find('div', class_="css-647kiw")
    child_div = parent_div.find('div', class_="css-vurnku")
    links = child_div.findAll(href=re.compile("https"))

    return link_setter(links, url)
