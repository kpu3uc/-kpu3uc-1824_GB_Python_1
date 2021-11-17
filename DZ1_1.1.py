import random
i = 0
number_of_values = 2
duration = []
# duration = [53, 66]
# duration = [153, 166]
# duration = [4153, 4166]
# duration = [400153, 400166]
# duration[0] = int(input('введите первое количество секунд: '))
# duration[1] = int(input('введите второе количество секунд: '))
while i <= number_of_values - 1:
    duration.append(random.randint(1, 599999))
    i += 1
print(duration)

i = 0

while i <= number_of_values - 1:
    if duration[i] != 86400:
        d = duration[i] // 86400
    else:
        d = 1
    if duration[i] != 3600:
        h = (duration[i] % 86400) // 3600
    else:
        h = 1
    if duration[i] != 60:
        m = ((duration[i] % 86400) % 3600) // 60
    else:
        m = 1
    s = ((duration[i] % 86400) % 3600) % 60

    if duration[i] >= 86400:
        print(d, "дн", h, "час", m, "мин", s, "сек")
    elif duration[i] >= 3600:
        print(h, "час", m, "мин", s, "сек")
    elif duration[i] >= 60:
        print(m, "мин", s, "сек")
    else:
        print(s, "сек")
    i += 1
