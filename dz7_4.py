# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи —
# верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов
# (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os
import random
import string
from copy import copy
# print(os.walk("some_data"))

target_folder = "some_data"


def grs(length):
    """Генератор строки"""
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def counter(path: str):
    """Возвращает список длин файлов в директории"""
    return_data = []
    for test_file in os.walk(path):
        # print(test_file)
        for file in test_file[2]:
            # print(file)
            # print(os.stat(test_file[0] + "\\" + file).st_size)
            return_data.append(os.stat(test_file[0] + "\\" + file).st_size)
            # print(return_data)
    return return_data


def fofile_gen(path: str, folders: int, files: int, size_min=1, size_max=10000):
    """Генератор папок, файлов в них и содержимого файлов, использует grs"""
    if os.path.exists(path):  #
        exit(1)
    while folders > 0:
        temp_name_folder = grs(8)
        # print(temp_name)
        os.makedirs(path + "\\" + temp_name_folder)
        temp_file = copy(files)
        while temp_file > 0:
            temp_name_file = grs(8)
            with open(path + "\\" + temp_name_folder + "\\" + temp_name_file, 'a') as random_file:
                random_file.write(grs(random.randint(size_min, size_max)))
            temp_file -= 1
        folders -= 1


fofile_gen(target_folder, 10, 10)


result = counter(target_folder)
# print(result)
final_dict = {}
for _ in result:
    a = 10
    while True:
        if _ < a:
            if a in final_dict:
                final_dict[a] += 1
            else:
                final_dict[a] = 1
            break
        a *= 10
print(final_dict)






