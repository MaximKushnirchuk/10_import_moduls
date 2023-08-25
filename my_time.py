
from datetime import datetime, date, time


# Время отправки домашней работы на проверку
d = date(2023, 8, 25)
t = time(18, 11, 22)
my_time = datetime.combine(d, t)
