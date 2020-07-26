import weathpar as wp

def get_full_weather_message(dt):
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

def get_help_message():
	"""Возвращяюет сообщение с краткой справкой
	
	"""
	return 'Для получения сведений о погоде введите дату в формате \
	%d.%m(Пример: 30.06) этот формат также можно изменить командой \
	/setformat <format>(Например /setformat %d-%m)\n\n \
	Полный список команд:\n\n/setformat <format> - Смена формата \
	даты\n /help - Вызов справки'