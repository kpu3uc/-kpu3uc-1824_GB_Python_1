employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in employees:
    print("Привет, " + i.split().pop(-1).title() + "!")
print(employees)
