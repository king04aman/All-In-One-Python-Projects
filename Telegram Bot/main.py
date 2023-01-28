# Importing modules
import os, requests
from apscheduler.schedulers.background import BackgroundScheduler
import telebot

# Golbal Variables
CITY_NAME = "Delhi,IN"
# Get Telegram Bot Token From Here: https://telegram.me/BotFather
BOT_TOKEN = os.environ['BOT_TOKEN']
# Get Your API Key From Here: https://openweathermap.org/api
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

scheduler = BackgroundScheduler()

# Initialize bot object
bot = telebot.TeleBot(BOT_TOKEN)


# get weather data
def getWeather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={WEATHER_API_KEY}"
    response = requests.get(url)
    weather_data = response.json()

    weather_text = ""

    if weather_data['cod'] == 200:
        weather_text += f"City : {weather_data['name']},  {weather_data['sys']['country']}\n"
        weather_text += f"Coordinate : {weather_data['coord']['lon']} °N, {weather_data['coord']['lat']} °E\n"
        weather_text += f"Weather : {weather_data['weather'][0]['main']}\n"
        weather_text += f"Temperature : {weather_data['main']['temp']} °F\n"
        weather_text += f"Pressure : {weather_data['main']['pressure']} hPa\n"
        weather_text += f"Humidity : {weather_data['main']['humidity']} %\n"
        weather_text += f"Min-Temp : {weather_data['main']['temp_min']} °F\n"
        weather_text += f"Max-Temp : {weather_data['main']['temp_max']} °F\n"
        weather_text += f"Wind Speed : {weather_data['wind']['speed']} m/s\n"
        weather_text += f"Wind Direction : {weather_data['wind']['deg']}°\n"
        weather_text += f"Visibility : {weather_data['visibility']} m\n"
    else:
        weather_text += f"Error:  {weather_data['message']} "

    return weather_text


# send weather data
def sendWeather(message):
    weather_text = getWeather()
    bot.send_message(
        message,
        text="The current weather details in Delhi is: \n\n" + weather_text)


# Start Weather updates
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Weather updates started successfully.")
    scheduler.add_job(sendWeather(message.chat.id), 'interval', hours=1)
    scheduler.start()


# Stop weather updates
@bot.message_handler(commands=['stop'])
def stop(message):
    scheduler.remove_all_jobs()
    bot.send_message(message.chat.id, text="Weather updates stopped successfully.")


# Test command
@bot.message_handler(commands=['test'])
def send_welcome(message):
    bot.reply_to(message, "Hello, I am ready to serve you.")


# Set the listener
bot.set_update_listener(start)
bot.set_update_listener(stop)
# Run the bot
bot.infinity_polling()
