# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
from time import time


class MyString(str):
    """Класс Моя строка"""

    def __new__(cls, value, name, time_):
        """Конструктор класса"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time_ = time()
        return instance


s = MyString('word', 'Dimok', time())

print(f'{s = }\t{s.name = }\t{s.time_ = }\t{type(s) = }')
print(s.__doc__)
print(help(s))
