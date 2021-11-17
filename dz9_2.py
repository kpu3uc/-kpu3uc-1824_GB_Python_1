# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    """
    Дорога
    :param length - m
    :param width - m
    :param thickness - cm
    :param mass - kg
    """
    __length, __width, __thickness, __mass = int, int, int, int

    def __init__(self, length, width=7.5, thickness=1, mass=25):
        self.__length = length
        self.__width = width
        self.__thickness = thickness
        self.__mass = mass

    def lay_asphalt(self):
        return self.__length * self.__width * self.__mass * self.__thickness


# narrow_road = Road(50)
# print(narrow_road.lay_asphalt())
# ordinary_road = Road(50, 6)
# print(ordinary_road.lay_asphalt())
# thick_road = Road(50, 6, 10)
# print(thick_road.lay_asphalt())
# rough_road = Road(50, 6, 10, 50)
# print(rough_road.lay_asphalt())
test_road = Road(5000, 20, 5, 25)  # длина, ширина, толщина, масса
print(test_road.lay_asphalt())  # в кг
