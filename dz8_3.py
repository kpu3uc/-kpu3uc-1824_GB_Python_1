# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
    # print("init")

    def catcher(*args, **kwargs):
        # print("catcher")
        with open("log.txt", "a", encoding="utf-8") as logs:  # замаскировали - в консоль ничего не идёт, пишется в файл
            logs.write(str(*args, **kwargs))
            logs.write(": ")
            logs.write(str(type(*args)))
            logs.write(" , типа значения функции: ")
            logs.write(str(type(func(*args, **kwargs))))  # тип значения функции
            logs.write("\n")
        return func(*args, **kwargs)

    return catcher


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
