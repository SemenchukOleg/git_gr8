# the2nd_l09_03_practice.py
"""
Создать папку LESSON_09. Перейти в папку LESSON_09 и создать в ней папку the2nd_l09_03_practice. Перейти в папку the2nd_l09_03_practice. Скопировать в нее файл the2nd_l09_03_practice.py.

ОБРАБОТКА БАЙТОВ
Напишите функцию parse_bytes, которая принимает в качестве аргумента строку. Функция должна возвращать список, который должен возвращать список двоичных байтов, содержащихся в строке.
Каждый байт - это комбинация состоящая из восьми единиц и нулей (например, 10001001).

Пример:
    parse_bytes("10101010 123 652") --> ["10101010"]
    parse_bytes("result: 10000001 00011000") --> ["10000001", "00011000"]
    parse_bytes(" 101010 ") --> []
    parse_bytes("this is not a byte") --> []
    parse_bytes("benjamin_10001000") --> []

"""
import re

# ВАШ КОД НИЖЕ
def parse_bytes(check_bytes):
    bite_regex = re.compile(r'\b\d{8}\b')
    match = bite_regex.findall(check_bytes)
    
    return match
    

check_list = [
        "10101010 123 652",
        "result: 10000001 00011000",
        " 101010 ",
        "this is not a byte",
        "benjamin_10001000"
        ]

for check in check_list: print(parse_bytes(check))