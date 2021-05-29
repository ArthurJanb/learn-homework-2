#----------
# Домашнее задание №2
#----------
# Задание: Дата и время

# 1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
# 2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

from datetime import date, timedelta, datetime

def print_days():
    dt_now = datetime.now()
    dt_yestarday = dt_now - timedelta(days=1)
    dt_30d_ago = dt_now - timedelta(days=30)

    print(f"Сейчас - {dt_now}")
    print(f"Вчера было - {dt_yestarday}")
    print(f"30 дней назад было - {dt_30d_ago}")

def change_srt(date_string):
    dt_data = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return dt_data

if __name__ == "__main__":
    print_days()
    print(change_srt("01/01/20 12:10:03.234567"))
