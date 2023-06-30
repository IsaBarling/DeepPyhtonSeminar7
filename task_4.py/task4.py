"""
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""

import os
import random
import string

def create_files_with_extension(extension, min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096, num_files=42):
    folder_name = 'task4_'
    os.makedirs(folder_name, exist_ok=True)  # Создаем папку task4_, если она не существует

    for i in range(num_files):
        # Генерируем случайное имя файла
        file_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(min_name_length, max_name_length)))

        # Собираем полный путь к файлу с указанным расширением
        file_path = os.path.join(folder_name, f"{file_name}.{extension}")

        # Генерируем случайное количество байт для записи в файл
        file_size = random.randint(min_file_size, max_file_size)

        # Генерируем случайные байты для записи в файл
        file_data = os.urandom(file_size)

        # Записываем данные в файл
        with open(file_path, 'wb') as file:
            file.write(file_data)

        print(f"Создан файл: {file_path} ({file_size} байт)")

# Вызываем функцию create_files_with_extension с указанием расширения и необязательными параметрами
create_files_with_extension('.txt', min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096, num_files=42)

