import os

from weather_sdk import get_new_event, SMSServer

token = os.getenv('FORECAST_TOKEN')
town_title = 'Курск'

sms_token = os.getenv('SMS_TOKEN')
server = SMSServer(sms_token)

new_event = get_new_event(token, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = '''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''

print("token", token)

print("town_title", town_title)
print("event_time", event_time)
print("event_date", event_date)
print("event_area", event_area)
print("phenomenon_description", phenomenon_description)
print("new_event", new_event)


sms_message = sms_template.format(
    phenomenon_description,
    town_title,
    event_time,
    event_date,
    event_area,
)

server.send(sms_message)

# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(new_event)
# Установленный факт: Выводится ew_event Регион:  Погода: 
# Вывод: В переменной что то не то.

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: print("town_title", town_title)
# Код для проверки: print("town_title", town_title)
# Установленный факт: Выводится town_title Курск
# Вывод: Выводится town_title Курск

# Гипотеза 2.2: В town_title не название города
# Способ проверки: print("town_title", town_title)
# Код для проверки: print("town_title", town_title)
# Установленный факт: Выводится town_title Курск
# Вывод: Выводится town_title Курск

# Гипотеза 3: В  token нет токена.
# Способ проверки: print("token", token)
# Код для проверки: print("token", token)
# Установленный факт: Выводится token None
# Вывод:  проблема в токене

# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: print("token", token)
# Код для проверки: print("token", token)
# Установленный факт: токен не пуст
# Вывод: токен не пуст

# Гипотеза 4.2: Может, в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`?
# Способ проверки: print("token", token)
# Код для проверки: print("token", token)
# Установленный факт: в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`
# Вывод: в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`

# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: print("token", token)
# Код для проверки: print("token", token)
# Установленный факт: в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`
# Вывод: значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки new_event

# Гипотеза 5.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: print("event_time", event_time)
# Код для проверки: print("event_time", event_time)
# Установленный факт: Все нормально
# Вывод: Все нормально

# Гипотеза 5.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: print("event_date", event_date)
# Код для проверки: print("event_date", event_date)
# Установленный факт: Все нормально
# Вывод: Все нормально

# Гипотеза 5.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: print("event_area", event_area)
# Код для проверки: print("event_area", event_area)
# Установленный факт: Все нормально
# Вывод: Все нормально

# Гипотеза 5.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: print("phenomenon_description", phenomenon_description)
# Код для проверки: print("phenomenon_description", phenomenon_description)
# Установленный факт: Все нормально
# Вывод: Все нормально

# Гипотеза 6: Есть ошибки в словах
# Способ проверки: проверка переменных через поиск по словам
# Код для проверки: 
# Установленный факт: ошибок нет
# Вывод: ошибок нет