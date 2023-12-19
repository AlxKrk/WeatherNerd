import telebot
from telebot import types

keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

def setup_bot(API_TOKEN):
    bot = telebot.TeleBot(API_TOKEN)

    return bot