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

# делаем тупо структуру c полными путями, первые уровни впереди,
# вторичные во вторую очередь, третичные - в третью.
import os

with open("config.yaml", encoding="utf-8") as config:
    while True:
        line = config.readline().replace('\n', '')
        if not line:
            break
        if not os.path.exists(line):
            if "." in line:
                open(line, 'a').close()
            else:
                os.mkdir(line)
