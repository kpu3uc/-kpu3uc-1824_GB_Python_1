# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
from __future__ import annotations


class Cotlex:

    def __init__(self, cotlex: complex):
        if isinstance(cotlex, complex):
            self.cotlex = cotlex
        else:
            raise TypeError("not complex")

    def __add__(self, other: Cotlex):
        if isinstance(other, Cotlex):
            return self.cotlex + other.cotlex

    def __mul__(self, other: Cotlex):
        if isinstance(other, Cotlex):
            return self.cotlex * other.cotlex

    def __str__(self):
        return str(self.cotlex)

    def __repr__(self):
        return str(self.cotlex)


print(3 + 7j)
cotlex = Cotlex(3 + 7j)
cotlex2 = Cotlex(4 + 2j)
print(cotlex)
print(type(cotlex))

a = {cotlex}
print(a)
print(cotlex2 + cotlex)
print(cotlex2 * cotlex)
