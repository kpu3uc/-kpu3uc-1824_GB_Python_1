from utils import currency_rates
import sys

if len(sys.argv) == 2:
    exit(currency_rates(sys.argv[1]))
else:
    print(currency_rates(input()))
