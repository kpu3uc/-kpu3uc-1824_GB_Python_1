# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data: str):
        pass

    @staticmethod
    def convert(data: str):
        day, month, year = data.split("-")
        return int(day), int(month), int(year)

    @classmethod
    def verification(cls, data: str):
        from datetime import datetime
        day, month, year = cls.convert(data)
        try:
            valid_data = datetime(year, month, day)
            ret = True
        except ValueError:
            ret = False
        return ret


print(Data.convert("29-02-1982"))
print(Data.verification("29-02-1900"))
print(Data.verification("29-02-2000"))
print(Data.verification("12-34-5678"))
