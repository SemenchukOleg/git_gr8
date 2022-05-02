# -*- coding: utf-8 -*-
# the2nd_l01_01_homework.py

import calendar
import requests
from PIL import Image, ImageFont, ImageDraw
from fpdf import FPDF
import random
import os
import time

# GET Calendar by month and year
def make_calendar_by_month_year(year, month):
    """Возвращает сроку в виде календаря на заданный год (year) и месяц (month)"""
    cal = calendar.TextCalendar(calendar.MONDAY)
    cal_str = cal.formatmonth(year, month)
    return cal_str

# Default Calendar Colors Indigo
DEFAULT_R = 75
DEFAULT_G = 0
DEFAULT_B = 130

# Default YEAR
YEAR = 2021

##### START PART 1 #####
# Ваш код ниже

# API DETAILS
KEY = '26450369-8069f750cf2bc5320819fe6fd' # получите ключ после регистрации
BASE_URL = 'https://pixabay.com/api/'
CATEGORIES = ['fashion', 'nature', 'backgrounds', 'science', 'education', 'people', 'feelings', 'religion', 'health', 'places', 'animals', 'industry', 'food', 'computer', 'sports', 'transportation', 'travel', 'buildings', 'music']
CATEGORIES.insert(0, None)
# category = input('Введите категорию поиска изображения\n')
# q = input('Введите условие поиска\n')

# Get random image within API
def get_random_images(category_my_own):
    """Функция для получения списка ссылок на изображения по заданным параметрам"""
    params = {
    'key': KEY,
    'orientation': 'horizontal',
    'image_type': 'photo',
    'lang' : 'en',
    'q': category_my_own[1],
    'category': category_my_own[0],
    'page': 12,
    # 'per_page': 3,
    'min_width': 1920,
    'min_height': 1080
    }
    response = requests.get(BASE_URL, params=params) # запрос к изображениям по указанным параметрам params
    data = response.json() # сохраняем полученные данные в переменную data
    # фильтруем полученные данные, оставляя только ссылки на изображения
    final_data = []
    for d in data['hits']:
        final_data.append(d['largeImageURL'])
    
    return final_data

##### END PART 1 #####


# Save image from API response
def save_image(image_link):
    """Сохраняет файл и возвращает имя файла для полученного по ссылке изображения (image_link)"""
    response = requests.get(image_link)
    filename = str(random.randint(10000, 99999)) + ".jpg"
    with open(filename, "wb") as f:
        f.write(response.content)
    return filename

# Write text on image
def write_text_on_image(filename, text_month, red=DEFAULT_R, green=DEFAULT_G, blue=DEFAULT_B):
    """Сохраняет файл с нанесенным текстом месяца (text_month) и цветовым фоном RGB (red, green, blue) в файл (filename) и возвращает имя файла, с сохраненным изображением"""
    img = Image.open(filename)
    w = img.width
    draw = ImageDraw.Draw(img)
    stepX = 130
    stepY = 0
    red = red
    green = green
    blue = blue
    draw.rectangle([(620 + stepX, 440), (800 + stepX, 570)], fill=(red, green, blue))
    draw.text((650 + stepX, 450), text_month, (abs(255-red), abs(255-green), abs(255-blue)))
    img.save('after_pil' + filename)
    return 'after_pil' + filename

# Delete images from HDD calendar Image pull
def destroy_calendare_image_pull():
    """Удаляет все используемые изображения"""
    for img_file in os.listdir(os.getcwd()):
        if img_file.endswith('.jpg'):
            os.remove(img_file) 

# Create PDF calendar
def create_calendar_pdf(pdf_filename, calendar_image_pull):
    """Создает календарь .pdf с заданным именем файла (pdf_filename) из списка файлов (calendar_image_pull)"""
    pdf = FPDF(orientation='L', unit='pt', format='Legal')
    for im in calendar_image_pull:
        pdf.add_page()
        pdf.set_left_margin(0)
        pdf.image(im, x = 0, y = 0)
        # pdf.multi_cell(200, 10, txt=TEXT)
    pdf.output(pdf_filename)

def YEAR_input():
    flag = True
    while flag == True:
        year = int(input('Введите год для календаря(от 1900 до 2049)\n'))
        if year >= 1900 and year <= 2049:
            flag = False
            return year
        else:
            print('Введите год в верном диапазоне!\n')


def choose_category():#возвращает список [category, my_own]
        while True:
            print("""Введите число, чтобы выбрать категорию от 1 до 19
1 - fashion
2 - nature
3 - backgrounds
4 - science
5 - education
6 - people
7 - feelings
8 - religion
9 - health
10 - places
11 - animals
12 - industry
13 - food
14 - computer
15 - sports
16 - transportation
17 - travel
18 - buildings
19 - music
Если Вы хотите подобрать изображения через поиск, то введите <my own>
Если Вы хотите выбрать случайную категорию, то введите <random>
""")
            choise = input() # выбор пользователя
            if choise.isnumeric():
                if int(choise) < 1 or int(choise) > 19:
                    print('Вы выбрали несуществующую категорию')
                    print('Попробуйте снова')
                    continue
                else:
                    print(f'Вы выбрали категорию {CATEGORIES[int(choise)]}')
                    return [CATEGORIES[int(choise)],'']
                    break
            elif choise.lower() == 'random':
                print('Вы выбрали случайную категорию')
                return [CATEGORIES[random.randint(1, len(CATEGORIES))],'']
                break
            elif choise.lower() == 'my_own':
                while True:
                    print('Введите слова для поиска')
                    my_own = input()
                    if len(my_own) > 100:
                        print('Вы привысили лимит символов!')
                        continue
                    else:
                        return['',my_own]
                        break
            else:
                print('не выбран ни один из вариантов')


# main
if __name__ == '__main__':
    print("Добро пожаловать в Calendar Maker!!!\n")

    ##### START PART 2 #####


    # Запрос Года
    YEAR = YEAR_input()

    # Запрос Изображения
    category_my_own = choose_category()


    # Запрос Цвета
    while True:
        print('''Введите <Y>, <N> или <R> 
Если Вы хотите выбрать цвет календаря, то введите <Y>
Если Вы хотите использовать цвет по умолчанию (Индиго: R-75, G-0, B-130), то введите <N>
Если Вы хотите использовать случайный цвет, то введите <R>''')
        color_choise = input()
        print(color_choise)
        if color_choise.upper() == 'Y':
            while True:
                print('Введите значение от 0 до 255 для КРАСНОГО:')
                USER_RED = int(input())
                if USER_RED > 255 or USER_RED < 0:
                    print('Вы ввели число вне диапазона от 0 до 255')
                    continue
                else:
                    break
            while True:
                print('Введите значение от 0 до 255 для ЗЕЛЕНОГО:')
                USER_GREEN = int(input())
                if USER_GREEN > 255 or USER_GREEN < 0:
                    print('Вы ввели число вне диапазона от 0 до 255')
                    continue
                else:
                    break
            while True:
                print('Введите значение от 0 до 255 для СИНЕГО:')
                USER_BLUE = int(input())
                if USER_BLUE > 255 or USER_BLUE < 0:
                    print('Вы ввели число вне диапазона от 0 до 255')
                    continue
                else:
                    break
        elif color_choise.upper() == 'N':
            USER_RED = 75
            USER_GREEN = 0
            USER_BLUE = 130
            break
        elif color_choise.upper() == 'R':
            USER_RED = random.randint(0, 255)
            USER_GREEN = random.randint(0, 255)
            USER_BLUE = random.randint(0, 255)
            break
        else:
            print('не выбран ни один из вариантов')


    try:
        print("Подбираем изображения...")
        image_link_list = get_random_images(category_my_own) # ВАМ ВАЖНО НЕ ЗАБЫТЬ ПЕРЕДАТЬ ПАРАМЕТРЫ ДЛЯ ПОЛУЧЕНИЯ СПИСКА НА ИЗОБРАЖЕНИЯ
        ##### END PART 2 #####
    except:
        print("Невозможно подобрать изображения по запросу!\nПопробуйте еще раз!")
    else:
        if len(image_link_list) == 0:
            print("По Вашему запросу не найдены изображения!\nПопробуйте другой запрос!")
        elif len(image_link_list) < 12:
            print("По Вашему запросу не найдено достаточно изображений!\nПопробуйте другой запрос!")
        else:
            image_list = []
            error_flag = False
            print("Cоздаем календарь...")
            for month, img in enumerate(image_link_list[0:12]):
                print(calendar.month_name[month + 1])
                text_cal = make_calendar_by_month_year(YEAR, month+1)
                fname = save_image(img)
                try:
                    fname_text = write_text_on_image(fname, text_cal, red=USER_RED, green=USER_GREEN, blue=USER_BLUE)
                except Exception as err:
                    print("Упс...Невозможно создать календарь с выбранными цветами...")
                    error_flag = True
                else:
                    image_list.append(fname_text)
            if error_flag:
                print("Произошла ошибка при создании календаря!")
                print("Попробуйте еще раз!")
            else:
                calendar_name = "_" + str(random.randint(123213, 21391939)) + ".pdf"
                create_calendar_pdf(calendar_name, image_list)
                destroy_calendare_image_pull()
                print("Ваш календарь успешно создан!!! Имя файла: {}".format(calendar_name))
