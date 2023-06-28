"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""


import os
import random
import string
from task4 import create_files_with_extension

def generate_files_with_extensions(extensions, num_files_per_extension):
    folder_path = os.path.dirname(os.path.abspath(__file__))  # Путь к папке, содержащей файл с кодом

    # Создание папки "task5.files" (если она не существует)
    task5_folder_path = os.path.join(folder_path, "task5.files")
    if not os.path.exists(task5_folder_path):
        os.makedirs(task5_folder_path)

    for extension, num_files in zip(extensions, num_files_per_extension):
        create_files_with_extension(extension, num_files=num_files, folder_path=task5_folder_path)

# Вызов функции generate_files_with_extensions с указанием расширений и количества файлов
extensions = ['.txt', '.csv', '.jpg', '.py']
num_files_per_extension = [10, 5, 3, 7]
generate_files_with_extensions(extensions, num_files_per_extension)

