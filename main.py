import config
import functions
import telebot
from telebot import types
import text


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def my_start(message):
    global status_get

    bot.send_message(message.from_user.id, text.START_TEXT, reply_markup=types.ReplyKeyboardRemove())
    status_get = 1


@bot.message_handler(commands=['help'])
def my_help(message):
    global status_get

    bot.send_message(message.from_user.id, text.HELP_TEXT, reply_markup=types.ReplyKeyboardRemove())
    status_get = 1


@bot.message_handler(commands=['echo'])
def my_help(message):
    global status_get

    bot.send_message(message.from_user.id, text.ECHO_TEXT, reply_markup=types.ReplyKeyboardRemove())
    status_get = 1


@bot.message_handler(commands=['get'])
def my_get(message):
    global status_get

    get_types_functions(message)
    status_get = 1


last_function = ''
last_filename = ''
last_columns = []
last_times = ''
status_get = 1


@bot.message_handler(content_types=['text'])
def process(message):
    global last_function, status_get, last_filename, last_columns, last_times

    if message.text in text.ALL_FUNCTIONS:
        bot.send_message(message.from_user.id, 'Вы выбрали функцию ' + message.text,
                         reply_markup=types.ReplyKeyboardRemove())
        last_function = message.text
        get_filename(message)
        status_get = 2
    elif message.text in text.ALL_FILENAMES:
        bot.send_message(message.from_user.id, 'Вы выбрали функцию ' + last_function + ' для файла ' + message.text,
                         reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.from_user.id, text.INPUT_VALUES)
        last_filename = message.text
        status_get = 3
    elif status_get == 3:
        mass = message.text.split()
        for i in range(len(mass)):
            try:
                mass[i] = int(mass[i])
                if mass[i] < 0:
                    bot.send_message(message.from_user.id, text.NEGATIVE_ERROR)
                    return
            except Exception:
                bot.send_message(message.from_user.id, text.INPUT_ERROR)
                return
        bot.send_message(message.from_user.id, 'Вы выбрали ' + last_function + ', файл ' + last_filename
                         + ', параметры (' + ', '.join([str(x) for x in mass]) + ')',
                         reply_markup=types.ReplyKeyboardRemove())
        if last_function == text.FOURTH_FUNCTION:
            bot.send_message(message.from_user.id, text.INPUT_TIME)
        else:
            bot.send_message(message.from_user.id, text.INPUT_TIMES)
        last_columns = mass
        status_get = 4
    elif status_get == 4:
        try:
            arr = message.text.split()

            if ((last_function == text.FOURTH_FUNCTION and len(arr) != 1) or
                    (last_function != text.FOURTH_FUNCTION and len(arr) != 2)):
                bot.send_message(message.from_user.id, text.INPUT_ERROR)
                return

            for i in range(len(arr)):
                mass = arr[i].split(':')

                if len(mass[0]) != 2 or len(mass[1]) != 2 or len(mass) != 2:
                    bot.send_message(message.from_user.id, text.INPUT_ERROR)
                    return

                mass[0] = int(mass[0])
                if mass[0] < 0 or mass[0] > 23:
                    bot.send_message(message.from_user.id, text.HOUR_ERROR)
                    return

                mass[1] = int(mass[1])
                if mass[1] < 0 or mass[1] > 59:
                    bot.send_message(message.from_user.id, text.MINUTE_ERROR)
                    return
        except Exception:
            bot.send_message(message.from_user.id, text.INPUT_ERROR)
            return

        bot.send_message(message.from_user.id, 'Функция ' + last_function + ', файл ' + last_filename + ', параметры ('
                         + ', '.join([str(x) for x in last_columns]) + '), время "' + message.text + '"',
                         reply_markup=types.ReplyKeyboardRemove())
        last_times = message.text.split()

        answer = functions.function(last_function, last_filename, last_columns, last_times)
        bot.send_message(message.from_user.id, str(answer))

        # f1 = open("/Users/htotu/PycharmProjects/TG_bot_info_networks/archive/sample.pdf", "rb")
        # f2 = open("/Users/htotu/PycharmProjects/TG_bot_info_networks/archive/sample.jpeg", "rb")
        #
        # bot.send_document(message.chat.id, f1)
        # bot.send_document(message.chat.id, f2)

        status_get = 1
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
