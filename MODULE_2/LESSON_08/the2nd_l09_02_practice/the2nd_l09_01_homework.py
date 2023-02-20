# the2nd_l09_01_homework.py
"""
Создать папку LESSON_09. Перейти в папку LESSON_09 и создать в ней папку the2nd_l09_01_homework. Перейти в папку the2nd_l09_01_homework. Скопировать в нее файл the2nd_l09_01_homework.py.

-=*** GIVE ME AN IMAGE FROM NATIONAL GEOGRAPHY ***=-

Напишите функцию get_img_url, которая будет находить ссылки на все изображения сохраненные в переменной data (данные хранятся в виде строки).
Данные в переменной data - это результат запроса GET на сайт https://www.instagram.com/natgeo/

Ссылки на изображения, к которым необходимо написать регулярное выражение представлены в формате:

"src":"https://scontent-arn2-1.cdninstagram.com/vp/d1bd5ef62357946d3e602e318a2ba0c1/5D3D3A74/t51.2885-15/sh0.08/e35/c0.135.1080.1080/s640x640/56347818_439423140135260_222436944865078914_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com","config_width":640

"src":"https://scontent-arn2-1.cdninstagram.com/vp/822a0ba89496db753a0cd1ec55d5a556/5D3F5191/t51.2885-15/sh0.08/e35/c0.75.1080.1080/s640x640/54513868_2499920290078880_6085694610039206455_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com","config_width":640

"src":"https://scontent-arn2-1.cdninstagram.com/vp/bf0671c779e473fe8312c62674bef6e4/5D3E631A/t51.2885-15/e15/c180.0.720.720/s640x640/54463866_560472434444154_2512477850949351202_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com","config_width":640

ОБЯЗАТЕЛЬНО ПРИ ПОИСКЕ УЧЕСТЬ ,"config_width":640 - ТАК КАК ЭТО ВЛИЯЕТ НА РАЗМЕР СОХРАНЯЕМОГО ИЗОБРАЖЕНИЯ

Данные необходимо вернуть в виде списка:

["https://scontent-arn2-1.cdninstagram.com/vp/d1bd5ef62357946d3e602e318a2ba0c1/5D3D3A74/t51.2885-15/sh0.08/e35/c0.135.1080.1080/s640x640/56347818_439423140135260_222436944865078914_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com", ..., ..., ..., "https://scontent-arn2-1.cdninstagram.com/vp/bf0671c779e473fe8312c62674bef6e4/5D3E631A/t51.2885-15/e15/c180.0.720.720/s640x640/54463866_560472434444154_2512477850949351202_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com"]

"""
import random
import requests
import re

def save_10_img(image_url):
    if image_url:
        for i in range(10):
            try:
                filename = img_prefix + str(i) + ".jpg"
                img_url = random.choice(image_url)
                image_url.remove(img_url)
                img_resp = requests.get(img_url)
                with open(filename, 'wb') as f:
                    f.write(img_resp.content)
            except Exception as err:
                print(err)
            else:
                print(filename + " is done")
    else:
        print("Your images url list is empty")

BASE_URL = "https://www.instagram.com/natgeo/"
json_harders = {'image_url':'image-url'}
response = requests.get(BASE_URL)
data = response.text
img_prefix = "nat_geo_"
print(response)
print(data)

# ВАШ КОД НИЖЕ
def get_img_url(http_page):
    urls_list = []
    pic_regex = re.compile(r'(\"src\":\")(.*)(\",\"config_width\":640)')
    find_urls = pic_regex.findall(http_page)
    for url in find_urls[0:9]:
        result = pic_regex.sub('g<2>', url)
        urls_list.append(result)
    return urls_list


nat_geo_img = get_img_url(data)
save_10_img(nat_geo_img)
