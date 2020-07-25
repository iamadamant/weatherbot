import datetime
import re

# Исключение, возникающее при попытке установить некорректный формат даты
class InvalidFormatError(Exception):
	msg = 'Формат некорректен. Попробуйте снова\n Введите\
	/help для вызова справки'

# Формат представления даты
date_format = '%d.%m'

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

def change_format(nformat_):
	"""Меняет формат представления даты. 

	Keyword arguments:
	nformat_ -- Строка формата
	
	"""
	global date_format
	if check_format(nformat_):
		date_format = nformat_
	else:
		raise InvalidFormatError

def get_date_from_str(dt):
	"""Преобразует строку в объект datetime.date

	Keyword arguments:
	dt -- Текстовое значение даты(месяца и дня)
	
	"""
	return datetime.datetime.strptime(
				dt,
				date_format
			).date()

def get_formatted_date(dt):
	"""Форматирует дату к виду %d-%m (Ex: 7-july)

	Keyword arguments:
	dt -- Текстовое значение даты(месяца и дня)
	
	"""
	date_ = get_date_from_str(dt)
	return str(date_.day) + '-' + months[date_.month]
