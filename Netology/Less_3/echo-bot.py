import telebot
token = "5252699878:AAEkDWgXWJdn9mKG9j2_GPPKQ7StOOWn65U"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    #  if telebot.__name__('Dmitriy Zakharov') in message:
    if __name__ == 'Dmitriy Zakharov':
        bot.send_message(message.chat.id, "Ба, знакомые все лица!")
    else:
        bot.send_message(message.chat.id, "Ты не Дмитрий")


bot.polling(none_stop=True)

# print(dir(telebot.__name__))
