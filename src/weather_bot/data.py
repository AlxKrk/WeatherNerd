import requests
import json

def load_json(path):
    file = open(path)
    json_file = json.load(file) 
    file.close()
    return json_file

def dump_json(json_file, path):
    file = open(path, 'w')
    json.dump(json_file, file)
    file.close()

users = load_json('weather_bot/databases/users.json')
cities = load_json('weather_bot/databases/cities.json')

def get_weather(chat_id):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={users[chat_id]['latitude']}&longitude={users[chat_id]['longitude']}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

def update_user_location(chat_id, latitude, longtitude):
    users[chat_id]['latitude'] = latitude
    users[chat_id]['longitude'] = longtitude
