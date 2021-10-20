import sys

with open('bakery.csv', 'a', encoding='utf-8') as bakery:
    bakery.writelines(sys.argv[1] + "\n") if len(sys.argv) == 2 else sys.exit(1)
