"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало
"""

import itertools
import math

def multiply_numbers(names_file, numbers_file, output_file):
    # Открываем файлы с именами и числами на чтение, а файл с результатами на запись
    with open(names_file, 'r') as names_file, open(numbers_file, 'r') as numbers_file, open(output_file, 'w') as output_file:
        # Читаем имена из файла и удаляем лишние пробельные символы
        names = [name.strip() for name in names_file]
        
        # Читаем числа из файла, разделяем их по вертикальной черте (|)
        # и преобразуем каждое число в числовой формат
        numbers = [line.strip().split('|') for line in numbers_file]

        # Используем zip_longest для итерации по именам и числам одновременно
        # Если один из файлов закончится, заполнитель fillvalue будет использован
        for name, (num1, num2) in itertools.zip_longest(names, numbers, fillvalue=None):
            if name is None or num1 is None or num2 is None:
                break

            # Умножаем числа и получаем результат
            result = float(num1) * float(num2)

            # Если результат отрицательный, записываем имя строчными буквами
            # и сохраняем произведение по модулю
            if result < 0:
                name = name.lower()
                result = abs(result)
            # Если результат положительный, записываем имя прописными буквами
            # и округляем произведение до целого
            else:
                name = name.capitalize()
                result = int(result)

            # Записываем имя и произведение в файл результатов
            output_file.write(f"{name} | {result}\n")

    print("Результаты сохранены в файл:", output_file.name)

# Вызываем функцию multiply_numbers с указанием файлов и их расширением
multiply_numbers('names.txt', 'data.txt', 'output.txt')

