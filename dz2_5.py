# import random
# prices = []
prices = [50.41, 70.68, 39, 0.86, 12.57, 28.09, 96.17,
          30.23, 52.22, 25.47, 52.82, 36.43, 20.9, 52.91, 76.67, 41.27, 3.65, 59.49, 7.1, 21.7]
reprices = []
top5prices = []
# while len(prices) < 20:
#     prices.append(round(random.uniform(1, 99), 2))
# print(prices)
#
# prices = [str(item) for item in prices]
# print(prices)
ii = 0

for i in prices:
    fractional_part = round(i % 1, 2)
    integer_part = int(i // 1)
    if fractional_part != 0:
        fractional_part = int(fractional_part * 100)
    # print(item, integer_part, fractional_part)

    integer_part = str(integer_part)
    fractional_part = str(fractional_part)

    if integer_part != 0:
        if len(integer_part) == 1:
            integer_part = "0" + integer_part
    else:
        integer_part = "00"
    integer_part = integer_part + " руб"
    # print(integer_part)

    if fractional_part != 0:
        if len(fractional_part) == 1:
            fractional_part = "0" + fractional_part
    else:
        fractional_part = "00"
    fractional_part = fractional_part + " коп"
    # print(fractional_part)
    item = integer_part + " " + fractional_part
    if ii < len(prices) - 1:
        print(item, end=", ")
    else:
        print(item)
    ii += 1

# print(sorted(prices))

ii = 0

print(id(prices))

for i in sorted(prices):
    fractional_part = round(i % 1, 2)
    integer_part = int(i // 1)
    if fractional_part != 0:
        fractional_part = int(fractional_part * 100)
    # print(item, integer_part, fractional_part)

    integer_part = str(integer_part)
    fractional_part = str(fractional_part)

    if integer_part != 0:
        if len(integer_part) == 1:
            integer_part = "0" + integer_part
    else:
        integer_part = "00"
    integer_part = integer_part + " руб"
    # print(integer_part)

    if fractional_part != 0:
        if len(fractional_part) == 1:
            fractional_part = "0" + fractional_part
    else:
        fractional_part = "00"
    fractional_part = fractional_part + " коп"
    # print(fractional_part)
    item = integer_part + " " + fractional_part
    if ii < len(prices) - 1:
        print(item, end=", ")
    else:
        print(item)
    ii += 1

print(id(prices))

for i in reversed(sorted(prices)):
    # print(i)
    reprices.append(i)

ii = 0

for i in reprices:
    fractional_part = round(i % 1, 2)
    integer_part = int(i // 1)
    if fractional_part != 0:
        fractional_part = int(fractional_part * 100)
    # print(item, integer_part, fractional_part)

    integer_part = str(integer_part)
    fractional_part = str(fractional_part)

    if integer_part != 0:
        if len(integer_part) == 1:
            integer_part = "0" + integer_part
    else:
        integer_part = "00"
    integer_part = integer_part + " руб"
    # print(integer_part)

    if fractional_part != 0:
        if len(fractional_part) == 1:
            fractional_part = "0" + fractional_part
    else:
        fractional_part = "00"
    fractional_part = fractional_part + " коп"
    # print(fractional_part)
    item = integer_part + " " + fractional_part
    if ii < len(prices) - 1:
        print(item, end=", ")
    else:
        print(item)
    ii += 1

ii = 0

for i in reversed(sorted(prices)):
    top5prices.insert(0, i)
    if len(top5prices) == 5:
        break

for i in top5prices:
    fractional_part = round(i % 1, 2)
    integer_part = int(i // 1)
    if fractional_part != 0:
        fractional_part = int(fractional_part * 100)
    # print(item, integer_part, fractional_part)

    integer_part = str(integer_part)
    fractional_part = str(fractional_part)

    if integer_part != 0:
        if len(integer_part) == 1:
            integer_part = "0" + integer_part
    else:
        integer_part = "00"
    integer_part = integer_part + " руб"
    # print(integer_part)

    if fractional_part != 0:
        if len(fractional_part) == 1:
            fractional_part = "0" + fractional_part
    else:
        fractional_part = "00"
    fractional_part = fractional_part + " коп"
    # print(fractional_part)
    item = integer_part + " " + fractional_part
    if ii < len(top5prices) - 1:
        print(item, end=", ")
    else:
        print(item)
    ii += 1
