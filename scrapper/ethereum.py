from bs4 import BeautifulSoup
import requests
import re
from .utils import link_setter


def ethereum_scrapper():
    url = 'https://ethereum.org/en/'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    parent_item = soup.find('div', class_='Footer__SocialIcons-sc-1to993d-9 kdLbod')
    links = parent_item.findAll(href=re.compile("https"))

    return link_setter(links, url)
