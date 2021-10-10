import random
# duration = 53
# duration = 153
# duration = 4153
# duration = 400153
# duration = int(input('введите количество секунд: '))
duration = random.randint(1, 599999)
# print(duration)
if duration != 86400:
    d = duration // 86400
else:
    d = 1
if duration != 3600:
    h = (duration % 86400) // 3600
else:
    h = 1
if duration != 60:
    m = ((duration % 86400) % 3600) // 60
else:
    m = 1
s = ((duration % 86400) % 3600) % 60

if duration >= 86400:
    print(d, "дн", h, "час", m, "мин", s, "сек")
elif duration >= 3600:
    print(h, "час", m, "мин", s, "сек")
elif duration >= 60:
    print(m, "мин", s, "сек")
else:
    print(s, "сек")
