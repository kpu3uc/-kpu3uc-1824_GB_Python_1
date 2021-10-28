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
    # print(func)

    def catcher(*args, **kwargs):
        # print("catcher")
        with open("logs.txt", "a", encoding="utf-8") as logs:  # замаскировали - в консоль не идёт, пишется в файл
            logs.write(str(func))
            logs.write("\n")
            for arg in args:
                logs.write(str(arg))
                logs.write(": ")
                logs.write(str(type(arg)))
                logs.write("\n")  # получилось с новой строки, а не через запятую
            for arg in kwargs.values():
                logs.write(str(arg))
                logs.write(": ")
                logs.write(str(type(arg)))
                logs.write("\n")
            logs.write("тип значения функции: ")
            logs.write(str(type(func(*args, **kwargs))))  # тип значения функции
            logs.write("\n")
        return func(*args, **kwargs)
    return catcher


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def multi_args(x, y, u=1):
    return x * y * u


print(calc_cube(5))
# print(multi_args(3, 4, u=10))
