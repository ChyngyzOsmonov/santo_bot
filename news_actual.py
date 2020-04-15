import requests
from bs4 import BeautifulSoup
import threading

news_1 = ''

news_2 = ''

news_3 = ''

news_4 = ''

news_5 = ''

news_6 = ''

news_7 = ''

news_8 = ''

news_9 = ''

news_10 = ''


def foo_all():
    global news_1, news_2, news_3, news_4, news_5, news_6, news_7, news_8, news_9, news_10
    threading.Timer(54000, foo_all).start()
    url = 'https://kaktus.media/'


    def get_html(url):
        r = requests.get(url)
        return r.text


    html = get_html(url)

    # ########################################### 1 ##########################################################################


    def get_1_news(html):
        try:
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find('div', {'class': 'main--important-articles-chunk'})
            div2 = div.find('div', {'class': 'main--important-article'})
            a = div2.find('a', {'class': 'main--important-article-title'})
            href = div2.find('a', {'class': 'main--important-article-title'}).get('href')
            return a.text.strip() + '\n' + href
        except:
            href = ''


    #################################################### 2 ################################################################

    def get_2_news(html):
        try:
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find('div', {'class': 'main--important-articles-chunk'})
            div2 = div.find('div', {'class': 'main--important-article'})
            div3 = div2.find_next('div', {'class': 'main--important-article'})
            a = div3.find('a', {'class': 'main--important-article-title'})
            href = div3.find('a', {'class': 'main--important-article-title'}).get('href')
            return a.text.strip() + '\n' + href
        except:
            href = ''


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
        try:
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find('div', {'class': 'main--important-articles-chunk'})
            div2 = div.find('div', {'class': 'main--important-article'})
            div3 = div2.find_next('div', {'class': 'main--important-article'})
            div4 = div3.find_next('div', {'class': 'main--important-article'})
            a = div4.find('a', {'class': 'main--important-article-title'})
            href = div4.find('a', {'class': 'main--important-article-title'}).get('href')
            return a.text.strip() + '\n' + href
        except:
            href = ''

    #################################################### 4 ###############################################################

    def get_4_news(html):
        try:
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find('div', {'class': 'main--important-articles-chunk'})
            div2 = div.find('div', {'class': 'main--important-article'})
            div3 = div2.find_next('div', {'class': 'main--important-article'})
            div4 = div3.find_next('div', {'class': 'main--important-article'})
            div5 = div4.find_next('div', {'class': 'main--important-article'})
            a = div5.find('a', {'class': 'main--important-article-title'})
            href = div5.find('a', {'class': 'main--important-article-title'}).get('href')
            return a.text.strip() + '\n' + href
        except:
            href = ''

    ################################################## 5 ###############################################################


    def get_5_news(html):
        try:
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find('div', {'class': 'main--important-articles-chunk'})
            div2 = div.find('div', {'class': 'main--important-article'})
            div3 = div2.find_next('div', {'class': 'main--important-article'})
            div4 = div3.find_next('div', {'class': 'main--important-article'})
            div5 = div4.find_next('div', {'class': 'main--important-article'})
            div6 = div5.find_next('div', {'class': 'main--important-article'})
            a = div6.find('a', {'class': 'main--important-article-title'})
            href = div6.find('a', {'class': 'main--important-article-title'}).get('href')
            return a.text.strip() + '\n' + href
        except:
            href = ''

    #############################################6##########################################################################


    def get_6_news(html):
        try:
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find('div', {'class': 'main--important-articles-chunk'})
            div2 = div.find('div', {'class': 'main--important-article'})
            div3 = div2.find_next('div', {'class': 'main--important-article'})
            div4 = div3.find_next('div', {'class': 'main--important-article'})
            div5 = div4.find_next('div', {'class': 'main--important-article'})
            div6 = div5.find_next('div', {'class': 'main--important-article'})
            div7 = div6.find_next('div', {'class': 'main--important-article'})
            a = div7.find('a', {'class': 'main--important-article-title'})
            href = div7.find('a', {'class': 'main--important-article-title'}).get('href')
            return a.text.strip() + '\n' + href
        except:
            href = ''


    ##############################################7###################################################################


    def get_7_news(html):
        try:
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find('div', {'class': 'main--important-articles-chunk'})
            div2 = div.find('div', {'class': 'main--important-article'})
            div3 = div2.find_next('div', {'class': 'main--important-article'})
            div4 = div3.find_next('div', {'class': 'main--important-article'})
            div5 = div4.find_next('div', {'class': 'main--important-article'})
            div6 = div5.find_next('div', {'class': 'main--important-article'})
            div7 = div6.find_next('div', {'class': 'main--important-article'})
            div8 = div7.find_next('div', {'class': 'main--important-article'})
            a = div8.find('a', {'class': 'main--important-article-title'})
            href = div8.find('a', {'class': 'main--important-article-title'}).get('href')
            return a.text.strip() + '\n' + href
        except:
            href = ''


    ######################################################8############################################################


    def get_8_news(html):
        try:
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find('div', {'class': 'main--important-articles-chunk'})
            div2 = div.find('div', {'class': 'main--important-article'})
            div3 = div2.find_next('div', {'class': 'main--important-article'})
            div4 = div3.find_next('div', {'class': 'main--important-article'})
            div5 = div4.find_next('div', {'class': 'main--important-article'})
            div6 = div5.find_next('div', {'class': 'main--important-article'})
            div7 = div6.find_next('div', {'class': 'main--important-article'})
            div8 = div7.find_next('div', {'class': 'main--important-article'})
            div9 = div8.find_next('div', {'class': 'main--important-article'})
            a = div9.find('a', {'class': 'main--important-article-title'})
            href = div9.find('a', {'class': 'main--important-article-title'}).get('href')
            return a.text.strip() + '\n' + href
        except:
            href = ''

    #############################################9########################################################################

    def get_9_news(html):
        try:
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find('div', {'class': 'main--important-articles-chunk'})
            div2 = div.find('div', {'class': 'main--important-article'})
            div3 = div2.find_next('div', {'class': 'main--important-article'})
            div4 = div3.find_next('div', {'class': 'main--important-article'})
            div5 = div4.find_next('div', {'class': 'main--important-article'})
            div6 = div5.find_next('div', {'class': 'main--important-article'})
            div7 = div6.find_next('div', {'class': 'main--important-article'})
            div8 = div7.find_next('div', {'class': 'main--important-article'})
            div9 = div8.find_next('div', {'class': 'main--important-article'})
            div10 = div9.find_next('div', {'class': 'main--important-article'})
            a = div10.find('a', {'class': 'main--important-article-title'})
            href = div10.find('a', {'class': 'main--important-article-title'}).get('href')
            return a.text.strip() + '\n' + href
        except:
            href = ''

    ####################################################10################################################################

    def get_10_news(html):
        try:
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find('div', {'class': 'main--important-articles-chunk'})
            div2 = div.find('div', {'class': 'main--important-article'})
            div3 = div2.find_next('div', {'class': 'main--important-article'})
            div4 = div3.find_next('div', {'class': 'main--important-article'})
            div5 = div4.find_next('div', {'class': 'main--important-article'})
            div6 = div5.find_next('div', {'class': 'main--important-article'})
            div7 = div6.find_next('div', {'class': 'main--important-article'})
            div8 = div7.find_next('div', {'class': 'main--important-article'})
            div9 = div8.find_next('div', {'class': 'main--important-article'})
            div10 = div9.find_next('div', {'class': 'main--important-article'})
            div11 = div10.find_next('div', {'class': 'main--important-article'})
            a = div11.find('a', {'class': 'main--important-article-title'})
            href = div11.find('a', {'class': 'main--important-article-title'}).get('href')
            return a.text.strip() + '\n' + href
        except:
            href = ''

    news_1 = get_1_news(html)

    news_2 = get_2_news(html)

    news_3 = get_3_news(html)

    news_4 = get_4_news(html)

    news_5 = get_5_news(html)

    news_6 = get_6_news(html)

    news_7 = get_7_news(html)

    news_8 = get_8_news(html)

    news_9 = get_9_news(html)

    news_10 = get_10_news(html)

foo_all()