import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("TOKEN")

def generate():
    global numbers, value, keyboard
    numbers = [random.randint(1, 10) for x in range(8)]
    print(numbers)
    value = (f"{numbers[0]} * {numbers[1]} = ?")
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(numbers[0] * numbers[1], callback_data="True"),
                InlineKeyboardButton(numbers[2] * numbers[3], callback_data="False" if numbers[2] * numbers[3] != numbers[0] * numbers[1] else "True"),
                 InlineKeyboardButton(numbers[4] * numbers[5], callback_data="False" if numbers[4] * numbers[5] != numbers[0] * numbers[1] else "True"),
                  InlineKeyboardButton(numbers[6] * numbers[7], callback_data="False" if numbers[6] * numbers[7] != numbers[0] * numbers[1] else "True")]
    random.shuffle(buttons)
    keyboard.add(buttons[0], buttons[1], buttons[2], buttons[3])

@bot.message_handler(commands=['start'])
def hello(message):
    global tasks
    tasks = 5
    print(f"{message.chat.id} {message.text}")
    generate()
    bot.send_message(message.chat.id, "Hello,this bot will helped you to learn multiplication.")
    bot.send_message(message.chat.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global tasks
    if call.data == "True":
        if tasks != 0:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"You're right, {numbers[0]} * {numbers[1]} = {numbers[0] * numbers[1]}.\n{tasks} tasks left.", reply_markup=None)
            generate()
            bot.send_message(call.message.chat.id, value, reply_markup=keyboard)
            tasks -= 1
        else:bot.send_message(call.message.chat.id, "Congratulations, you have completed all the tasks for today.", reply_markup=None)
    elif "False":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"You're wrong, {numbers[0]} * {numbers[1]} = {numbers[0] * numbers[1]}.\n{tasks} tasks left.", reply_markup=None)
        generate()
        bot.send_message(call.message.chat.id, value, reply_markup=keyboard)

bot.infinity_polling()