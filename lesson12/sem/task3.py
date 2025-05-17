# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

from math import factorial as fact


class Generator:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 1, start
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step <= 0:
            raise ValueError('Шаг должен быть положительным')
        if self.current > self.stop:
            raise StopIteration
        res = fact(self.current)
        self.current += self.step
        return res

    def __str__(self):
        return f'Factorial(start={self.start}, stop={self.stop}, step={self.stop})'

f = Generator(5, 10, 2)
for item in f:
    print(item)
print(f)
