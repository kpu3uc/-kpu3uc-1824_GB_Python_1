# 4. Реализуйте базовый класс Car.
# У класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    speed = 0
    possible_color = ("white", "black", "red", "green")
    color = possible_color[0]
    name = "Car"
    _is_police = False

    def __init__(self, name: str, color_from_possible: int = 0):
        if color_from_possible in range(len(self.possible_color)):
            self.color = self.possible_color[color_from_possible]
        else:
            raise ValueError("color not possible")
        self.name = name

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        pass

    def show_speed(self):
        return self.speed


class TownCar(Car):
    possible_color = ("white", "black", "red", "green", "orange", "yellow", "blue", "purple", "pink", "gray")
    name = "TownCar"

    def __init__(self, name: str, color_from_possible: int = 0):
        super().__init__(name, color_from_possible)
        if color_from_possible in range(len(self.possible_color)):
            self.color = self.possible_color[color_from_possible]
        else:
            raise ValueError("color not possible")
        self.name = name


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass


test_car = Car("Пусечка", 2)
print(test_car.name, test_car.color, test_car.speed)
test_town_car = TownCar("Утипусечка", 6)
print(test_town_car.name, test_town_car.color, test_town_car.speed)
