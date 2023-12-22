from telebot import types
from .data import users, cities, dump_json, get_weather, update_user_location
from .drawing import draw_graph
from .__init__ import keyboard

def run_bot(bot) -> None:
    @bot.message_handler(commands=['start'])
    def start(message) -> None:

        button = types.KeyboardButton('Погода')
        keyboard.add(button)
        button = types.KeyboardButton('Температура')
        keyboard.add(button)
        button = types.KeyboardButton('Скорость Ветра')
        keyboard.add(button)
        button = types.KeyboardButton('Отправить Местоположение', request_location=True)
        keyboard.add(button)
        button = types.KeyboardButton('Выбрать Город')
        keyboard.add(button)

        bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)

    @bot.message_handler(content_types=['location'])
    def get_user_location(message) -> None:
        chat_id = str(message.chat.id)

        if chat_id in users:
            update_user_location(chat_id, message.location.latitude, message.location.longitude)
        else:
            # new_user = {
            #         chat_id: {
            #             'latitude': message.location.latitude,
            #             'longitude': message.location.longitude
            #         }
            # }
            # users.append(new_user)
            users[chat_id] = {
                'latitude': message.location.latitude,
                'longitude': message.location.longitude
            }

            dump_json(users, 'weather_bot/databases/users.json')
            bot.reply_to(message, 'Местоположение обновлено')

    @bot.message_handler(func=lambda message: True)
    def response(message) -> None:
        chat_id = str(message.chat.id)

        weather = get_weather(chat_id)

        if weather is None:
            bot.reply_to(message, "Отправьте своё местоположение или выберите город")
            return None

        reply = ''
        match message.text:
            case 'Погода':
                timestamps = weather['hourly']['time'][:24]
                temperatures = weather['hourly']['temperature_2m'][:24]
                draw_graph(timestamps, temperatures)
                bot.send_photo(message.chat.id, types.InputFile('weather_bot/graphs/graph.png'))
            case 'Температура':
                if chat_id in users:
                    temperature = weather['current']['temperature_2m']
                    reactions = ['💀', '🥶', '😖', '😬', '🙁', '😐', '🙂', '😚', '😅', '🥵']
                    i = int((temperature + 40)/10)
                    i *= (i > 0)*(i < 10)
                    reply = reactions[i] + str(temperature) + ' °C' + reactions[i]
                else:
                    bot.reply_to(message, 'Сначала передайте мне свое местоположение')
            case 'Скорость Ветра':
                if chat_id in users:
                    reply = str(weather['current']['wind_speed_10m']) + ' км/ч'
                else:
                    bot.reply_to(message, 'Сначала передайте мне свое местоположение')
            case 'Выбрать Город':
                msg = bot.reply_to(message, 'Введите имя города')
                bot.register_next_step_handler(msg, get_city_location)

        if reply != '':
            bot.reply_to(message, reply)

    def get_city_location(message) -> None:
        chat_id = str(message.chat.id)

        city = message.text
        if city in cities:
            update_user_location(chat_id, cities[city]['latitude'], cities[city]['longitude'])
            bot.reply_to(message, 'Местоположение успешно измененно на ' + city)
        else:
            bot.reply_to(message, 'Город не распознан')


    bot.polling()
