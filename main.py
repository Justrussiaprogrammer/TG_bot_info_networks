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


@bot.message_handler(content_types=['text'])
def process(message):
    if message.text == text.FIRST_FUNCTION:
        bot.send_message(message.from_user.id, 'Ты мой хороший :)', reply_markup=types.ReplyKeyboardRemove())
    elif message.text == text.SECOND_FUNCTION:
        bot.send_message(message.from_user.id, 'И так бывает(', reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "echo":
        bot.send_message(message.from_user.id, text.ECHO_TEXT)
    else:
        bot.send_message(message.from_user.id, text.ANOTHER_TEXT)


def get_types_functions(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text.FIRST_FUNCTION)
    btn2 = types.KeyboardButton(text.SECOND_FUNCTION)
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Какой язык выберешь?', reply_markup=markup)


def get_file_name(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ухожу в питон!")
    btn2 = types.KeyboardButton("Остаюсь с c++(")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Какой язык выберешь?', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
