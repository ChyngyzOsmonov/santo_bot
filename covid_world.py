import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_world(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        total = soup.find('div', class_='input-summary-presentation-container').find('div',
                            class_='summary').find('div',
                            class_='summary--item summary--confirmed').find('span',
                            class_='summary--number').text.strip()
        died = soup.find('div', class_='input-summary-presentation-container').find('div',
                            class_='summary').find('div',
                            class_='summary--item summary--deaths').find('span',
                            class_='summary--number').text.strip()
        cured = soup.find('div', class_='input-summary-presentation-container').find('div',
                            class_='summary').find('div',
                            class_='summary--item summary--recoveries').find('span',
                            class_='summary--number').text.strip()
        return '<b>В мире:</b>\nВыявлено всего: ' + total + \
               '\n' + 'Умерли: ' + died + '\n' + 'Выздоровели: ' + cured
    except:
        total = ''






