# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

# import dz7_2
# dz7_2
import os
from shutil import copy

project = "my_project"
if not os.path.exists(project):  # проекта нет - выходим
    exit(1)
if os.path.exists(project + "/templates"):  # уже существует папка templates, выходим
    exit(1)
# os.mkdir(project + "/templates")
for path in os.walk(project):  # для каждой папки в проекте
    # print(path)
    if "templates" in path[1]:  # проверяем, есть ли там папка с шаблонами
        # print("catch")
        for copy_path in os.walk(path[0] + "\\templates"):
            # print("copy", copy_path)
            for file in copy_path[2]:
                trash, temp_name = path[0].split("\\")
                temp_path = project + "\\templates\\" + temp_name
                # print("temp_path", temp_path)
                os.makedirs(temp_path) if not os.path.exists(temp_path) else ...
                copy(copy_path[0] + "\\" + file, temp_path)
