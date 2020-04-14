import requests
from bs4 import BeautifulSoup

url = 'https://kaktus.media/'


def get_html(url):
    r = requests.get(url)
    return r.text


html = get_html(url)


# ########################################### 1 ##########################################################################
def get_news_1(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 1})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip()
    except:
        span = ''


def get_link_1(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 1})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return href
    except:
        href = ''


#################################################### 2 ################################################################

def get_news_2(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 2})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip()
    except:
        span = ''


def get_link_2(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 2})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return href
    except:
        href = ''


################################################ 3 ##################################################################

def get_news_3(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 3})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip()
    except:
        span = ''


def get_link_3(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 3})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return href
    except:
        href = ''


#################################################### 4 ###############################################################

def get_news_4(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 4})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip()
    except:
        span = ''


def get_link_4(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 4})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return href
    except:
        href = ''


################################################## 5 ###############################################################


def get_news_5(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 5})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip()
    except:
        span = ''


def get_link_5(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 5})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return href
    except:
        href = ''


##################################################6##########################################################


def get_news_6(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 6})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip()
    except:
        span = ''


def get_link_6(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 6})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return href
    except:
        href = ''

def get_data_2(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        li = soup.find('li', {'class': 'topic_item clearfix', 'data-num': '1'})
        a = li.find('a').get('href')
        span = li.find('span', {'class': 'n'})
        return (span.text + '\n' + a)
    except:
        print('Parse error')

news_last = get_data_2(html)

news_1_main = get_news_1(html)
link_1_main = get_link_1(html)

news_2_main = get_news_2(html)
link_2_main = get_link_2(html)

news_3_main = get_news_3(html)
link_3_main = get_link_3(html)

news_4_main = get_news_4(html)
link_4_main = get_link_4(html)

news_5_main = get_news_5(html)
link_5_main = get_link_5(html)

news_6_main = get_news_6(html)
link_6_main = get_link_6(html)