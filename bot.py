import telebot
import cfg
from telebot import types
from covid_kg import *
from covid_world import *
from string import Template
import csv
from news_main import *
from news_actual import *
from bs4 import BeautifulSoup
import requests
import time
from threading import Thread
from vebinar import *

bot = telebot.TeleBot(cfg.token)

main_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
covid = types.KeyboardButton('Ситуация короновируса')
news = types.KeyboardButton('Новости')
sending = types.KeyboardButton('Рассылка')
studying = types.KeyboardButton('Обучение')
profile = types.KeyboardButton('Анкетирование')
helper = types.KeyboardButton('Помощник')
main_button.add(covid)
main_button.add(news, studying)  # studying
main_button.add(sending, profile)
# main_button.add(helper)

temporary_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
covid_kg = types.KeyboardButton('Ситуация короновируса в Кыргызстане')
covid_world = types.KeyboardButton('Ситуация короновируса в мире')
back = types.KeyboardButton('Назад в меню')
temporary_button.add(covid_kg)
temporary_button.add(covid_world)
temporary_button.add(back)

sending_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
catalog = types.KeyboardButton('Информация о товарах')
# sending_buttons.add(catalog)
sending_buttons.add(back)

news_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
news_popular = types.KeyboardButton('Самые популярные новости')
news = types.KeyboardButton('Все новости')
news_buttons.add(news_popular, news)
news_buttons.add(back)

back_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_to = types.KeyboardButton('Назад')
back_button.add(back_to)

next_news_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
other_news = types.KeyboardButton('Еще новости')
next_news_buttons.add(other_news)
next_news_buttons.add(back_to)

profile_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
registration = types.KeyboardButton('/profile')
profile_buttons.add(registration)
profile_buttons.add(back)

inline_keyboard = types.InlineKeyboardMarkup()
reg = types.InlineKeyboardButton(text='Рагистрация на данный курс', callback_data='regis')
inline_keyboard.add(reg)

user_dict = {}


class User:
    def __init__(self, gender):
        self.gender = gender

        keys = ['fullname', 'phone']

        for key in keys:
            self.key = None


user_dict_study = {}


class UserStudy:
    def __init__(self, title1):
        self.title1 = title1

        keys = ['fullname', 'phone']

        for key in keys:
            self.key = None


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.chat.id)
    bot.send_message(
        message.chat.id,
        '''Добро пожаловать
        ''',
        reply_markup=main_button)


#########################################################Profile###################################################

@bot.message_handler(commands=["profile"])
def user_reg(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    male = types.KeyboardButton('Мужской')
    female = types.KeyboardButton('Женский')
    markup.add(male, female)

    msg = bot.send_message(message.chat.id, 'Ваш пол', reply_markup=markup)
    bot.register_next_step_handler(msg, process_gender_step)


def process_gender_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        # удалить клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'Введите Ф.И.О', reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)

    except Exception as e:
        bot.reply_to(message, 'Попробуйте еще раз')


def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(chat_id, 'Введите Ваш номер телефона')
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        bot.reply_to(message, 'Повторите попытку')


def process_phone_step(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        bot.send_message(chat_id, getRegData(user, 'Ваша заявка', message.from_user.first_name),
                         parse_mode="Markdown", reply_markup=main_button)
        bot.send_message(cfg.chat_id, getRegData(user, 'Заявка от бота', bot.get_me().username),
                         parse_mode="Markdown")
        print(chat_id)
    except Exception as e:
        print(e)
        msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
        bot.register_next_step_handler(msg, process_phone_step)


def getRegData(user, title, name):
    t = Template('$title *$name* \nФИО: *$fullname* \nТелефон: *$phone* \nПол: *$gender*')

    f_name = user.fullname
    phone = user.phone
    gender = user.gender

    with open('users_profile.csv', 'a') as csvfile:
        fieldnames = ['Full name', 'Phone', 'Gender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Full name': f_name, 'Phone': phone, 'Gender': gender})

    return t.substitute({
        'title': title,
        'name': name,
        'fullname': user.fullname,
        'phone': user.phone,
        'gender': user.gender
    })


###########################################################End_profile##################################################
###########################################################Study#######################################################


@bot.message_handler(commands=["registration"])
def user_reg_study(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    title = types.KeyboardButton(veb_title)
    keyboard.add(title)

    msg = bot.send_message(message.chat.id, 'Нажмите на кнопку для выбора названия курса', reply_markup=keyboard)
    bot.register_next_step_handler(msg, process_gender_step_study)


def process_gender_step_study(message):
    try:
        chat_id = message.chat.id
        user_dict_study[chat_id] = UserStudy(message.text)

        # удалить клавиатуру
        keyboard = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'Введите Ф.И.О', reply_markup=keyboard)
        bot.register_next_step_handler(msg, process_fullname_step_study)

    except Exception as e:
        bot.reply_to(message, 'Повторите еще раз')


def process_fullname_step_study(message):
    try:
        chat_id = message.chat.id
        user_study = user_dict_study[chat_id]
        user_study.fullname = message.text

        msg = bot.send_message(chat_id, 'Введите Ваш номер телефона')
        bot.register_next_step_handler(msg, process_phone_step_study)

    except Exception as e:
        bot.reply_to(message, 'Повторите попытку')


def process_phone_step_study(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        user_study = user_dict_study[chat_id]
        user_study.phone = message.text

        bot.send_message(chat_id, getRegDataStudy(user_study, 'Ваша заявка', message.from_user.first_name),
                         parse_mode="Markdown",
                         reply_markup=main_button)
        bot.send_message(cfg.chat_id, getRegDataStudy(user_study, 'Заявка от бота', bot.get_me().username),
                         parse_mode="Markdown")

    except Exception as e:
        print(e)
        msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
        bot.register_next_step_handler(msg, process_phone_step_study)


def getRegDataStudy(user_study, title, name):
    t = Template('$title *$name* \nФИО: *$fullname* \nТелефон: *$phone* \nНазвания курса: *$title1*')

    return t.substitute({
        'title': title,
        'name': name,
        'fullname': user_study.fullname,
        'phone': user_study.phone,
        'title1': user_study.title1
    })


###########################################################End_Study###################################################


@bot.message_handler(content_types=["text"])
def send_anytext(message):
    chat_id = message.chat.id
    if message.text == 'Ситуация короновируса':
        bot.send_message(chat_id, 'Вы выбрали раздел о ситуации короновируса', reply_markup=temporary_button)
    if message.text == 'Ситуация короновируса в Кыргызстане':
        bot.send_message(chat_id, 'Выявлено всего: {} \nВыявлено за сутки: {}\nИзлечились: {}\nУмерло: {}'.format(total,
                                                                                                                  today,
                                                                                                                  cured,
                                                                                                                  died_kg))
    if message.text == 'Ситуация короновируса в мире':
        bot.send_message(chat_id, 'Выявлено всего: {}\nУмерли: {}'.format(total_world, died_world))
    if message.text == 'Назад в меню':
        bot.send_message(chat_id, 'Вы в главном меню', reply_markup=main_button)

    #################################################News###########################################################

    if message.text == 'Новости':
        bot.send_message(chat_id, 'Вы выбрали раздел новостей', reply_markup=news_buttons)

        def pars():
            def get_html(url):
                result = requests.get(url)
                return result.text

            html = get_html('https://kaktus.media/')
            while True:

                def get_data(html):
                    time.sleep(300)
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
                        
                def get_data_1(html):
                    time.sleep(600)
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
                b = get_data_1(html)
                print('a: {}'.format(a))
                print('b: {}'.format(b))
                if a == b:
                    # bot.send_message(message.chat.id, 'В разделе "Новости" появились новые актуальные новости')
                    print('Same')
                elif a != b:
                    bot.send_message(message.chat.id, 'В разделе "Новости" появились новые актуальные новости')

        if __name__ == '__main__':
            Thread(target=pars).start()
    if message.text == 'Самые популярные новости':
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_1_main, link_1_main))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_2_main, link_2_main))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_3_main, link_3_main))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_4_main, link_4_main))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_6_main, link_6_main))
    if message.text == 'Все новости':
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_1, link_1))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_2, link_2))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_3, link_3))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_4, link_4))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_5, link_5), reply_markup=next_news_buttons)
    if message.text == 'Еще новости':
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_6, link_6))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_7, link_7))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_8, link_8))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_9, link_9))
        bot.send_message(chat_id, '{}\nЧитать по ссылке:\n{}'.format(news_10, link_10), reply_markup=back_button)
    if message.text == 'Назад':
        bot.send_message(chat_id, 'Вы в разделе новостей', reply_markup=news_buttons)

    ##################################################Profile########################################################

    if message.text == 'Анкетирование':
        bot.send_message(chat_id, 'Вы выбрали раздел анкетирования\nДля анкетирования нажмите на /profile',
                         reply_markup=profile_buttons)

    #####################################################Study####################################################

    if message.text == 'Обучение':
        def pars_veb():
            def get_html(url):
                result = requests.get(url)
                return result.text

            html = get_html('http://santo-pharm.kg/news')
            while True:
                def veb1(html):
                    time.sleep(172900)
                    soup = BeautifulSoup(html, 'lxml')
                    try:
                        title = soup.find('div',
                                          class_='last-news__right').find('div',
                                          class_='news__right-item').find(
                            'h2').text.strip()
                        return len(title)
                    except:
                        title = ''
                        
                def veb2(html):
                    time.sleep(173000)
                    soup = BeautifulSoup(html, 'lxml')
                    try:
                        title = soup.find('div',
                                          class_='last-news__right').find('div',
                                          class_='news__right-item').find(
                            'h2').text.strip()
                        return len(title)
                    except:
                        title = ''

                v1 = veb1(html)
                v2 = veb2(html)
                print('a: {}'.format(v1))
                if v1 == v2:
                    pass
                else:
                    bot.send_message(message.chat.id, 'В разделе "Обучение" появился новый вебинар')

        if __name__ == '__main__':
            Thread(target=pars_veb).start()

        bot.send_message(chat_id, '{} \n{}\n{}'.format(veb_title, veb_text, veb_link), reply_markup=inline_keyboard)

    #####################################################Sending######################################################

    if message.text == 'Рассылка':
        bot.send_message(chat_id, 'Вы выбрали раздел рассылки.\n\n{}\n{}\n{}'.format(veb_title, veb_text, veb_link),
                         reply_markup=sending_buttons)
    if message.text == 'Информация о товарах':
        bot.send_message(chat_id, 'Информация о товарах')

    #####################################################Helper########################################################

    if message.text == 'Помощник':
        bot.send_message(chat_id, 'Вы выбрали раздел помощника', reply_markup=None)


#########################################################Inline_callback##############################################


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "regis":
            bot.send_message(call.message.chat.id, 'Нажмите на /registration для регистрации')


try:
    bot.polling(none_stop=True, interval=0, timeout=30)
except Exception as E:
    print(E)
