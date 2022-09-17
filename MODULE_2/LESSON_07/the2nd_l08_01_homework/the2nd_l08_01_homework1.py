# the2nd_l08_01_homework.py

"""
В папке LESSON_08 создать папку the2nd_l08_01_homework. Перейти в папку the2nd_l08_01_homework. И сохранить в ней скрипт the2nd_l08_01_homework.py и два файла .csv: dc-wikia-data.csv, marvel-wikia-data.csv

ЗАДАНИЕ.

1. В сохраненных файлах .csv содержится вся инфорация о героях DC (dc-wikia-data.csv) и MARVEL (marvel-wikia-data.csv)

2. Вам необходимо создать БД (на ваш выбор sqlite3 или postgreSQL) c названием comics.db (или comics для postgreSQL)

3. Создать с помощью кода python и используемого модуля sqlite3 (или psycopg2) внутри БД comics.db две таблицы dc_comics и marvel_comics

4. Напишите python скрипт который сохранит все данные из файлов .csv в таблицы dc_comics и marvel_comics в созданной БД comics

5. Название столбцов заголовка таблиц соответствует заголовкам в .csv файлах 
"""

# Ваш код ниже
import sqlite3, csv, os


combined_db_name = "all_person.db"
dc_db = "dc-wikia-data.csv"
marvel_db = "marvel-wikia-data.csv"



con = sqlite3.connect(combined_db_name)
curs = con.cursor()
try:
    curs.execute(f'''CREATE TABLE IF NOT EXISTS dc_wikia_data(page_id INTEGER, name TEXT, urlslug TEXT, ID TEXT, ALIGN TEXT, EYE TEXT, HAIR TEXT, SEX TEXT, GSM TEXT, ALIVE TEXT, APPEARANCES INTEGER, FIRST APPEARANCE TEXT, YEAR INTEGER) ''')
except Exception as err:
    print(err)   
with open(dc_db) as f:
    pers_list = list(csv.reader(f))
pers_list.pop(0)
for person in pers_list:
    curs.execute('''INSERT INTO dc_wikia_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''',person)
con.commit()
print('Персонажи ДС в таблице dc_wikia_data')


curs = con.cursor()
try:
    curs.execute(f'''CREATE TABLE IF NOT EXISTS marvel_wikia_data(page_id INTEGER, name TEXT, urlslug TEXT, ID TEXT, ALIGN TEXT, EYE TEXT, HAIR TEXT, SEX TEXT, GSM TEXT, ALIVE TEXT, APPEARANCES INTEGER, FIRST APPEARANCE TEXT, YEAR INTEGER) ''')
except Exception as err:
    print(err)   
with open(marvel_db) as f:
    pers_list = list(csv.reader(f))
pers_list.pop(0)
for person in pers_list:
    curs.execute('''INSERT INTO marvel_wikia_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''',person)
con.commit()
print('Персонажи ДС в таблице marvel_wikia_data')