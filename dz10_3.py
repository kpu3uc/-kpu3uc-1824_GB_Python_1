# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__, __truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# округление до целого числа деления клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять,
# только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
# В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.
from __future__ import annotations


class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other) -> Cell:
        if not isinstance(other, Cell):
            raise ValueError("not Cell")
        return Cell(self.count + other.count)

    def __sub__(self, other) -> Cell:
        if not isinstance(other, Cell):
            raise ValueError("not Cell")
        if self.count <= other.count:
            raise ValueError("zero or less")
        return Cell(self.count - other.count)

    def __mul__(self, other) -> Cell:
        if not isinstance(other, Cell):
            raise ValueError("not Cell")
        return Cell(self.count * other.count)

    def __floordiv__(self, other) -> Cell:
        if not isinstance(other, Cell):
            raise ValueError("not Cell")
        return Cell(self.count // other.count)

    def __truediv__(self, other) -> Cell:
        if not isinstance(other, Cell):
            raise ValueError("not Cell")
        return Cell(self.count // other.count)  # всё равно делим нацело, у нас int

    def make_order(self, row):
        ret = ""
        count = self.count
        while count > row:
            count -= row
            ret += f'{"*" * row}\n'
        ret += f'{"*" * count}'
        return ret


cell1 = Cell(3)
cell2 = Cell(10)
cell3 = cell1 + cell2
print(f'{cell1.count} + {cell2.count} = {cell3.count}')
print(5, cell3.make_order(5), sep="\n")
cell3 = cell1 * cell2
print(f'{cell1.count} * {cell2.count} = {cell3.count}')
print(11, cell3.make_order(11), sep="\n")
cell3 = cell1 / cell2
print(f'{cell1.count} / {cell2.count} = {cell3.count}')
print(5, cell3.make_order(5), sep="\n")
cell3 = cell1 // cell2
print(f'{cell1.count} // {cell2.count} = {cell3.count}')
print(5, cell3.make_order(5), sep="\n")
cell3 = cell2 / cell1
print(f'{cell2.count} / {cell1.count} = {cell3.count}')
print(2, cell3.make_order(2), sep="\n")
cell3 = cell2 // cell1
print(f'{cell2.count} // {cell1.count} = {cell3.count}')
print(1, cell3.make_order(1), sep="\n")
# cell3 = cell1 - cell2
# print(f'{cell1.count} - {cell2.count} = {cell3.count}')
cell3 = cell2 - cell1
print(f'{cell2.count} - {cell1.count} = {cell3.count}')
print(5, cell3.make_order(5), sep="\n")
print(f'10 + 5 =\n{(Cell(10) + Cell(5)).make_order(5)}')

