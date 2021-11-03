# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
from __future__ import annotations


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self) -> str:
        ret = ""
        for row in self.matrix:
            ret += f'| {" ".join(map(str, row))} |\n'
        return ret  # [:-1] - дело вкуса

    def __add__(self, other) -> Matrix:
        if not isinstance(other, Matrix):
            raise ValueError("not Matrix")
        ret = []
        for row, other_row in zip(self.matrix, other.matrix):
            ret.append(list((map(sum, zip(row, other_row)))))
        return Matrix(ret)


test_matrix = Matrix([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
test_matrix2 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(test_matrix, test_matrix2, sep="\n")
print(test_matrix + test_matrix2)
# print(test_matrix + [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] + test_matrix)
print(test_matrix + Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
test_matrix3 = test_matrix + test_matrix2
print(test_matrix3)
test_matrix4 = Matrix([["один", "два", "три", "четыре"], [5, 6, 7, 8], [9, 10, 11, 12]])
print(test_matrix4)
# print(test_matrix + test_matrix4)
