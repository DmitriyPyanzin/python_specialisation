# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

from math import factorial as fact


class Factorial:

    def __init__(self, k):
        self.k = k
        self.history = []

    def __call__(self, n):
        self.history.append({n: fact(n)})
        self.history = self.history[-self.k:]
        return fact(n)

    @property
    def get_history(self):
        return self.history


f = Factorial(3)
for i in range(1, 11):
    print(f'{i}! = {f(i)}')
print(f.get_history)
