# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    def __init__(self, width, length=None):
        self._width = width
        self._length = width if length is None else length

    def perimeter(self):
        return 2 * (self._width + self._length)

    def area(self):
        return self._width * self._length

    def __sub__(self, other):
        return Rectangle(int(self.perimeter()) - int(other.perimeter()))

    def __add__(self, other):
        return Rectangle(self.perimeter() + other.perimeter())

    @property
    def get_perimeter(self):
        return f'{self.perimeter()}'


rect1 = Rectangle(4, 7)
rect2 = Rectangle(5)
print(rect1.get_perimeter)
print(rect2.get_perimeter)
print(Rectangle(6).perimeter(), Rectangle(2, 3).area())

print((rect1 - rect2).get_perimeter)
print((rect1 + rect2).get_perimeter)
