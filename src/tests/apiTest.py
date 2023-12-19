import requests
import telebot

# Введите ваш API-ключ для доступа к погодному API
API_KEY = '59cb1f396e0bf4bbd4dec280c214db6e'

# Создаем экземпляр бота с помощью токена
bot = telebot.TeleBot("6434773479:AAFdqFqoXUrR5SCgyWfiVj_jfUK20dIZXWg")

# Функция для получения данных о погоде
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == '404':
        return "Город не найден"
    else:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        weather_info = f"Погода в городе {city}:\n" \
                       f"Описание: {weather_description}\n" \
                       f"Температура: {temperature} K\n" \
                       f"Влажность: {humidity}%"

        return weather_info

# Обращение к боту на команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Введите название города, чтобы получить информацию о погоде.")

# Обращение к боту на текстовое сообщение
@bot.message_handler(func=lambda message: True)
def send_weather(message):
    city = message.text
    weather_info = get_weather(city)
    bot.reply_to(message, weather_info)

# Запуск бота
bot.polling()


