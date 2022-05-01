# the2nd_l01_01_practice.py
"""
Используя библиотеку requests и метод get получить список из 7 шуток с сайта https://icanhazdadjoke.com
Данные необходимо получить используя 1 запрос, то есть нужно изучить документацию API в разделе Search for dad jokes
Данные сохранить в список jokes и вывести все шутки на экран. 
"""
# Ваш код ниже
import requests
BASE_URL = 'https://icanhazdadjoke.com/search' # основной URL
json_headers = {'Accept': 'application/json'} # ответ в формате json
response = requests.get(BASE_URL, headers=json_headers, params = {'limit':'7'}) # API запрос
data = response.json() # сохранение данных в json

jokes = [x['joke'] for x in data['results']]

print("Задание 1:\n" + "\n".join(jokes))
