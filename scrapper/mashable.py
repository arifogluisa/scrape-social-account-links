from bs4 import BeautifulSoup
import requests
import re
from .utils import link_setter


def mashable():
    url = 'https://mashable.com/'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    first_item = soup.find('ul', class_='flex flex-row text-white flex-wrap my-8 md:mb-12 md:mt-5 md:space-x-8')
    links = first_item.findAll(href=re.compile("https"))

    return link_setter(links, url)
