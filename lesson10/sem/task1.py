# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

import math
from random import randint as ra


class Circle:
    PI = math.pi

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return round(self.__radius ** 2 * self.PI, 4)

    def circumference_length(self):
        return round(2 * self.__radius * self.PI, 4)

num = ra(1, 20)
circle = Circle(num)
print(Circle)
print(circle)
print(circle.area())
print(circle.circumference_length())

print(Circle(5).circumference_length())
