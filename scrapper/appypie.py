from bs4 import BeautifulSoup
import requests
import re
from .utils import link_setter


def appypie():
    url = 'https://www.appypie.com/contact-us'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    first_item = soup.find('div', class_='footer-social')
    links = first_item.findAll(href=re.compile("https"))

    return link_setter(links, url)
