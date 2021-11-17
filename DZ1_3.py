n = 1

while n <= 100:
    case = n % 10
    if case in range(5, 10) or n in range(11, 15) or case == 0:
        print(n, " процентов")
    elif case == 1:
        print(n, " процент")
    else:
        print(n, " процента")
    n += 1
