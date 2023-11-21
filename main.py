import telebot


token = 'Add token to start bot'
bot = telebot.TeleBot(token)


START_TEXT = ("Приветствуем в нашем боте! В будущем он сможет возвращать информацию о нейронках, но пока он еще"
              " растет) Пока работает только эхо, попробуй его активировать!\n")
HELP_TEXT = "Напиши 'echo'"
ECHO_TEXT = "Эхо вернулось!"
ANOTHER_TEXT = "Ты написал что-то не то, но сервер пашет! Напиши '/help'"


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, START_TEXT)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, HELP_TEXT)
    elif message.text == "echo":
        bot.send_message(message.from_user.id, ECHO_TEXT)
    else:
        bot.send_message(message.from_user.id, ANOTHER_TEXT)


bot.polling(none_stop=True, interval=0)
