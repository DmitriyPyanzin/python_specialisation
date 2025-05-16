# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    def __init__(self, width, length=None):
        self._width = width
        self._length = width if length is None else length

    def perimeter(self):
        return self._width * self._length

    def area(self):
        return 2 * (self._width + self._length)

    def __sub__(self, other):
        return self.perimeter() - other.perimeter()

    def __add__(self, other):
        return self.perimeter() + other.perimeter()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() >= other.area()


rect1 = Rectangle(4, 7)
rect2 = Rectangle(5)
print(rect1.perimeter(), rect1.area())
print(rect2.perimeter(), rect2.area())
print(Rectangle(6).perimeter(), Rectangle(2, 3).area())
print(rect1 - rect2)
print(rect1 + rect2)

print(rect1 == rect2)
print(rect1 != rect2)
print(rect1 > rect2)
print(rect1 <= rect2)
print(rect1 < rect2)
print(rect1 >= rect2)
