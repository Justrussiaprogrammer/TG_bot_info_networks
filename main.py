import telebot
from telebot import types


token = '6729177372:AAE996SmTkpSBx_Zi5ixgDoxK8aAPJyWTTc'
bot = telebot.TeleBot(token)


START_TEXT = ("Приветствуем в нашем боте, неизвестный! В будущем он сможет возвращать информацию о нейронках,"
              " но пока он еще растет) Для получения всей информации о боте введи команду /help")
HELP_TEXT = ("Бот умеет обрабатывать запросы о обучении нейросети и выводить информацию о ней пользователю."
             "Пока что работает только это, для его активации напиши 'echo'")
ECHO_TEXT = "Эхо вернулось!"
ANOTHER_TEXT = "Ты написал что-то не то, но сервер пашет! Напиши '/help'"

GET_TEXT = "Как тебя называть? пока не робает"


FIRST_REQ = 'Ухожу в питон!'
SECOND_REQ = 'Остаюсь с c++('


@bot.message_handler(commands=['start'])
def my_start(message):
    bot.send_message(message.from_user.id, START_TEXT)


@bot.message_handler(commands=['help'])
def my_help(message):
    bot.send_message(message.from_user.id, HELP_TEXT)


@bot.message_handler(commands=['get'])
def my_get(message):
    get_buttons(message)


@bot.message_handler(content_types=['text'])
def process(message):
    if message.text == FIRST_REQ:
        bot.send_message(message.from_user.id, 'Ты мой хороший :)', reply_markup=types.ReplyKeyboardRemove())
    elif message.text == SECOND_REQ:
        bot.send_message(message.from_user.id, 'И так бывает(', reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "echo":
        bot.send_message(message.from_user.id, ECHO_TEXT)
    else:
        bot.send_message(message.from_user.id, ANOTHER_TEXT)


# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     global age
#     if call.data == "Ухожу в питон!":
#         bot.send_message(call.message.chat.id, 'Запомню : )', reply_markup=types.ReplyKeyboardRemove())
#     elif call.data == "Остаюсь с c++(":
#         bot.send_message(call.message.chat.id, "Начнем с начала. Как тебя называть?",
#                          reply_markup=types.ReplyKeyboardRemove())
#         bot.register_next_step_handler(call.message, get_name)


def get_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ухожу в питон!")
    btn2 = types.KeyboardButton("Остаюсь с c++(")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Какой язык выберешь?', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
