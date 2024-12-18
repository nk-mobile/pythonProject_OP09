import telebot
import schedule
import time

# Токен вашего бота, полученный от BotFather
BOT_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Создаем экземпляр бота
bot = telebot.TeleBot(BOT_TOKEN)

# ID чата, куда будут отправляться сообщения
CHAT_ID = '890904904'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.chat.id)
    bot.reply_to(message, "Ваш ID чата: {}".format(message.chat.id))

# Функция для отправки сообщения
def send_message():
    bot.send_message(CHAT_ID, "Привет! Это сообщение отправлено по расписанию в хх:хх")

# Устанавливаем расписание
schedule.every().day.at("22:20").do(send_message)  # Отправка сообщения каждый день в 22:20

# Основной цикл для проверки расписания
def main():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

bot.polling(none_stop=True)
