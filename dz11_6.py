# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
from __future__ import annotations


class Warehouse:
    name = "Warehouse"

    def __init__(self, name: str):
        self.name = name
        self.storage = {}

    def store(self, *items):
        for item_name in items:
            if isinstance(item_name, OfficeEquipment):
                if item_name.name in self.storage:
                    self.storage[item_name.name] += item_name.count
                else:
                    self.storage[item_name.name] = item_name.count
            else:
                raise ValueError("Not Office Equipment")

    def send(self, item_name, count: int, recipient: Warehouse = None):
        if type(count) != int:
            raise ValueError("Not int")
        if self.storage[item_name] < count:
            raise ValueError("Not enough in stock")
        self.storage[item_name] -= count
        if recipient:
            if not isinstance(recipient, Warehouse):
                raise ValueError("Not Warehouse")
            if item_name in recipient.storage:
                recipient.storage[item_name] += count
            else:
                recipient.storage[item_name] = count


class OfficeEquipment:
    name = "Оргтехника"
    count = 0

    def __init__(self, count=1):
        self.count = count

    # def __repr__(self):
    #     return self.name


class Printer(OfficeEquipment):
    name = "Принтер"


class Scanner(OfficeEquipment):
    name = "Сканер"


class Xerox(OfficeEquipment):
    name = "Ксерокс"


warehouse = Warehouse("Главхран")
omsk = Warehouse("Омское оргохранилище")
xeroxs = Xerox(20)
printers = Printer(15)
scanners = Scanner(10)
print(xeroxs.count, warehouse.storage)
warehouse.store(xeroxs)
print(xeroxs.count, warehouse.storage)
warehouse.store(xeroxs, printers, scanners)
print(warehouse.storage)
warehouse.send("Принтер", 10, omsk)
warehouse.send("Ксерокс", 10)
print(warehouse.storage)
print(omsk.storage)
print()
# warehouse.store("Земля в иллюминаторе")
# warehouse.send("Принтер", "10", omsk)
# warehouse.send("Принтер", 10, omsk)
# warehouse.send("Ксерокс", 10, "saratov")
