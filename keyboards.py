import telebot
from telebot import types


main_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
covid = types.KeyboardButton('Ситуация короновируса')
news = types.KeyboardButton('Новости')
studying = types.KeyboardButton('Обучение')
profile = types.KeyboardButton('Анкетирование')
test = types.KeyboardButton('Тестирование')
main_button.add(covid)
main_button.add(news, profile)
main_button.add(studying, test)

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