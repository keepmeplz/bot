import telebot


bot = telebot.TeleBot('6553053895:AAGass2qrX318VeYL7T9Gz79SyWLQ4QKpq4')


@bot.message_handler(func=lambda message: True)
def save_context(message):

    text = message.text


    print("юзер:", text)


    bot.reply_to(message, "Ты хуй")


bot.polling()
