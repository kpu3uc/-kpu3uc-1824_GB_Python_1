cube_list = []
cube_sum = 0
cube_sum_2 = 0
i = 0

for i in range(1, 1000, 2):
    cube_list.append(i ** 3)
# print(cube_list)

i = 0

while i <= (len(cube_list)-1):
    divisibility_check = cube_list[i]
    sum_this_digits = 0
    while divisibility_check != 0:
        sum_this_digits += divisibility_check % 10
        divisibility_check = divisibility_check // 10
        # print(sum_this_digits, divisibility_check)
    if sum_this_digits % 7 == 0:
        cube_sum = cube_sum + cube_list[i]
        # print(cube_sum, cube_list[i], i, sum_this_digits)
    i += 1
# print(cube_sum)

i = 0

while i <= len(cube_list) - 1:
    cube_list[i] += 17
    i += 1

i = 0

while i <= (len(cube_list)-1):
    divisibility_check = cube_list[i]
    sum_this_digits = 0
    while divisibility_check != 0:
        sum_this_digits += divisibility_check % 10
        divisibility_check = divisibility_check // 10
        # print(sum_this_digits, divisibility_check)
    if sum_this_digits % 7 == 0:
        cube_sum_2 = cube_sum_2 + cube_list[i]
        print(cube_sum_2, cube_list[i], i, sum_this_digits)
    i += 1
print(cube_sum_2)
