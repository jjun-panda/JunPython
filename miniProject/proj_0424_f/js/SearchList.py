import requests
from bs4 import BeautifulSoup

def getSearchList(url, css_selector):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    search_list = soup.select(css_selector)
    return search_list
