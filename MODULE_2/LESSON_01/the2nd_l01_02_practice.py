# the2nd_l01_02_practice.py
"""
Используя библиотеку requests и метод get получить список из 7 шуток с сайта https://icanhazdadjoke.com
Данные необходимо получить используя 1 запрос, то есть нужно изучить документацию API в разделе Search for dad jokes
Данные сохранить в список jokes и вывести все шутки на экран.
Описанное выше задание полностью соответствует заданию pybc_l01_01.py

Из полученных данных необходимо сохранить 7 изображений в формате .png
Названия изображений должны полностью соответствовать id шутки.
"""
# Ваш код ниже
import requests
BASE_URL = 'https://icanhazdadjoke.com' # основной URL
json_headers = {'Accept': 'application/json'} # ответ в формате json
response = requests.get(BASE_URL + '/search' , headers=json_headers, params = {'limit':'7'}) # API запрос
data = response.json() # сохранение данных в json

jokes = [x['joke'] for x in data['results']]

print("Задание 1:\n" + "\n".join(jokes))

jokes_id = [x['id'] for x in data['results']] # сохранение id шутки в переменную
print(jokes_id)
for joke_id in jokes_id:
    joke_png_path = f'/j/{joke_id}.png' # доп путь запроса для получения png
    response_png = requests.get(BASE_URL + joke_png_path) # запрос
    print(BASE_URL + joke_png_path)
    data_png = response_png.content # сохранение изображения в переменную
    # Сохранения файла в формате png
    filename = joke_id + '.png'
    with open(filename, 'wb') as f:
        f.write(data_png)

print("Задание 2:\n" + "Все изображения успешно сохранены")
