# 4. Реализуйте базовый класс Car.
# У класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    __speed = 0
    direction = 0  # 0 - прямо, 1 - налево, 2 - направо
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

    def go(self, speed: int = 10):
        self.speed = speed
        return f'{self.name} едет'

    def stop(self):
        self.speed = 0
        return f'{self.name} стоит'

    def turn(self, direction: int = 0):
        if direction == 0:
            self.direction = direction
            return f'{self.name} не поворачивает'
        elif direction == 1:
            self.direction = direction
            return f"{self.name} поворачивает налево"
        elif direction == 2:
            self.direction = direction
            return f"{self.name} поворачивает направо"
        else:
            raise ValueError("unexpected value")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    possible_color = ("white", "black", "red", "green", "orange", "yellow", "blue", "purple", "pink", "gray")
    name = "TownCar"

    def show_speed(self):
        if self.speed <= 40:
            return self.speed
        else:
            return f"{self.speed}, превышаем"


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass


print()
test_car = Car("Пусечка", 2)
print(test_car.name, test_car.color, test_car.show_speed())
print(test_car.go(), test_car.turn(1))
test_town_car = TownCar("Утипусечка", 6)
print(test_town_car.go(110), test_town_car.turn(1))
print(test_town_car.name, test_town_car.color, test_town_car.show_speed())
