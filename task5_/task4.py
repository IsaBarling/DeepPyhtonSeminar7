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

def create_files_with_extension(extension, folder_path, min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096, num_files=42):
    os.makedirs(folder_path, exist_ok=True)  # Создаем указанную папку, если она не существует

    for i in range(num_files):
        # Генерируем случайное имя файла
        file_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(min_name_length, max_name_length)))

        # Собираем полный путь к файлу с указанным расширением
        file_path = os.path.join(folder_path, f"{file_name}.{extension}")

        # Генерируем случайное количество байт для записи в файл
        file_size = random.randint(min_file_size, max_file_size)

        # Генерируем случайные байты для записи в файл
        file_data = os.urandom(file_size)

        # Записываем данные в файл
        with open(file_path, 'wb') as file:
            file.write(file_data)

        print(f"Создан файл: {file_path} ({file_size} байт)")

def generate_files_with_extensions(extensions, num_files_per_extension, folder_path):
    for extension, num_files in zip(extensions, num_files_per_extension):
        create_files_with_extension(extension, folder_path, num_files=num_files)

# Вызываем функцию generate_files_with_extensions с указанием расширений, количества файлов и папки
folder_path = 'task5.files'
extensions = ['.txt', '.csv', '.json']
num_files_per_extension = [10, 5, 7]
generate_files_with_extensions(extensions, num_files_per_extension, folder_path)



