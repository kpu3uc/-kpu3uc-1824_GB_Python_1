

def odd_numbers(max_odd):
    for _ in range(1, max_odd + 1, 2):
        yield _


# print(list(odd_numbers(16)))
test = odd_numbers(10)
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
