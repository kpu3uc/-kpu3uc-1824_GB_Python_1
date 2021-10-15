# ### 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего,
# например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```
#
# Подсказка: использовать возможности python, изученные на уроке.
from time import perf_counter
from numpy import random

# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

src = [random.randint(100) for _ in range(1, 100000)]
# print(src)

start = perf_counter()
result = [y for i, y in enumerate(src) if y > src[i-1]]  # неправильный вариант, но было весело
# print(result, perf_counter() - start)
print(perf_counter() - start)

start = perf_counter()
result = [y for i, y in zip(src, src[1:]) if y > i]  # мой вариант быстрее
# print(result, perf_counter() - start)
print(perf_counter() - start)

start = perf_counter()
result = [src[i + 1] for i in range(len(src) - 1) if src[i + 1] > src[i]]  # подсмотрено у чатика
# print(result, perf_counter() - start)
print(perf_counter() - start)
