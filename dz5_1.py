# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

def odd_numbers(max_odd):
    """генератор нечетных чисел от одного до max_odd"""
    for _ in range(1, max_odd + 1, 2):
        yield _


# print(list(odd_numbers(16)))
# test = odd_numbers(10)
# print(test)
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))

for _ in odd_numbers(10):
    print(_)
