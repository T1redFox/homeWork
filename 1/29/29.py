from datetime import date, datetime, timedelta
import locale

# date
# today = date.today()
# print(today) # ответ 2019-07-10
# print(today.day) # ответ 10
# print(today.month) # ответ7
# print(today.year) # ответ 2019
# print(today.weekday()) # ответ 2019
# datetime
# now = datetime.now()
# now2 = datetime.today()
# print(now) # ответ 2019-07-10 14:16:51.696373
# print(now.day) # ответ 10
# print(now.month) # ответ7
# print(now.year) # ответ 2019
# print(now.weekday()) # ответ 2
# print(now.hour) # ответ 14
# print(now.minute) # ответ 16
# print(now.second) # ответ 51

# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# print(days[now.weekday()]) # ср

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# locale.setlocale(locale.LC_ALL, 'ru_RU')

# now = datetime.now()
# print(now)
#
# print(now.strftime('%a'))
# print(now.strftime('%A'))
#
# print(f'Дата: {now.strftime("%A, %d %b %Y")}')
# print(f'Время: {now.strftime("%H:%M:%S")}')
#
# print(now.strftime('%c'))
# print(now.strftime('%x'))
# print(now.strftime('%X'))

now = datetime.today()
print(now.strftime('%c'))
d1 = now + timedelta(days=1, hours=2, minutes=10)
print(d1.strftime('%c'))
