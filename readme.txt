Телеграм-бот "WeatherBot" 

Позволяет узнать краткую справку о погоде на конкретную дату.

Перед запуском проекта сначала необходимо установить все зависимости из файла "requirements.txt". Это делается следующей командой:

	pip install -r requirements.txt

После того как все необходимыфе библиотеки установяться необходимо запустить скрипт "bot.py". Это можно сделать следующей командой:

	python3 bot.py

Все наш бот настроен и готов работать. 

Перейдите в телеграмме по ссылке: t.me/waetherbot

Теперь можете ввести дату(день, месяц) и узнать погоду.

Пример:

Ваш ввод:
	
	12.04

Ответ:
	
	Погода на 12.04 в г. Ярославль

	Температура: 5°
	Вероятность осадков: 0%
	Атмосферное давление: Давление 756 мм
	Ветер 2 м/с

Полный список команд бота:

	/help - Для получения краткой справки
	/setformat <format> -  устанавливает формат даты на переданный формат format