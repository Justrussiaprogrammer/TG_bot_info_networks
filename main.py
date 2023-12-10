import telebot
from telebot import types


token = '6729177372:AAE996SmTkpSBx_Zi5ixgDoxK8aAPJyWTTc'
bot = telebot.TeleBot(token)


START_TEXT = ("Приветствуем в нашем боте, неизвестный! В будущем он сможет возвращать информацию о нейронках,"
              " но пока он еще растет) Для получения всей информации о боте введи команду /help\n")
HELP_TEXT = ("Бот умеет обрабатывать запросы о обучении нейросети и выводить информацию о ней пользователю."
             "Пока что работает только это, для его активации напиши 'echo'")
ECHO_TEXT = "Эхо вернулось!"
ANOTHER_TEXT = "Ты написал что-то не то, но сервер пашет! Напиши '/help'"

GET_TEXT = "Как тебя называть? пока не робает"


name = ''
age = 0


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, START_TEXT)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, HELP_TEXT)
    elif message.text == '/get':
        if name == '':
            bot.send_message(message.from_user.id, GET_TEXT)
            bot.register_next_step_handler(message, get_name)
        else:
            bot.register_next_step_handler(message, get_name)
    elif message.text == "echo":
        bot.send_message(message.from_user.id, ECHO_TEXT)
    else:
        bot.send_message(message.from_user.id, ANOTHER_TEXT)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global age
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        age = 10
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        bot.send_message(call.message.from_user.id, "Начнем с начала. Как тебя называть?")
        bot.register_next_step_handler(call.message, get_name)  # следующий шаг – функция get_name


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Что тебе нужно от бота?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    keyboard = types.InlineKeyboardMarkup() #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
    keyboard.add(key_yes) #добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)
