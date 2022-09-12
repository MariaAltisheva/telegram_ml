from ml_dict import ml
from bot import bot
from welcome import welcome_
from text import text

@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_(message)

@bot.message_handler(content_types=['text'])
def lalala(message):
    text(message)

bot.polling(none_stop=True)