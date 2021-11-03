# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
from abc import ABC


class Clothes(ABC):
    flag = 0

    def __init__(self, name: str, vh: int):
        self.name = name
        self.vh = vh

    def formula(self):
        if self.flag == 1:
            return self.vh/6.5 + 0.5
        elif self.flag == 2:
            return 2*self.vh + 0.3
        else:
            return ValueError

    def calculation(self):
        return self.formula()


class Coat(Clothes):
    flag = 1


class Suit(Clothes):
    flag = 2


coat = Coat("kurtka", 10)
print(coat.calculation())
suit = Suit("kostum", 10)
print(suit.calculation())
