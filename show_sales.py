import sys

with open('bakery.csv', 'r', encoding='utf-8') as bakery:
    if len(sys.argv) == 1:
        print(bakery.read())
    elif len(sys.argv) == 2:
        arg1 = int(sys.argv[1])
        _ = 1
        while _ < arg1:
            line = bakery.readline()
            if not line:
                break
            _ += 1
        while True:
            line = bakery.readline()
            if not line:
                break
            print(line.replace('\n', ''))
    elif len(sys.argv) == 3:
        arg1, arg2 = int(sys.argv[1]), int(sys.argv[2])
        _ = 1
        while _ < arg1:
            line = bakery.readline()
            if not line:
                break
            _ += 1
        while _ <= arg2:
            line = bakery.readline()
            if not line:
                break
            print(line.replace('\n', ''))
            _ += 1
