import config
import telebot
from telebot import types
import text


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def my_start(message):
    bot.send_message(message.from_user.id, text.START_TEXT)


@bot.message_handler(commands=['help'])
def my_help(message):
    bot.send_message(message.from_user.id, text.HELP_TEXT)


@bot.message_handler(commands=['echo'])
def my_help(message):
    bot.send_message(message.from_user.id, text.ECHO_TEXT)


@bot.message_handler(commands=['get'])
def my_get(message):
    get_types_functions(message)


last_function = ''


@bot.message_handler(content_types=['text'])
def process(message):
    global last_function
    if message.text in text.ALL_FUNCTIONS:
        bot.send_message(message.from_user.id, 'Вы выбрали функцию ' + message.text,
                         reply_markup=types.ReplyKeyboardRemove())
        last_function = message.text
        get_filename(message)
    elif message.text in text.ALL_FILENAMES:
        bot.send_message(message.from_user.id, 'Вы выбрали функцию ' + last_function + ' для файла ' + message.text,
                         reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.from_user.id, text.ANOTHER_TEXT)


def get_types_functions(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text.FIRST_FUNCTION)
    btn2 = types.KeyboardButton(text.SECOND_FUNCTION)
    btn3 = types.KeyboardButton(text.THIRD_FUNCTION)
    btn4 = types.KeyboardButton(text.FOURTH_FUNCTION)
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, text.GET_FUNCTION_TEXT, reply_markup=markup)


def get_filename(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text.FIRST_FILENAME)
    btn2 = types.KeyboardButton(text.SECOND_FILENAME)
    btn3 = types.KeyboardButton(text.THIRD_FILENAME)
    btn4 = types.KeyboardButton(text.FOURTH_FILENAME)
    btn5 = types.KeyboardButton(text.FIFTH_FILENAME)
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, text.GET_FILENAME_TEXT, reply_markup=markup)


bot.polling(none_stop=True)
