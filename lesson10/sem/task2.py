# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, width, length=None):
        self._width = width
        self._length = width if length is None else length

    def perimeter(self):
        return self._width * self._length

    def area(self):
        return 2 * (self._width + self._length)


rect1 = Rectangle(4, 7)
rect2 = Rectangle(5)
print(rect1.perimeter(), rect1.area())
print(rect2.perimeter(), rect2.area())
print(Rectangle(6).perimeter(), Rectangle(2, 3).area())
