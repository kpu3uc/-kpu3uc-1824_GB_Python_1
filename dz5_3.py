tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', "Роза", "Упала", "На", "Лапу", "Азор"
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def cortage_gen():
    _ = 0
    while _ < len(tutors):
        if _ < len(klasses):
            yield tutors[_], klasses[_]
            _ += 1
        else:
            yield tutors[_], None
            _ += 1


print(cortage_gen())
for _ in cortage_gen():
    print(_)
