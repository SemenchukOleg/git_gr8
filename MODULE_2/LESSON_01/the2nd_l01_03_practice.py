# the2nd_l01_03_practice.py
"""
Используя библиотеку requests и метод get необходимо программу для получения изображений, используя pixabay API

1) Программа должна запросить у пользователя категорию изображения - <category> (обязательно учесть отказ от использования категории для получения случайной категории изображения)
2) Далее программа должна запросить у пользователя условие поиска - <q> (также учесть отказ от поиска - случайное изображение)
3) Сам запрос реализовать в виде функции с двумя обязательными аргументами category и q - get_image(category, q)
4) Программа должна работать до тех пор пока пользователь не захочет ее прервать (использовать цикл while) и логику также реализовать в виде функции - collect_images()
P.S. if __name__ == '__main__' - информацию можно узнать перейдя по ссылке:

https://zen.yandex.ru/media/id/5bbcd4ab48032300ab7460a6/chto-delaet-if-name--main-v-python-5eb5731aa19aea5aa92fdcf5
"""

# Ваш код ниже
import requests
import random

KEY = '26450369-8069f750cf2bc5320819fe6fd' # ключ запроса (необходимо получить после регистрации)
BASE_URL = 'https://pixabay.com/api/' # URL адрес запроса

def get_image(category, q):
    params = {
    'key': KEY,
    'orientation': 'horizontal',
    'image_type': 'photo',
    'lang' : 'ru',
    'q': q,
    'category': category,
    # 'page': 2,
    # 'per_page': 3,
    'min_width': 1920,
    'min_height': 1080
    }
    response = requests.get(BASE_URL, params=params) # запрос к изображениям по указанным параметрам params
    data = response.json() # сохраняем полученные данные в переменную data
    response = requests.get(BASE_URL, params=params) # запрос к изображениям по указанным параметрам params
    data = response.json() # сохраняем полученные данные в переменную data
    # фильтруем полученные данные, оставляя только ссылки на изображения
    final_data = []
    for d in data['hits']:
        final_data.append(d['largeImageURL'])
    photo_url = random.choice(final_data) # выбираем любое изображение
    response_image = requests.get(photo_url) # запрос к случайно выбранному изображению
    data_img = response_image.content # сохраняем в битовом представлении полученное изображение
    # сохраняем изображение
    with open(photo_url.split('/')[-1], 'wb') as f:
        f.write(data_img)
    print('Изображение успешно сохранено!')
    pass


def collect_images():
    while True:
        category = input('Введите категорию поиска изображения\n')
        q = input('Введите условие поиска\n')
        if category == 'stop' or q == 'stop':
            break
        get_image(category, q)


if __name__ == '__main__':
    collect_images()
