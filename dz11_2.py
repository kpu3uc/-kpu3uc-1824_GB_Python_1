# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


print("Делим одно число на другое")
first_int = input("Введите первое число: ")
second_int = input("Введите второе число: ")

try:
    first_int = int(first_int)
    second_int = int(second_int)
    if second_int == 0:
        raise MyZeroDivisionError("На ноль делить нельзя, я сказал!")
except ValueError:
    print("Вы ввели не число")
except MyZeroDivisionError as err:
    print(err)
else:
    print(f"Получилось {first_int / second_int}")
