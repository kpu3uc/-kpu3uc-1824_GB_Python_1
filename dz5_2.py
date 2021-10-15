def odd_numbers(max_odd):
    return(_ for _ in range(1, max_odd + 1, 2))


# print(list(odd_numbers(16)))
test = odd_numbers(10)
print(test)
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))

for _ in odd_numbers(10):
    print(_)