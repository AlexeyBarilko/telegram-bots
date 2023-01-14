import telebot
from pprint import pprint
import requests
from datetime import datetime

open_weather_token = "WEATHER_TOKEN"
bot = telebot.TeleBot('TELEGRAM_API_TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Please,enter city name.")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    open_weather_token = "WEATHER_TOKEN"
    try:
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()
        city = data["name"]
        cur_weather = data["main"]["temp"]
        nirvana = data["main"]["feels_like"]
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.fromtimestamp(data["sys"]["sunset"])
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        speed = data["wind"]["speed"]
        weather = "In city " + city + " " + str(cur_weather) + "C." + "\n" + "Feels like " + str(nirvana) + "C." + "\n" + "Sunrise at " + str(sunrise) + "\n" + "Sunset at " + str(sunset) + "\n" + "Wind speed " + str(speed) + " m/s." + "\n" + "Humidity " + str(humidity) + "%." + "\n" + "Pressure " + str(pressure) + "." + "\n"
        bot.send_message(message.chat.id, weather)
        f.write(datetime.now().strftime("%Y.%m.%d %H:%M:%S") + " " + str(message.chat.id) + " " + str(message.text) + "\n" + weather + "\n")
    except Exception as ex:
        bot.send_message(message.chat.id, "The city you entered does not exist.")

bot.infinity_polling()