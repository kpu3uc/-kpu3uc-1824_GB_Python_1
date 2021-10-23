# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе
# «руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

# структура config.yaml у нас c полными путями, первые уровни впереди,
# вторичные во вторую очередь, третичные - в третью.
import os

with open("config.yaml", encoding="utf-8") as config:
    while True:
        line = config.readline().replace('\n', '')  # правила нашего config.yaml говорят что там нет пустых строк
        if not line:                                # и неправильных данных :pokerface:
            break
        if not os.path.exists(line):
            if "." in line:                         # правила нашего config.yaml говорят что:
                open(line, 'a').close()             # файлы у нас с точками в названии
            else:
                os.mkdir(line)                      # папки у нас без точек в названии
