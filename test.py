import requests
from bs4 import BeautifulSoup
import time
from threading import Thread

def pars():
    def get_html(url):
        result = requests.get(url)
        return result.text

    html = get_html('https://kaktus.media/')
    while True:


        def get_data_1(html):
            time.sleep(10)
            try:
                soup = BeautifulSoup(html, 'lxml')
                ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
                li = ul.find('li', {'data-num': 1})
                div = li.find('div', {'class': 't f_medium'})
                a_teg = div.find('a')
                span = a_teg.find('span', {'class': 'n'})
                return len(span.text)
            except:
                print()



        def get_data(html):
            time.sleep(15)
            try:
                soup = BeautifulSoup(html, 'lxml')
                ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
                li = ul.find('li', {'data-num': 1})
                div = li.find('div', {'class': 't f_medium'})
                a_teg = div.find('a')
                span = a_teg.find('span', {'class': 'n'})
                return len(span.text)
            except:
                print()

        a = get_data(html)
        print('a: {}'.format(a))
        b = get_data_1(html)
        print('b: {}'.format(b))
        if a == b:
            pass
        else:
            print('New')
            # bot.send_message(message.chat.id, 'В разделе "Новости" появились новые актуальные новости')


if __name__ == '__main__':
    Thread(target=pars).start()