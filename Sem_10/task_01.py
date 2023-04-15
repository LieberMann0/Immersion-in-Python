# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь

from math import pi


class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        self.__long = pi * self.radius * 2
        self.__area = pi * self.radius ** 2


    def circ_len(self) -> float:
        return self.__long


    def circ_area(self) -> float:
        return self.__area


if __name__ == '__main__':
    my_circ = Circle(5)
    print(my_circ.circ_len(), my_circ.circ_area())
