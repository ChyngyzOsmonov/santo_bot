import requests
from bs4 import BeautifulSoup

url = 'https://kaktus.media/'


def get_html(url):
    r = requests.get(url)
    return r.text

html = get_html(url)


def get_total(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        total = soup.find('div', class_='covid19-banner--info').find('div', class_='covid19-banner--info-row').find('div', class_='covid19-banner--info-row-value').text.strip()
        return total
    except:
        total = ''


def get_today(html):
    soup = BeautifulSoup(html, 'lxml')
    
    try:
        today = soup.find('div', class_='covid19-banner--info').find('div', class_='covid19-banner--info-row').find_next('div', class_='covid19-banner--info-row').find('div', class_='covid19-banner--info-row-value').text.strip()
        return today
    except:
        today = ''


def get_cured(html):
    soup = BeautifulSoup(html, 'lxml')
    
    try:
        cured = soup.find('div', class_='covid19-banner--info').find('div', class_='covid19-banner--info-row').find_next('div', class_='covid19-banner--info-row').find('div', class_='covid19-banner--info-row-value').find_next('div', class_='covid19-banner--info-row-value').text.strip()
        return cured
    except:
        cured = ''


def get_died(html):
    soup = BeautifulSoup(html, 'lxml')

    try:
        died = soup.find('div', class_='covid19-banner--info').find('div', class_='covid19-banner--info-row').find_next('div', class_='covid19-banner--info-row').find('div', class_='covid19-banner--info-row-value').find_next('div', class_='covid19-banner--info-row-value').find_next('div', class_='covid19-banner--info-row-value').text.strip()
        return died
    except:
        died = ''


total = get_total(html)
today = get_today(html)
cured = get_cured(html)
died_kg = get_died(html)


