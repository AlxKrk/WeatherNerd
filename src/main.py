from weather_bot import setup_bot
from weather_bot.handlers import run_bot
from weather_bot.token import API_TOKEN

if __name__ == '__main__':
    bot = setup_bot(API_TOKEN)
    run_bot(bot)