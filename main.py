import requests
import telebot
import time

TOKEN = '7469294817:AAH2GuElArgcAodeiLYC15ybRjw-wV0tqLA'

bot = telebot.TeleBot(TOKEN)

def get_solana_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd'
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        price = data['solana']['usd']
        return price
    except Exception as e:
        print(f"Ошибка получения курса: {e}")
        return None

def send_daily_update():
    while True:
        price = get_solana_price()
        if price:
            message = f"Сегодняшний курс Solana (SOL): ${price}"
            bot.send_message(MY_USER_ID, message)
        else:
            print("Не удалось получить курс. Пробуем снова позже.")
        time.sleep(60)  # сейчас раз в сутки (можно поменять на 60 для теста)

if __name__ == "__main__":
    time.sleep(5)
    send_daily_update()
