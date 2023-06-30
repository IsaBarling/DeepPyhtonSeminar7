"""
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""


import random

def fill_file_with_random_pairs(filename, num_lines):
    with open(filename, 'a') as file:
        for _ in range(num_lines):
            # Генерируем случайные числа
            first_num = random.randint(-1000, 1000)
            second_num = random.uniform(-1000, 1000)

            # Записываем числа в файл
            file.write(f"{first_num}|{second_num}\n")

fill_file_with_random_pairs("data.txt", 100)
