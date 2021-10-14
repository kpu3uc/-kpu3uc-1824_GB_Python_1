import requests
from pyquery import PyQuery as pq
from lxml import etree

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def send_request() -> requests.Response:
    """Выполняет запрос данных с ЦБР"""
    response = requests.get(URL, timeout=2)
    if not response.ok:
        print(f'Запрос не успешен: {response.status_code}')
    return response


def extract_data():
    """Извлекает данные и возвращает список string значений"""
    res = send_request()
    main_root = pq(etree.fromstring(res.content))
    curs_val = main_root.pop()
    return [curs_val.xpath(f'//Valute/{"CharCode"}/text()'), curs_val.xpath(f'//Valute/{"Value"}/text()')]


def currency_rates(code: str):  # -> price:float,

    """
    Функция currency_rates(), принимает в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
    возвращает курс этой валюты по отношению к рублю. Использует библиотеку requests. В качестве API
    использует http://www.cbr.ru/scripts/XML_daily.asp

    """
    mm, nn = extract_data()
    ii = 0
    while ii < len(mm):
        # print(mm[ii], nn[ii])
        if code.upper() == mm[ii]:
            rr = nn[ii].replace(",", ".")
            return float(rr)
        ii += 1
