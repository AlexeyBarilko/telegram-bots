import telebot
import random
from telebot import types

bot = telebot.TeleBot("TOKEN")

def generate():
    global x1, x2, x3, x4, x5, x6, x7, x8, value, keyboard
    x1 = random.randint(1, 10)
    x2 = random.randint(1, 10)
    x3 = random.randint(1, 10)
    x4 = random.randint(1, 10)
    x5 = random.randint(1, 10)
    x6 = random.randint(1, 10)
    x7 = random.randint(1, 10)
    x8 = random.randint(1, 10)
    value = str(x1) + " * " + str(x2) + " = "
    keyboard = types.ReplyKeyboardRemove()
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    rand = random.randint(1, 4)
    if rand == 1:
        keyboard.add(types.KeyboardButton(x1 * x2), types.KeyboardButton(x3 * x4), types.KeyboardButton(x5 * x6),
                     types.KeyboardButton(x7 * x8))
    elif rand == 2:
        keyboard.add(types.KeyboardButton(x3 * x4), types.KeyboardButton(x1 * x2), types.KeyboardButton(x5 * x6),
                     types.KeyboardButton(x7 * x8))
    elif rand == 3:
        keyboard.add(types.KeyboardButton(x5 * x6), types.KeyboardButton(x3 * x4), types.KeyboardButton(x1 * x2),
                     types.KeyboardButton(x7 * x8))
    elif rand == 4:
        keyboard.add(types.KeyboardButton(x7 * x8), types.KeyboardButton(x3 * x4), types.KeyboardButton(x5 * x6),
                     types.KeyboardButton(x1 * x2))


@bot.message_handler(commands=['start'])
def Hi(message):
    print(message.chat.id + "\n" + message.text + " start ")
    bot.send_message(message.chat.id, "Hello,this bot help u learn multiplication.",
                     reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id, value, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def check(message):
    print(message.chat.id + "\n" + message.text)
    try:
        if int(message.text) == x1 * x2:
            bot.send_message(message.chat.id, "Right", reply_markup=None)
            generate()
            bot.send_message(message.chat.id, value, reply_markup=keyboard)
        elif int(message.text) != x1 * x2:
            bot.send_message(message.chat.id, "Wrong, try again.")
    except ValueError:
        bot.send_message(message.chat.id, "Please, insert the number")

generate()
bot.infinity_polling()
