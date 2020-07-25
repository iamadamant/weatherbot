import telebot
import weathpar as wp
from dateparse import *
from messages import *


bot = telebot.TeleBot('1330718891:AAGoCgH2B4BqKawDX-gETQLIODZlVpe3WvY')


@bot.message_handler(commands=['setformat'])
def set_format(message):
	"""Обработчик комманды /setformat. Устанавливает заданный формат
	для даты
	
	"""
	global date_template

	msg = ''
	try:
		new_date_template = message.text.split(' ')[1]
		change_format(new_date_template)
		msg = 'Установленно'
	except IndexError:
		msg = 'Вы не указали формат'
	except InvalidFormatError:
		msg = InvalidFormatError.msg
	bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['help'])
def get_info(message):
	"""Обработчик комманды /help. Возвращяет справку пользователю
	
	"""
	help_msg = get_help_message()
	bot.send_message(message.chat.id, help_msg)

@bot.message_handler(func=lambda m: True)
def get_weather(message):
	"""Когда пользователь введет дату вернет описание погоды за этот
	день
	
	"""
	msg = ''
	try:
		date_ = get_formatted_date(message.text)
		wp.set_date(date_)
		msg = get_full_weather_message(message.text)	
	except ValueError as e:
		msg = 'Введите корректную дату в формате {0}\nДля получения\
		справки наберите комманду /help'.format(date_format)
		print(e)
	bot.send_message(message.chat.id, msg)


bot.polling()
