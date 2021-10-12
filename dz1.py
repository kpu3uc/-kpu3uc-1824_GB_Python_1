# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
# возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
# браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
# величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей
# от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

import requests
import sys
from pyquery import PyQuery as pq
from lxml import etree


URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def send_request() -> requests.Response:
    """Выполняет запрос данных с ЦБР"""
    response = requests.get(URL, timeout=2)
    if not response.ok:
        print(f'Запрос не успешен: {response.status_code}')
        sys.exit(0)
    return response


def extract_data():
    """Извлекает данные из соответствующего тега и возвращает список string значений"""
    tag1, tag2 = "CharCode", "Value"
    res = send_request()
    main_root = pq(etree.fromstring(res.content))
    curs_val = main_root.pop()
    return [curs_val.xpath(f'//Valute/{tag1}/text()'), curs_val.xpath(f'//Valute/{tag2}/text()')]


# if __name__ == '__main__':
#     # пример использования
#     name_valutes = extract_data('Name')
#     pprint(name_valutes)


def currency_rates(code: str):

    """
    Функция currency_rates(), принимает в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
    возвращает курс этой валюты по отношению к рублю. Использует библиотеку requests. В качестве API
    использует http://www.cbr.ru/scripts/XML_daily.asp
    :return:
    """
    mm, nn = extract_data()
    ii = 0
    while ii < len(mm):
        # print(mm[ii], nn[ii])
        if code.upper() == mm[ii]:
            return nn[ii]
        ii += 1
    #     curr_dic = {ii: nn}
    #     print(curr_dic)


# print(extract_data())
# i, n = extract_data()
# print(i, n)
print("usd", currency_rates("usd"))
print("EUR", currency_rates("EUR"))
