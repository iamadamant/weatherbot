import requests
from bs4 import BeautifulSoup
import re

class EmptyDateError(Exception):
	"""Исключение возникающее если дата не установленна
	
	"""
	msg = 'Дата не установленна' # Текст сообщения об ошибке


soup = None

def is_parsed(f):
	"""Декоратор. Проверяет установленна ли дата, 
	и возбуждает исключение если это не так

	Keyword arguments:
	f -- Функция, которая зависит от даты(установленна или нет)
	
	"""
	def inner():
		if soup is None:
			raise EmptyDateError(EmptyDateError.msg)
		else:
			return f()
	return inner


def set_date(dt):
	"""Устанавливает дату и парсит данные

	Keyword arguments:
	dt -- Текстовое значение даты
	(месяца и дня в формате %d-%m Ex: 7-july)
	
	"""
	global soup
	res = requests.get(
			'https://weather.rambler.ru/v-yaroslavle/{0}/'.format(dt)
		)
	soup = BeautifulSoup(res.text, 'html.parser')


@is_parsed
def get_precipitation_prob():
	"""Возвращяет сообщение о вероятности осадков
	
	"""
	answ = 'Вероятность осадков: '
	try:
		precipitation_prb = soup.find(text='Осадки').parent.parent
		answ += precipitation_prb.getText().split(' ')[2]
	except IndexError:
		answ += '0%'
	except:
		answ += 'Нет данных'
	return answ


@is_parsed
def get_temperature():
	"""Возвращяет сообщение о температуре
	
	"""
	answ = 'Температура: '
	try:
		temperature = soup.find_all('', class_='_1HBR')[0]
		answ += temperature.getText()
	except IndexError:
		answ += 'Нет данных'
	return answ

@is_parsed
def get_pressure():
	"""Возвращяет сообщение о давлении
	
	"""
	answ = 'Атмосферное давление: '
	try:
		pressure = soup.find(text=re.compile('Давление.*')).parent
		answ += pressure.getText()
	except IndexError:
		answ += 'Нет данных'
	return answ

@is_parsed
def get_wind():
	"""Возвращяет сообщение о силе ветра
	
	"""
	answ = 'Ветер: '
	try:
		wind = soup.find(text=re.compile('Ветер.*')).parent
		answ = wind.getText()
	except:
		answ += 'Нет данных'
	return answ
		