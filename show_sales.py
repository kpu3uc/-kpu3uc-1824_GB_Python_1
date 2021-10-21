import sys

with open('bakery.csv', 'r', encoding='utf-8') as bakery:
    if len(sys.argv) == 1:  # нет параметров - выводим весь список
        print(bakery.read())
    elif len(sys.argv) == 2:  # один параметр - выводим список с нужной строки
        arg1 = int(sys.argv[1])
        _ = 1
        while _ < arg1:  # пропускаем нужное количество строк
            # line = bakery.readline()
            # if not line:
            if not bakery.readline():
                break
            _ += 1
        while True:  # выводим оставшиеся строки
            line = bakery.readline()
            if not line:
                break
            print(line.replace('\n', ''))
    elif len(sys.argv) == 3:  # два параметра - выводим список с нужной до нужной строки
        arg1, arg2 = int(sys.argv[1]), int(sys.argv[2])
        _ = 1
        while _ < arg1:  # пропускаем нужное количество строк
            # line = bakery.readline()
            # if not line:
            if not bakery.readline():
                break
            _ += 1
        while _ <= arg2:  # выводим нужное количество строк
            line = bakery.readline()
            if not line:
                break
            print(line.replace('\n', ''))
            _ += 1
    else:
        sys.exit(1)
