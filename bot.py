from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Настройка прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
	'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

# Логируем все в файлик
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')

# Веси пока я не захочу тебя прервать. Тут мы конектимся к телеграму
def main():
	mybot = Updater("744307307:AAE_oJt_HMSYoYdUCFou7sZc4gFyY1dFz7A", request_kwargs=PROXY)
	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))
	mybot.start_polling()
	mybot.idle()

#когда пользователь в чате напишет /start вручную или подключится к боту в первый раз
def greet_user(bot, update):
	text = "Вызван /start"
	print(text)
	print(update)
	update.message.reply_text(text)

def talk_to_me(bot, update):
	user_text = update.message.text 
	print(user_text)
	update.message.reply_text(user_text)

main()
