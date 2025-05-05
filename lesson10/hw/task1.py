# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
# ● имя,
# ● возраст,
# ● список детей.
# И он может:
# ● сообщить информацию о себе,
# ● успокоить ребёнка,
# ● покормить ребёнка.
# У ребёнка есть:
# ● имя,
# ● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# ● состояние спокойствия,
# ● состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
# и словарь состояний, и что-то поинтереснее.

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, kid):
        self.children.append(kid)

    @property
    def get_children(self):
        return self.children

    def feed(self):
        pass

    def __str__(self):
        return f'Имя {self.name}, {self.age} лет, ' + (f'дети {self.children}' if len(self.children) != 0
                                                       else 'детей нет')


class Child:
    def __init__(self, name, age, calmness, hungry):
        self._name = name
        self._age = age
        self.calmness = calmness
        self.hungry = hungry

    def __str__(self):
        return f'Имя {self._name}, {self._age} лет'

    def __repr__(self):
        return f'{self._name}, {self._age}, {self.calmness}, {self.hungry}'


if __name__ == '__main__':
    parent = Parent('Маша', 38)
    print(parent)
    child1 = Child('Миша', 10, False, False)
    print(child1)
    print(repr(child1))
    parent.add_child(child1)
    print(parent)
