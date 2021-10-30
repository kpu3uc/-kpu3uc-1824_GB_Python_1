# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    name: str = "Пахом"
    surname: str = "Иванов"
    position: str = "дворник"
    wage, bonus = 10, 10
    __income: dict = {"wage": wage, "bonus": bonus}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.__income = {"wage": wage, "bonus": bonus}

    def get_wage(self):
        return self.__income["wage"]

    def get_income(self):
        return self.__income["bonus"]


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self.get_wage() + self.get_income()


test_worker = Worker("Кирилл", "Лыков", "монтировщик", 5000, 1000)
test_position = Position("Ирина", "Лыкова", "актриса", 8000, 2000)

print(f'{test_worker.name} {test_worker.surname}, {test_worker.position}: {test_worker.get_wage() + test_worker.bonus}')
print(f'{test_position.get_full_name()}, {test_position.position}: {test_position.get_total_income()}')
