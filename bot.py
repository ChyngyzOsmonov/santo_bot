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
from parser import *

bot = telebot.TeleBot(cfg.token)

main_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
covid = types.KeyboardButton('Ситуация короновируса')
news = types.KeyboardButton('Новости')
sending = types.KeyboardButton('Рассылка')
studying = types.KeyboardButton('Обучение')
profile = types.KeyboardButton('Анкетирование')
test = types.KeyboardButton('Тестирование')
main_button.add(covid)
main_button.add(news, studying)
main_button.add(sending, profile)
main_button.add(test)

temporary_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
covid_kg = types.KeyboardButton('Ситуация короновируса в Кыргызстане')
covid_world = types.KeyboardButton('Ситуация короновируса в мире')
back = types.KeyboardButton('Назад в меню')
temporary_button.add(covid_kg)
temporary_button.add(covid_world)
temporary_button.add(back)

testing_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
testing = types.KeyboardButton('Пройти тестирование на знание препаратов')
testing_buttons.add(testing)
testing_buttons.add(back)

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
users = []
new = ''
new_sending = ''
new_covid_world = ''
new_covid_kg = ''


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
        bot.send_message(cfg.sending_chat_id, getRegData(user, 'Заявка от бота', bot.get_me().username),
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
    html_veb = get_html('http://santo-pharm.kg/news')
    title = types.KeyboardButton(vebinar_title(html_veb))
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
        bot.send_message(cfg.sending_chat_id, getRegDataStudy(user_study, 'Заявка от бота', bot.get_me().username),
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
    global new, new_sending, new_covid_world, new_covid_kg
    chat_id = message.chat.id
    if message.text == 'Ситуация короновируса':
        bot.send_message(chat_id, 'Вы выбрали раздел о ситуации короновируса', reply_markup=temporary_button)

        def covid():
            while True:
                time.sleep(1200)
                with open('users.txt', 'r') as file:
                    for line in file:
                        html_c_w = get_html('https://www.bbc.com/russian/news-51706538')
                        html_c_k = get_html('https://kaktus.media/')
                        if new_covid_world != get_total_world(html_c_w) or new_covid_kg != get_total(html_c_k):
                            bot.send_message(line, f'<b>Ситуация короновируса в мире</b>\n\n{get_total_world(html_c_w)}\n\n'
                                                   f'<b>Ситуация короновируса в Кыргызстане</b>\n\n{get_total(html_c_k)}',
                                             parse_mode='HTML')
                            new_covid_world = get_total_world(html_c_w)
                            new_covid_kg = get_total(html_c_k)

        if __name__ == '__main__':
            Thread(target=covid).start()
    if message.text == 'Ситуация короновируса в Кыргызстане':
        html_c_k = get_html('https://kaktus.media/')
        bot.send_message(chat_id, get_total(html_c_k), parse_mode='HTML')
    if message.text == 'Ситуация короновируса в мире':
        html_c_w = get_html('https://www.bbc.com/russian/news-51706538')
        bot.send_message(chat_id, get_total_world(html_c_w), parse_mode='HTML')
    if message.text == 'Назад в меню':
        bot.send_message(chat_id, 'Вы в главном меню', reply_markup=main_button)

    #################################################News###########################################################

    if message.text == 'Новости':
        bot.send_message(chat_id, 'Вы выбрали раздел новостей', reply_markup=news_buttons)

        def pars_2():
            global new
            if chat_id not in users:
                with open('users.txt', 'a+') as f:
                    f.write(str(chat_id) + '\n')
            else:
                pass
            while True:
                time.sleep(300)
                with open('users.txt', 'r') as file:
                    for line in file:
                        print(line)
                        html = get_html('https://kaktus.media/')
                        if new != get_data(html):
                            bot.send_message(line, get_data(html))
                            new = get_data(html)

        if __name__ == '__main__':
            Thread(target=pars_2).start()

    if message.text == 'Самые популярные новости':
        html_p_n = get_html('https://kaktus.media/')
        bot.send_message(chat_id, get_news_1_p(html_p_n))
        bot.send_message(chat_id, get_news_2_p(html_p_n))
        bot.send_message(chat_id, get_news_3_p(html_p_n))
        bot.send_message(chat_id, get_news_4_p(html_p_n))
        bot.send_message(chat_id, get_news_5_p(html_p_n))
        bot.send_message(chat_id, get_news_6_p(html_p_n))
    if message.text == 'Все новости':
        html_a_n = get_html('https://kaktus.media/')
        bot.send_message(chat_id, get_1_news(html_a_n))
        bot.send_message(chat_id, get_2_news(html_a_n))
        bot.send_message(chat_id, get_3_news(html_a_n))
        bot.send_message(chat_id, get_4_news(html_a_n))
        bot.send_message(chat_id, get_5_news(html_a_n), reply_markup=next_news_buttons)
    if message.text == 'Еще новости':
        html_a_n = get_html('https://kaktus.media/')
        bot.send_message(chat_id, get_6_news(html_a_n))
        bot.send_message(chat_id, get_7_news(html_a_n))
        bot.send_message(chat_id, get_8_news(html_a_n))
        bot.send_message(chat_id, get_9_news(html_a_n))
        bot.send_message(chat_id, get_10_news(html_a_n), reply_markup=back_button)
    if message.text == 'Назад':
        bot.send_message(chat_id, 'Вы в разделе новостей', reply_markup=news_buttons)

    ##################################################Profile########################################################

    if message.text == 'Анкетирование':
        bot.send_message(chat_id, 'Вы выбрали раздел анкетирования\nДля анкетирования нажмите на /profile',
                         reply_markup=profile_buttons)

    #####################################################Study####################################################

    if message.text == 'Обучение':
        html_veb = get_html('http://santo-pharm.kg/news')
        bot.send_message(chat_id, '{} \n{}\n{}'.format(vebinar_title(html_veb), vebinar_text(html_veb),
                                                       vebinar_link(html_veb)),
                         reply_markup=inline_keyboard)

    #####################################################Sending######################################################

    if message.text == 'Рассылка':
        html_veb = get_html('http://santo-pharm.kg/news')
        bot.send_message(chat_id, 'Вы выбрали раздел рассылки.\n\n{}\n{}\n{}'.format(vebinar_title(html_veb),
                                                                                      vebinar_text(html_veb),
                                                                                      vebinar_link(html_veb),
                                                                                     reply_markup=main_button))

        def sending_veb():
            global new_sending
            while True:
                time.sleep(7200)
                with open('users.txt', 'r') as f_opened:
                    for x in f_opened:
                        html_veb = get_html('http://santo-pharm.kg/news')
                        print(x)
                        if new_sending != vebinar_title(html_veb):
                            bot.send_message(x, 'Новый вебинар:\n\n{}\n{}\n{}'.format(vebinar_title(html_veb),
                                                                                      vebinar_text(html_veb),
                                                                                      vebinar_link(html_veb)))
                            new_sending = vebinar_title(html_veb)

        if __name__ == '__main__':
            Thread(target=sending_veb).start()

    if message.text == 'Тестирование':
        bot.send_message(chat_id, 'Вы в разделе тестирования', reply_markup=testing_buttons)
    if message.text == 'Пройти тестирование на знание препаратов':
        bot_link = 'Для перехода на тест нажмите на @SantoTestBot'
        bot.send_message(chat_id, bot_link, reply_markup=main_button)

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
