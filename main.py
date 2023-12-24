import config
import functions
import telebot
from telebot import types

import pd_info
import text
# import io


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
        if message.text == text.GET_INFO_FUNCTION:
            bot.send_message(message.from_user.id, pd_info.get_info(message.text))
            status_get = 1
            return

        bot.send_message(message.from_user.id, 'Вы выбрали функцию ' + last_function + ' для файла ' + message.text,
                         reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.from_user.id, text.INPUT_VALUES)
        last_filename = message.text
        status_get = 3
    elif status_get == 3:
        try:
            final_mass = list()
            mass = message.text.split(',')
            for i in range(len(mass)):
                mass[i] = ''.join(mass[i])
                if '-' not in mass[i]:
                    final_mass.append(int(mass[i]))
                elif mass[i][0] == '-' and mass[i].count('-') == 1:
                    bot.send_message(message.from_user.id, text.NEGATIVE_ERROR)
                    return
                elif mass[i].count('-') > 1:
                    bot.send_message(message.from_user.id, text.INPUT_ERROR)
                    return
                else:
                    borders = mass[i].split('-')
                    if len(borders) == 1:
                        bot.send_message(message.from_user.id, text.INPUT_ERROR)
                        return
                    left, right = borders
                    left = int(''.join(left.split()))
                    right = int(''.join(right.split()))
                    final_mass.extend(list(range(left, right + 1)))
        except Exception:
            bot.send_message(message.from_user.id, text.INPUT_ERROR)
            return

        bot.send_message(message.from_user.id, 'Вы выбрали ' + last_function + ', файл ' + last_filename
                         + ', параметры (' + ', '.join([str(x) for x in final_mass]) + ')',
                         reply_markup=types.ReplyKeyboardRemove())
        if last_function == text.VALUE_FUNCTION:
            bot.send_message(message.from_user.id, text.INPUT_TIME)
        else:
            bot.send_message(message.from_user.id, text.INPUT_TIMES)
        last_columns = final_mass
        status_get = 4
    elif status_get == 4:
        try:
            arr = message.text.split()

            if ((last_function == text.VALUE_FUNCTION and len(arr) != 1) or
                    (last_function != text.VALUE_FUNCTION and len(arr) != 2)):
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

        # try:
        #     x = np.linspace(0, 10, 10)
        #     y = np.linspace(0, 10, 10)
        #     plt.plot(x, y)
        #
        #     figfile = io.BytesIO()
        #     plt.savefig(figfile, format='png')
        #
        #     buf = io.BytesIO()
        #
        #     # extract csv-string, convert it to bytes and write to buffer
        #     buf.write(figfile.getvalue().encode())
        #     buf.seek(0)
        #
        #     # set a filename with file's extension
        #     buf.name = f'secret_report_for_cool_guys.csv'
        #
        #     # send the buffer as a regular file
        #     bot.send_document(message.chat.id, buf)
        # except Exception:
        #     bot.send_message(message.from_user.id, "Что-то пошло нет так")

        if last_function == 'plot' and answer != text.QUERY_ERROR:
            f_for_out = open("./plot_image.jpg", "rb")
            bot.send_document(message.chat.id, f_for_out)
            f_for_out.close()

        status_get = 1
    else:
        bot.send_message(message.from_user.id, text.ANOTHER_TEXT)


def get_types_functions(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text.MIN_FUNCTION)
    btn2 = types.KeyboardButton(text.MAX_FUNCTION)
    btn3 = types.KeyboardButton(text.PLOT_FUNCTION)
    btn4 = types.KeyboardButton(text.VALUE_FUNCTION)
    btn5 = types.KeyboardButton(text.MEAN_FUNCTION)
    btn6 = types.KeyboardButton(text.DEVIATION_FUNCTION)
    btn7 = types.KeyboardButton(text.VARIANCE_FUNCTION)
    btn8 = types.KeyboardButton(text.GET_INFO_FUNCTION)
    btn9 = types.KeyboardButton(text.MEDIAN_FUNCTION)
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
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


if __name__ == '__main__':
    print("The end")
