# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
# из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.
cont = {}

with open("nginx_logs.txt", encoding="utf-8") as logs:
    while True:
        line = logs.readline()
        if not line:
            break
        remote_addr, *trash = line.split()
        if remote_addr in cont:
            cont[remote_addr] += 1
        else:
            cont = {remote_addr: 1}
