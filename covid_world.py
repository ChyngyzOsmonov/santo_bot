import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/russian/news-51706538'


def get_html(url):
    r = requests.get(url)
    return r.text

html = get_html(url)

def get_total_world(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        total = soup.find('tr', class_='summary__body').find('td', class_='summary__infected gel-double-pica').text.strip()
        return total
    except:
        total = ''

def get_died_world(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        died = soup.find('tr', class_='summary__body').find('td', class_='summary__deceased gel-double-pica').text.strip()
        return died
    except:
        died = ''

total_world = get_total_world(html)
died_world = get_died_world(html)