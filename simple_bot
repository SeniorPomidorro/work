import telebot

bot_token = ''
bot = telebot.TeleBot(bot_token)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling()
