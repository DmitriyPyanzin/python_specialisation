# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.

class ValidDescriptor:
    def __set_name__(self, own, name):
        self.param_name = name

    @staticmethod
    def validate(val):
        if val <= 0:
            raise ValueError('Некорректное значение')

    def __set__(self, inst, val):
        self.validate(val)
        setattr(inst, self.param_name, val)


class Rectangle:
    length = ValidDescriptor()
    width = ValidDescriptor()

    def __init__(self, length, width):
        self.length = length
        self.width = width
        if width == 0:
            self.width = length

    def get_perimetr(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width
