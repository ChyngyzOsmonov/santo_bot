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

#################################################### 2 ################################################################

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

################################################ 3 ##################################################################

def get_3_news(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        news = soup.find('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').text.strip()
        return news
    except:
        news = ''


def get_3_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        links = soup.find('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').get('href')
        return links
    except:
        links = ''

#################################################### 4 ###############################################################

def get_4_news(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        news = soup.find('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').text.strip()
        return news
    except:
        news = ''


def get_4_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        links = soup.find('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').get('href')
        return links
    except:
        links = ''


################################################## 5 ###############################################################


def get_5_news(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        news = soup.find('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').text.strip()
        return news
    except:
        news = ''


def get_5_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        links = soup.find('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').get('href')
        return links
    except:
        links = ''

#############################################6##########################################################################


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

##############################################7###################################################################


def get_7_news(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        news = soup.find('div',
                         class_='main--important-articles-chunk').find_next('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').text.strip()
        return news
    except:
        news = ''


def get_7_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        links = soup.find('div',
                         class_='main--important-articles-chunk').find_next('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').get('href')
        return links
    except:
        links = ''

######################################################8############################################################


def get_8_news(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        news = soup.find('div',
                         class_='main--important-articles-chunk').find_next('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').text.strip()
        return news
    except:
        news = ''


def get_8_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        links = soup.find('div',
                         class_='main--important-articles-chunk').find_next('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').get('href')
        return links
    except:
        links = ''

#############################################9########################################################################

def get_9_news(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        news = soup.find('div',
                         class_='main--important-articles-chunk').find_next('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').text.strip()
        return news
    except:
        news = ''


def get_9_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        links = soup.find('div',
                         class_='main--important-articles-chunk').find_next('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').get('href')
        return links
    except:
        links = ''

####################################################10################################################################

def get_10_news(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        news = soup.find('div',
                         class_='main--important-articles-chunk').find_next('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').text.strip()
        return news
    except:
        news = ''


def get_10_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        links = soup.find('div',
                         class_='main--important-articles-chunk').find_next('div',
                         class_='main--important-articles-chunk').find('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find_next('div',
                         class_='main--important-article').find('a',
                         class_='main--important-article-title').get('href')
        return links
    except:
        links = ''


news_1 = get_1_news(html)
link_1 = get_1_links(html)

news_2 = get_2_news(html)
link_2 = get_2_links(html)

news_3 = get_3_news(html)
link_3 = get_3_links(html)

news_4 = get_4_news(html)
link_4 = get_4_links(html)

news_5 = get_5_news(html)
link_5 = get_5_links(html)

news_6 = get_6_news(html)
link_6 = get_6_links(html)

news_7 = get_7_news(html)
link_7 = get_7_links(html)

news_8 = get_8_news(html)
link_8 = get_8_links(html)

news_9 = get_9_news(html)
link_9 = get_9_links(html)

news_10 = get_10_news(html)
link_10 = get_10_links(html)

