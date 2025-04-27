import requests
import telebot
import time

# Твой токен от Telegram бота
TOKEN = '8113463759:AAGDcv9ffQXXJvUjVVpDjHy88zUYZG*****'
# Твой user_id
MY_USER_ID = 450564953

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Функция получения курса Solana
def get_solana_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    price = data['solana']['usd']
    return price

# Основной цикл отправки сообщений
def send_daily_update():
    while True:
        price = get_solana_price()
        message = f"Сегодняшний курс Solana (SOL): ${price}"
        bot.send_message(MY_USER_ID, message)
        time.sleep(86400)  # 86400 секунд = 24 часа

# Запуск программы
if __name__ == "__main__":
    time.sleep(5)  # Небольшая задержка для Render
    send_daily_update()
