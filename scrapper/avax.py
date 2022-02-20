from bs4 import BeautifulSoup
import requests
import re
from .utils import link_setter


def avax_scrapper():
    url = 'https://www.avax.network/'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    parent_item = soup.find('div', class_='footer-containerel-el')
    child_item = parent_item.next_sibling.next_sibling.next_sibling
    links = child_item.findAll(href=re.compile("https"))

    return link_setter(links, url)
