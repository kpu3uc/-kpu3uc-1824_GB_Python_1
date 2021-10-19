# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

par_log = []

with open("nginx_logs.txt", encoding="utf-8") as logs:
    while True:
        line = logs.readline()
        if not line:
            break
        remote_addr, trash, trash, trash, trash, request_type, requested_resource, *trash = line.split()
        # print(remote_addr, request_type, requested_resource)
        par_log.append((remote_addr, request_type[1:100500], requested_resource))
print(par_log)
