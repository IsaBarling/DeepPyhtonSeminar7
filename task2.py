"""
Задание №2
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""


import random
import string

def generate_pseudo_names(filename, num_names):
    vowels = 'AEIOU'  # Гласные буквы
    consonants = ''.join(set(string.ascii_uppercase) - set(vowels))  # Согласные буквы

    with open(filename, 'w') as file:
        for _ in range(num_names):
            name_length = random.randint(4, 7)  # Длина имени от 4 до 7 символов
            name = random.choice(vowels)  # Начинаем имя с гласной

            # Добавляем оставные символы
            for _ in range(name_length - 1):
                if len(name) % 2 == 0:
                    name += random.choice(consonants)
                else:
                    name += random.choice(vowels)

            # Записываем имя в файл
            file.write(name.capitalize() + '\n')

generate_pseudo_names("names.txt", 100)

