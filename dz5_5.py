# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов
# список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
from time import perf_counter
from numpy import random
from collections import Counter

# li_ra = 10000
# li_uni = 100
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def test_three(li_ra: int, li_uni: int):
    """
    обернул в функцию чтобы потестить разные значения длины списка и количества уникальных значений
    li_ra - количество элементов в списке, li_uni - количество уникальных значений
    """
    src = [random.randint(100) for _ in range(1, li_ra - li_uni)]
    # print(src)
    for _ in range(li_uni):
        src.insert(random.randint(li_ra), 100 + _)
    # print(src)

    start = perf_counter()
    result = [_ for _ in src if src.count(_) == 1]  # решение "в лоб": добавляется каждый элемент которого в списке
    # print(result, perf_counter() - start)         # только одна штука
    rez_out1 = (perf_counter() - start)

    start = perf_counter()
    set_src = set()
    result = []
    for _ in src:                                   # второй вариант
        if _ not in set_src:                        # если элемент ещё не встречался в множестве, тогда:
            set_src.add(_)                          # добавим в множество
            if src.count(_) == 1:                   # узнаем, он один такой в списке
                result.append(_)                    # если да - добавляем, если нет - пропускаем
    # print(result, perf_counter() - start)         # если элемент уже есть в множестве, значит делать с ним ничего не надо
    rez_out2 = (perf_counter() - start)

    start = perf_counter()
    set_src = set()
    result = []
    for __, _ in enumerate(src):                    # третий вариант
        if _ not in set_src:                        # если элемент ещё не встречался в множестве, тогда:
            set_src.add(_)                          # добавим в множество
            if _ not in src[__+1::]:                # узнаём, не встречается ли он в остатке списка
                result.append(_)                    # если да, не встречается - добавляем
    # print(result, perf_counter() - start)
    rez_out3 = (perf_counter() - start)

    start = perf_counter()
    result = []
    set_count = Counter(src)                        # четвертый вариант через Counter
    for _ in src:
        if set_count[_] == 1:
            result.append(_)
    # print(result, perf_counter() - start)
    rez_out4 = (perf_counter() - start)
    print(li_ra, li_uni, round(rez_out1, 4), round(rez_out2, 4), round(rez_out3, 4), round(rez_out4, 4))


test_three(20, 5)              # 20     5      0.0      0.0      0.0      0.0
test_three(100, 10)            # 100    10     0.0001   0.0001   0.0001   0.0
test_three(100, 20)            # 100    20     0.0001   0.0001   0.0001   0.0
test_three(500, 20)            # 500    20     0.0025   0.0006   0.0003   0.0001
test_three(500, 100)           # 500    100    0.0024   0.0009   0.0005   0.0001
test_three(1000, 100)          # 1000   100    0.0092   0.0019   0.001    0.0001
test_three(10000, 10)          # 10000  10     0.9922   0.0103   0.0028   0.0008
test_three(10000, 100)         # 10000  100    0.9229   0.019    0.0078   0.0008
# test_three(100000, 100)      # 100000 100    92.8828  0.1837   0.0908   0.0089
test_three(10, 10)             # 10     10     0.0      0.0      0.0      0.0
test_three(100, 100)           # 100    100    0.0001   0.0001   0.0001   0.0
test_three(500, 500)           # 500    500    0.0022   0.0024   0.002    0.0001
test_three(1000, 1000)         # 1000   1000   0.0087   0.0098   0.0059   0.0002
test_three(10000, 10000)       # 10000  10000  1.0454   1.051    0.6852   0.0015
# test_three(100000, 100000)   # 100000 100000 184.6781 171.4175 109.6687 0.0249
test_three(1000, 0)            # 1000   0      0.0086   0.0009   0.0003   0.0001
test_three(10000, 0)           # 10000  0      0.9061   0.009    0.0022   0.0009
# test_three(100000, 0)        # 100000 0      91.922   0.0915   0.0288   0.009
