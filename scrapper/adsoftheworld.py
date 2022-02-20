from bs4 import BeautifulSoup
import requests
import re
from .utils import link_setter


def adsoft_scraper():
    url = 'https://www.adsoftheworld.com'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    parent_item = soup.find('div', class_="social-media container-footer")
    links = parent_item.findAll(href=re.compile("https"))

    return link_setter(links, url)
