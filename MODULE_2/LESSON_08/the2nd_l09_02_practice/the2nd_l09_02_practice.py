# the2nd_l09_02_practice.py
"""
Создать папку LESSON_09. Перейти в папку LESSON_09 и создать в ней папку the2nd_l09_02_practice. Перейти в папку the2nd_l09_02_practice. Скопировать в нее файл the2nd_l09_02_practice.py.

ПРОВЕРКА ВРЕМЕНИ
Напишите функцию is_valid_time, которая принимает в качестве аргумента строку. Функция должна возвращать значение True, если строка отформатированна согласно времени (от "00:00" до "23:59"). Если же строка содержит некорректные данные согласно принятому формату времени, то функция возвращает False.
Имейте ввиду, что допускается использовать в часах как одну цифру, так и две ("7:15" или "07:15" - корректное время)

Пример:
    is_valid_time("7:15") --> True
    is_valid_time("07:15") --> True
    is_valid_time("17.15") --> False
    is_valid_time("2315") --> False
    is_valid_time("147:15") --> False
    is_valid_time("24:00") --> False
    is_valid_time("00:00") --> True
    is_valid_time("03:63") --> False

Строка должна содержать только время:
    is_valid_time("time is 17:49") --> False
    is_valid_time("17:49 the time") --> False
"""
import re

# ВАШ КОД НИЖЕ
def is_valid_time(check_time):
    time_regex = re.compile(r"\d{1,2}:\d{1,2}")
    match = time_regex.fullmatch(check_time)
    if match:
        return True
    return False

check_list = ["7:15", "07:15", "17.15", "2315", "147:15", "24:00", "00:00", "time is 17:49", "17:49 the time"]
for check in check_list: print(is_valid_time(check))



