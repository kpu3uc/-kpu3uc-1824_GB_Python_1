# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    """Светофор"""
    __color = {"Red": .7, "Yellow": 2, "Green": 1}  # для теста красный у нас .7

    def __init__(self, green_time=1):
        self.__color["Green"] = green_time

    def running(self, log=False):
        if self.__color.keys() != {"Red", "Yellow", "Green"}:
            raise ValueError("Internal color dict error")
        for keys in self.__color.items():
            print(keys[0], keys[1]) if log else print(keys[0])
            time.sleep(keys[1])

    def _blue(self):
        self.__color["Blue"] = 100500


svetofor = TrafficLight()
TrafficLight.running(svetofor, 1)

svetofor5 = TrafficLight(5)
svetofor5.running(True)
svetofor6 = TrafficLight(6)
svetofor6._blue()
svetofor6.running()
