
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 08:14:55 2022

@author: Winuser
"""
#!/usr/bin/env python3

"""
СЛОВА ИЗ СЛОВ
Онлайн пример игры для понимания процесса:
https://ollgames.ru/slova-iz-slova/

ПРАВИЛА ИГРЫ

Цель игры – составить максимальное количество слов из предложенного длинного слова. Каждую букву длинного слова можно использовать в новом слове только один раз. Буквы можно использовать в произвольном порядке. Слова не менее 3-х букв.

Пример:
	Слово: мексиканец
	Буквы (в виде списка): ['м', 'е', 'к', 'с', 'и', 'к', 'а', 'н', 'е', 'ц']
	Возможные варианты: ['иена', 'икс', 'иск', 'каик', 'каин', 'камин', 'кан', 'кекс', 'кениец', 'кика', 'кикс', 'кница', 'маис', 'мак', 'мансиец', 'мекка', 'мексиканец', 'мена', 'миска', 'немец', 'самец', 'сан', 'сема', 'сиамец', 'сиена', 'синец', 'скена', 'смена', 'сцена', 'цена', 'цинк']
	В случае составленного слова выводим определение: иена - ж. Денежная единица Японии.

В требования к игре:
	- 30 % составленных слов для перехода на следующий уровень (округление в большую сторону, то есть 31 слово * 0.3 = 9.3 --> 10, значит для перехода на следующий уровень 10 слов)
	- если все слова составлены, то автоматический переход на следующий уровень (на последнем уровне выводить сообщение все слова составлены, для начала новой игры введите NEW) 
	- слово для уровня должно содержать не менее 30 вариантов (для проверки используйте help_functions.py - описание ниже)
	- игру создать минимум на 10 уровней
	- каждый уровень должен увеличиваться по сложности согласно количеству слов для составления. Например:
			1 уровень: 30 возможных слов (для перехода 9 слов);
			2 уровень: 35 возможных слов (для перехода 11 слов);
			...
			10 уровень: 75 возможных слов (для завершения 23 слова).
	- список слов для игры сохранить в глобальную переменную GAME_WORDS
	- реализовать интерфейс игры:
			NEXT - переход на следующий уровень (если вы угадали нужное количество слов)
			PREVIOUS - переход на предыдущий уровень (если хотите угадать большее количество слов)
			EXIT - выход и сохранение прогресса (для PLAYER)
			NEW - стирает весь прогресс и вы начинаете заново
			RULES - выводит правила игры
			RATING - выводит соотношение составленных слов к общему числу вариантов на текущий уровень (то есть, вы на 3 уровне всего 105 слов, угадано 50 - рейтинг 50 / 105 = 0.48 или 48 %, 
			HELP - выводит команды интерфейса игры
	- предусмотреть возможность сохранения игры (через сохранение в .json файл прогресс игрока, причем имя файла == имя игрока, например:
			имя nick - файл nick.json
	- если имя игрока не найдено (то есть файл json с именем не найден), то начинаем новую игру)
	- если имя игрока найдено (то есть файл json с именем найден), то продолжаем игру с того места где закончили
	- реализация игры через Классы:
		1) Класс Player - класс игрока
		2) Класс Game - класс процесса игры
	- при загрузке игры слова поместить в ГЛОБАЛЬНУЮ ПЕРЕМЕННУЮ WORDS_WITH_DEFINITIONS (далее использовать ее для проверки слов и вывода определений)


Вспомогательные данные:

Дан 1 файл:
1.    nouns.csv - таблица слов из существительных (word) 34263 слов, у каждого слова есть определение (definition), в качестве значения к слову
	пример: 
		"иена": "ж. Денежная единица Японии."
		
		
В файле help_functions.py написаны 3 функции:
1.    check_word(word: str) - функция принимает в качестве аргумента слово (str) и возвращает кортеж из 2-х элементов: (True или False, количество вариантов). Если первый элемент кортежа False, то слово не подходит для игры.
2.    get_word_letters(word: str) - функция принимает в качестве аргумента слово (str) и возвращает список букв в порядке их следования в переданном слове (понадобится для вывода на экран доступных букв)
3.    create_word_list(word: str) - функция принимает в качестве аргумента слово и возвращает список возможных слов, с учетом правила, где каждое слово >= 3 буквы (понадобится для составления списка вариантов слов на каждом уровне)

Профиль игрока:
1. Для создания нового игрока используется class Player:
	class Player:
		def __init__(self, name):
			self.name = name
			self.profile = {}

	Атрибут self.profile имеет структуру:
		
	{
		"current_level" : 1, # номер уровня (int)
		"level_1": {
			"word": "слово уровня 1", # сохранить слово уровня 1
			"letters": "буквы для слова", # используйте вспомогательную функцию
			"variants": 30, # количество вариантов для слова
			"answers": [], # угаданные слова в виде списка
			"guessed": 1, # количество угаданных слов
			"need_to_next_level": 9, # сколько слов до перехода на следующий уровень
			"is_done": False, # Пройден уровень - True, если нет - False (зависит от параметра "need_to_next_level")
			},
			...,
			"level_10": {}, # словарь до 10 уровня
	}

Игровой процесс:
1. Для создания процесса игры используется class Game:
		class Game:
			def __init__(self):
				self.player = Player() # игрок
				self.game_words = GAME_WORDS # слова для уровней игры по возрастанию количества вариантов
				self.word_list_definitions = WORDS_WITH_DEFINITIONS # словарь "слово": "определение"
				self.game_flag = True # управление процессом игры в цикле
				self.rules = '''ПРАВИЛА ИГРЫ
				
				Цель игры – составить максимальное количество слов из предложенного длинного слова. Каждую букву длинного слова можно использовать в новом слове только один раз. Буквы можно использовать в произвольном порядке. Слова не менее 3-х букв.
				
				Пример:
					Слово: мексиканец
					Буквы (в виде списка): ['м', 'е', 'к', 'с', 'и', 'к', 'а', 'н', 'е', 'ц']
					Возможные варианты: ['иена', 'икс', 'иск', 'каик', 'каин', 'камин', 'кан', 'кекс', 'кениец', 'кика', 'кикс', 'кница', 'маис', 'мак', 'мансиец', 'мекка', 'мексиканец', 'мена', 'миска', 'немец', 'самец', 'сан', 'сема', 'сиамец', 'сиена', 'синец', 'скена', 'смена', 'сцена', 'цена', 'цинк']
					В случае составленного слова выводим определение: иена - ж. Денежная единица Японии.'''
				self.command_list = [
					'NEXT',
					'PREVIOUS',
					'EXIT',
					'NEW',
					'RULES',
					'HELP',
					'RATING'
				]
2. В начале игры запрашивается имя игрока, если оно найдено в списке файлов username.json, то игра продолжается с того места, на котором вы остановились
3. Если игрок новый, то начинаете новую игру и все остальные поля игрока заполняются автоматически (self.profile)
4. Далее выведите на экран ПРАВИЛА ИГРЫ
5. После этого выведите номер уровня и СЛОВО, для которого подбираете слова
6. После каждой попытки выводите следующую информацию (можете оформить на свое усмотрение):
	УРОВЕНЬ: 1
	СЛОЖНОСТЬ: ЛЕГКИЙ
	СЛОВО: МЕКСИКАНЕЦ
	ВАРИАНТОВ: 30
	НЕОБХОДИМО УГАДАТЬ: 8
	УГАДАННО СЛОВ: 4
	ДО СЛЕДУЮЩЕГО УРОВНЯ: 4
	БУКВЫ: М Е К С И К А Н Е Ц
	УГАДАННЫЕ СЛОВА: ['иена', 'каин', 'кениец', 'миска']
	ВВЕДИТЕ СЛОВО: смена
	>>> ПОЗДРАВЛЯЕМ, username, Вы угадали!
7. При вводе вводе ключевых слов интерфейса (NEXT, PREVIOUS, NEW, EXIT, RULES, RATING, HELP) выполнять действия, описанные выше.

"""
from help_functions import get_word_letters, check_word, create_word_list, WORDS_WITH_DEFINITIONS
import csv
import json
# Ваш код ниже
import math
from pprint import pprint
GAME_WORDS = ['иезуитство','мексиканец','мистификация','злодейка','многолесье','зрелость','избиратель','игротека','золотоискатель','абитуриентка']

rules = '''ПРАВИЛА ИГРЫ
Цель игры – составить максимальное количество слов из предложенного длинного слова. Каждую букву длинного слова можно использовать в новом слове только один раз. Буквы можно использовать в произвольном порядке. Слова не менее 3-х букв.
Пример:
    Слово: мексиканец
    Буквы (в виде списка): ['м', 'е', 'к', 'с', 'и', 'к', 'а', 'н', 'е', 'ц']
    Возможные варианты: ['иена', 'икс', 'иск', 'каик', 'каин', 'камин', 'кан', 'кекс', 'кениец', 'кика', 'кикс', 'кница', 'маис', 'мак', 'мансиец', 'мекка', 'мексиканец', 'мена', 'миска', 'немец', 'самец', 'сан', 'сема', 'сиамец', 'сиена', 'синец', 'скена', 'смена', 'сцена', 'цена', 'цинк']
    В случае составленного слова выводим определение: иена - ж. Денежная единица Японии.'''
command_list = [
    'NEXT',
    'PREVIOUS',
    'EXIT',
    'NEW',
    'RULES',
    'HELP',
    'RATING'
    ]
help_text = '''NEXT - переход на следующий уровень (если вы угадали нужное
        количество слов)
    PREVIOUS - переход на предыдущий уровень (если хотите угадать
        большее количество слов)
    EXIT - выход и сохранение прогресса (для PLAYER)
    NEW - стирает весь прогресс и вы начинаете заново
    RULES - выводит правила игры
    RATING - выводит соотношение составленных слов к общему числу
        вариантов на текущий уровень (то есть, вы на 3 уровне всего 105 слов, угадано 50 -
        рейтинг 50 / 105 = 0.48 или 48 %,
    HELP - выводит команды интерфейса игры'''


class Player: #Инициация игрока
    def __init__(self):
        self.name = name_input
        self.profile = {}
        self.file_name = f'{self.name}.json'
        try:
            with open(self.file_name, 'r', encoding="utf-8") as file:
                self.profile = json.load(file)
                
        except:
            self.profile = {f"level_{k}": {"word": "","letters": "","variants": 0,"answers": [],"guessed": 0,"need_to_next_level": 0,"is_done": False} for k in range(1,11,1)}
            self.profile.update({'current_level' : 1})
    def save_profile(self, profile):  #сохранение в файл
        self.file_name = f'{name_input}.json'
        self.profile = profile
        with open(self.file_name, 'w', encoding="utf-8") as file:
            json.dump(self.profile, file,ensure_ascii = False)


class Game:
    def __init__(self):
        self.player = Player() # игрок
        self.profile = self.player.profile
        self.game_words = GAME_WORDS # слова для уровней игры по возрастанию количества вариантов
        self.word_list_definitions = WORDS_WITH_DEFINITIONS # словарь "слово": "определение"
        self.game_flag = True # управление процессом игры в цикле
        
    def compari(self, word , word_to_comp): #проверка слова
        self.word_to_comp = word_to_comp
        self.word_list = create_word_list(word)
        for word_user in self.word_list:
            if self.word_to_comp == word_user:
                return 1
                break
        return 0

    def profile_out(self, current_level, complexity): #вывод на экран прогресса уровня
        pprint(
        {'УРОВЕНЬ': self.profile['current_level'],
        'СЛОЖНОСТЬ': complexity,
        'СЛОВО': self.current_level['word'],
        'ВАРИАНТОВ': self.current_level['variants'],
        'НЕОБХОДИМО УГАДАТЬ': self.current_level['need_to_next_level'],
        'УГАДАННО СЛОВ': self.current_level['guessed'],
        'ДО СЛЕДУЮЩЕГО УРОВНЯ': self.current_level['need_to_next_level'] - self.current_level['guessed'],
        'БУКВЫ': self.current_level['letters'],
        'УГАДАННЫЕ СЛОВА': self.current_level['answers'],
        })

    def actual_word_lvl(self):
        self.level = self.profile['current_level'] #уровень
        self.word = GAME_WORDS[int(self.level) - 1] #cлово из списка слов по уровню

    def comand_action(self):
        if self.word_to_comp.lower() == 'next':
            if self.current_level['is_done'] == True or self.profile['current_level'] == 10:
                self.profile['current_level'] += 1
                self.level_flag == False
            else:
                print('Дальше нельзя!')
        elif self.word_to_comp == 'previous':
            if self.profile['current_level'] == 1:
                print('Уровня 0 не существует!')
            else:
                self.profile['current_level'] -= 1
                self.level_flag == False
        elif self.word_to_comp == 'exit':
            Player.save_profile(self, self.profile)
            self.level_flag = False
            self.game_flag = False
            print('Произошло сохранение, досвидания!')
        elif self.word_to_comp == 'new':
            self.current_level['answers'] = []
            self.current_level['guessed'] = 0
            self.current_level['need_to_next_level'] = math.ceil(self.variants * 0.3)
        elif self.word_to_comp == 'rules':
            print(rules)
        elif self.word_to_comp == 'help':
            print(help_text)
        elif self.word_to_comp == 'rating':
            rating = round((self.current_level['guessed'] / self.variants),2) * 100
            print(f'угадано {int(rating)}%')

    def complexity_identif(self):
        if self.current_level['need_to_next_level'] == 0:
            self.current_level['need_to_next_level'] = math.ceil(self.variants * 0.3)
        if self.profile['current_level'] in range(1,9,1):
            complexity = self.profile['current_level']
        elif self.profile['current_level'] == 9:
            complexity = 'Нереально'
        elif self.profile['current_level'] == 10:
            complexity = 'Ультранереально'
        return complexity

    def can_go_next_lvl(self):
        answer = False
        while answer == False:
            self.level_ansver = input('вы прошли уровень! желаете перейти на следующий?\n').lower()
            if self.level_ansver == 'да':
                self.level_flag == False
                self.current_level['is_done'] = True
                self.profile['current_level'] += 1
                Player.save_profile(self, self.profile)
                answer = True
            elif self.level_ansver == 'нет':
                answer = True

    def game_play(self):
        while self.game_flag == True: #цикл игры
            Game.actual_word_lvl(self) #считает уровень и слово из профиля при загрузки игры
            print(f"Уровень - {self.level}")
            print(f"Слово {self.word}")
            self.level_flag = True
            
            while self.level_flag == True: #цикл уровня
                Game.actual_word_lvl(self )#считает уровень и слово из профиля во время игры
                self.current_level = self.profile[f'level_{self.profile["current_level"]}']
                self.variants = len(create_word_list(self.word)) #кол-во вариантов
                self.current_level['word'] = self.word
                self.current_level['letters'] = get_word_letters(self.word)
                self.current_level['variants'] = self.variants
                
                complexity = Game.complexity_identif(self)
                Game.profile_out(self, self.profile, complexity)   #вывод на экран прогресса уровня
                
                self.word_to_comp = input('Ведите слово:\n').lower()
                self.word_compari = Game.compari(self, self.current_level['word'], self.word_to_comp)
                
                if self.word_to_comp.upper() in command_list: #проверка на слово для команды
                    Game.comand_action(self)
                    continue       # чтобы слово не проверялось далее
                    
                if self.word_compari == 1 and self.word_to_comp not in self.current_level['answers']: #если слово верное и не повторное
                    print(self.word_to_comp, ':', self.word_list_definitions[self.word_to_comp])
                    self.current_level['answers'].append(self.word_to_comp)
                    self.current_level['guessed'] += 1
                    if self.current_level['need_to_next_level'] <= 0: #если игрок угадывает больше слов чем нужно число не уходит в -
                        self.current_level['need_to_next_level'] = 0
                else:
                    print('слово не подходит')
                    
                if self.current_level['guessed'] >= math.ceil(self.variants * 0.3): #если достигнуто кол-во ответов для перехода на след лвл
                    Game.can_go_next_lvl(self)
            self.game_flag = False


name_input = input('Веведите имя игрока\n')


g = Game()
g.game_play()


