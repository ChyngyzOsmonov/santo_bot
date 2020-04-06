import requests
from bs4 import BeautifulSoup

url = 'https://kaktus.media/'


def get_html(url):
    r = requests.get(url)
    return r.text


html = get_html(url)

# ########################################### 1 ##########################################################################


def get_1_news(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        news = soup.find('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').text.strip()
        return news
    except:
        news = ''

def get_1_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        links = soup.find('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').get('href')
        return links
    except:
        links = ''

def get_2_news(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        news = soup.find('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').text.strip()
        return news
    except:
        news = ''


def get_2_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        links = soup.find('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').get('href')
        return links
    except:
        links = ''


def get_6_news(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        news = soup.find('div',
                         class_='main--important-articles-chunk').find_next('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').text.strip()
        return news
    except:
        news = ''


def get_6_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        links = soup.find('div',
                         class_='main--important-articles-chunk').find_next('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').get('href')
        return links
    except:
        links = ''


news_1 = get_1_news(html)
link_1 = get_1_links(html)
print(news_1)
print(link_1)
news_2 = get_2_news(html)
link_2 = get_2_links(html)
print(news_2)
print(link_2)
news_6 = get_6_news(html)
link_6 = get_6_links(html)
print(news_6)
print(link_6)