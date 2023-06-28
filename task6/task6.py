"""
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

import os
import random
import string

def generate_pseudo_names(filename, num_names):
    vowels = 'AEIOU'
    consonants = ''.join(set(string.ascii_uppercase) - set(vowels))

    with open(filename, 'w') as file:
        for _ in range(num_names):
            name_length = random.randint(4, 7)
            name = random.choice(vowels)

            for _ in range(name_length - 1):
                if len(name) % 2 == 0:
                    name += random.choice(consonants)
                else:
                    name += random.choice(vowels)

            file.write(name + '\n')

def multiply_numbers(names_file, numbers_file, result_file):
    with open(names_file, 'r') as names, open(numbers_file, 'r') as numbers, open(result_file, 'w') as result:
        for name, number in zip(names, numbers):
            name = name.strip()
            number = float(number)

            product = name.lower() if number < 0 else name.upper()
            product += " | " + str(abs(int(number))) if number < 0 else " | " + str(round(number))

            result.write(product + '\n')

def create_files_with_extension(extension, folder_path, min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096, num_files=42):
    os.makedirs(folder_path, exist_ok=True)

    existing_files = os.listdir(folder_path)

    for i in range(num_files):
        file_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(min_name_length, max_name_length)))
        file_path = os.path.join(folder_path, f"{file_name}.{extension}")

        if file_path in existing_files:
            continue

        file_size = random.randint(min_file_size, max_file_size)
        file_data = os.urandom(file_size)

        with open(file_path, 'wb') as file:
            file.write(file_data)

        print(f"Создан файл: {file_path} ({file_size} байт)")

def generate_files_with_extensions(extensions, num_files_per_extension, folder_path):
    os.makedirs(folder_path, exist_ok=True)

    for extension, num_files in zip(extensions, num_files_per_extension):
        create_files_with_extension(extension, folder_path, num_files=num_files)

folder_path = 'task6'
extensions = ['.txt', '.csv', '.json']
num_files_per_extension = [10, 5, 7]
generate_files_with_extensions(extensions, num_files_per_extension, folder_path)
