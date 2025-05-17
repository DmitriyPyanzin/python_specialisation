# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

from math import factorial as fact
from json import dump


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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('task2.json', 'a', encoding='utf-8') as file:
            dump(self.history, file)


f = Factorial(3)
with f as js:
    for i in range(1, 11):
        print(f'{i}! = {f(i)}')
print(f.get_history)
