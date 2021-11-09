# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    pass


class OfficeEquipment:
    weight = 1
    scan = True
    print = True


class Printer(OfficeEquipment):
    weight = 2
    scan = False
    print = True


class Scanner(OfficeEquipment):
    weight = 3
    scan = True
    print = False


class Xerox(OfficeEquipment):
    weight = 5
    scan = False
    print = True


