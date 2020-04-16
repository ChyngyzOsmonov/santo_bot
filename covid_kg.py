import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        total = soup.find('div',
                          class_='covid19-banner--info').find('div',
                          class_='covid19-banner--info-row').find('div',
                          class_='covid19-banner--info-row-value').text.strip()
        today = soup.find('div',
                          class_='covid19-banner--info').find('div',
                          class_='covid19-banner--info-row').find_next('div',
                          class_='covid19-banner--info-row').find('div',
                          class_='covid19-banner--info-row-value').text.strip()
        cured = soup.find('div',
                          class_='covid19-banner--info').find('div',
                          class_='covid19-banner--info-row').find_next('div',
                          class_='covid19-banner--info-row').find('div',
                          class_='covid19-banner--info-row-value').find_next('div',
                          class_='covid19-banner--info-row-value').text.strip()
        died = soup.find('div',
                         class_='covid19-banner--info').find('div',
                         class_='covid19-banner--info-row').find_next('div',
                         class_='covid19-banner--info-row').find('div',
                         class_='covid19-banner--info-row-value').find_next('div',
                         class_='covid19-banner--info-row-value').find_next('div',
                         class_='covid19-banner--info-row-value').text.strip()
        return f'<b>В Кыргызстане:</b>\nВсего случаев: {total}\nЗа сутки: {today}\nВылечились: {cured}\nУмерли: {died}'
    except:
        died = ''




