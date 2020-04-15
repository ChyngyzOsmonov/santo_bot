import requests
from bs4 import BeautifulSoup
from threading import Thread

news_1_main = ''

news_2_main = ''

news_3_main = ''

news_4_main = ''

news_5_main = ''

news_6_main = ''


def foo():
    global news_last, news_1_main, news_2_main, news_3_main, news_4_main, news_5_main, news_6_main
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
            return span.text.strip() + '\n' + href
        except:
            span = ''

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
            return span.text.strip() + '\n' + href
        except:
            span = ''

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
            return span.text.strip() + '\n' + href
        except:
            span = ''

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
            return span.text.strip() + '\n' + href
        except:
            span = ''

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
            return span.text.strip() + '\n' + href
        except:
            span = ''

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
            return span.text.strip() + '\n' + href
        except:
            span = ''

    news_1_main = get_news_1(html)

    news_2_main = get_news_2(html)

    news_3_main = get_news_3(html)

    news_4_main = get_news_4(html)

    news_5_main = get_news_5(html)

    news_6_main = get_news_6(html)


if __name__ == '__main__':
    Thread(target=foo).start()
