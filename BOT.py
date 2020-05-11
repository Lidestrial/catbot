import telebot
import config
import requests
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['cat'])
def cat(message):
    resp = requests.get(f'http://aws.random.cat/meow')
    pic = resp.json()['file']
    if pic[-4:] == ".gif":
        bot.send_video(message.chat.id, pic)
    else:
        bot.send_photo(message.chat.id, pic)

    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton("/cat")
    markup.row(item1)

    bot.send_message(message.chat.id, "foo", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def foo(message):
    bot.send_message(message.chat.id, "U'r mommy ones said " + message.text)


# RUN
bot.polling(none_stop=True)
