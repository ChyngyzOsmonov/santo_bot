from bs4 import BeautifulSoup as BS
import requests
import time


def get_html(url):
    result = requests.get(url)
    return result.text


def get_data(html):
    try:
        soup = BS(html, 'lxml')
        li = soup.find('li', {'class': 'topic_item clearfix', 'data-num': '1'})
        a = li.find('a').get('href')
        span = li.find('span', {'class': 'n'})
        return (span.text + '\n' + a)
    except:
        print('Parse error')
