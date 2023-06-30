"""
Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""



import os

directory = r'D:\Github5\seminar7\task4'
desired_name = 'renamed_new_file'
num_digits = 3
source_extension = '.txt'
target_extension = '.csv'
name_range = [3, 6]

def batch_rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range=None):
    file_counter = 1

    for file_name in os.listdir(directory):
        if file_name.endswith(source_extension):
            source_file_path = os.path.join(directory, file_name)

            if name_range:
                start_index, end_index = name_range
                original_name = file_name[start_index-1:end_index]
                new_file_name = f"{original_name}_{desired_name}_{file_counter:0{num_digits}}{target_extension}"
            else:
                new_file_name = f"{desired_name}_{file_counter:0{num_digits}}{target_extension}"

            target_file_path = os.path.join(directory, new_file_name)

            os.rename(source_file_path, target_file_path)
            print(f"Переименован файл: {source_file_path} -> {target_file_path}")

            file_counter += 1



batch_rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range)

