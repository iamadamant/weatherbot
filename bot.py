import datetime
import telebot
import weathpar as wp
import re


bot = telebot.TeleBot('1330718891:AAGoCgH2B4BqKawDX-gETQLIODZlVpe3WvY')

# Шаблон представления даты
date_template = '%d.%m'

# Текстовое название месяцев
months = [
	None,
	'january',
	'february',
	'march',
	'april',
	'may',
	'june',
	'july',
	'august',
	'september',
	'october',
	'november',
	'december',
]

def check_format(format_):
	"""Проверяет корректен ли формат даты, установленный пользователем

	Keyword arguments:
	format_ -- Строка формата, задаваемая пользователем
	
	"""
	return len(re.findall('%[dm]+.{1}%[dm]', format_.lower())) > 0


def get_date_from_str(dt):
	"""Преобразует строку в объект datetime.date

	Keyword arguments:
	dt -- Текстовое значение даты(месяца и дня)
	
	"""
	return datetime.datetime.strptime(
				dt,
				date_template
			).date()

def get_formatted_date(dt):
	"""Форматирует дату к виду %d-%m (Ex: 7-july)

	Keyword arguments:
	dt -- Текстовое значение даты(месяца и дня)
	
	"""
	date_ = get_date_from_str(dt)
	return str(date_.day) + '-' + months[date_.month]

def get_full_wether_message(dt):
	"""Возвращяюет сообщение с описанием погоды

	Keyword arguments:
	dt -- Текстовое значение даты(месяца и дня)
	
	"""
	msg = 'Погода на ' + str(dt) + ' в г. Ярославль' + '\n\n'
	msg += wp.get_temperature() + '\n'
	msg += wp.get_precipitation_prob() + '\n'
	msg += wp.get_pressure() + '\n'
	msg += wp.get_wind()
	return msg


@bot.message_handler(commands=['setformat'])
def set_format(message):
	"""Обработчик комманды /setformat. Устанавливает заданный формат
	для даты
	
	"""
	global date_template

	msg = ''
	try:
		new_date_template = message.text.split(' ')[1]
		if check_format(new_date_template):
			date_template = new_date_template
			msg = 'Установленно'
		else:
			msg = 'Формат некорректен. Попробуйте снова\n Введите\
			/help для вызова справки'
	except IndexError:
		msg = 'Вы не указали формат'
	bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['help'])
def get_info(message):
	"""Обработчик комманды /help. Возвращяет справку пользователю
	
	"""
	help_msg = 'Для получения сведений о погоде введите дату в формате \
	%d.%m(Пример: 30.06) этот формат также можно изменить командой \
	/setformat <format>(Например /setformat %d-%m)\n\n \
	Полный список команд:\n\n/setformat <format> - Смена формата \
	даты\n /help - Вызов справки'
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
		msg = get_full_wether_message(message.text)	
	except ValueError as e:
		msg = 'Введите корректную дату в формате {0}\nДля получения\
		справки наберите комманду /help'.format(date_template)
		print(e)
	bot.send_message(message.chat.id, msg)


bot.polling()
