# 5. Продолжить работу над первым заданием. Разработайте методы,
# которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
# from __future__ import annotations
#
#
# class Warehouse:
#     name = "Warehouse"
#
#     def __init__(self, name: str):
#         self.name = name
#         self.storage = {}
#
#     def store(self, *items):
#         for item_name in items:
#             if isinstance(item_name, OfficeEquipment):
#                 if item_name.name in self.storage:
#                     self.storage[item_name.name] += item_name.count
#                 else:
#                     self.storage[item_name.name] = item_name.count
#
#     def send(self, item_name, count: int, recipient: Warehouse = None):
#         self.storage[item_name] -= count
#         if recipient:
#             if item_name in recipient.storage:
#                 recipient.storage[item_name] += count
#             else:
#                 recipient.storage[item_name] = count
#
#
# class OfficeEquipment:
#     name = "Оргтехника"
#     count = 0
#
#     def __init__(self, count=1):
#         self.count = count
#
#     # def __repr__(self):
#     #     return self.name
#
#
# class Printer(OfficeEquipment):
#     name = "Принтер"
#
#
# class Scanner(OfficeEquipment):
#     name = "Сканер"
#
#
# class Xerox(OfficeEquipment):
#     name = "Ксерокс"
#
#
# warehouse = Warehouse("Главхран")
# omsk = Warehouse("Омское оргохранилище")
# xeroxs = Xerox(20)
# printers = Printer(15)
# scanners = Scanner(10)
# print(xeroxs.count, warehouse.storage)
# warehouse.store(xeroxs)
# print(xeroxs.count, warehouse.storage)
# warehouse.store(xeroxs, printers, scanners)
# print(warehouse.storage)
# warehouse.send("Принтер", 10, omsk)
# print(warehouse.storage)
# print(omsk.storage)
# print()
