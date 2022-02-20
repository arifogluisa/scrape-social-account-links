from bs4 import BeautifulSoup
import requests
from .utils import link_setter


def catcoin():
    url = 'https://www.catcoincrypto.net/'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    parent_item = soup.find('div', id='w-node-c378fd71-ee0e-c6a1-c9ec-32dbf06d71a4-bd2a4008')

    return link_setter(parent_item, url)
