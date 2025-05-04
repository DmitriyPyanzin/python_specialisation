# Создайте три (или более) отдельных классов животных.
# Например, рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animal:
    def __init__(self, view, name, age, colour):
        self._view = view
        self._name = name
        self._age = age
        self._colour = colour

    @property
    def get_animal(self):
        return f'{self._view}, {self._name}, {self._age}, {self._colour}'


class Cat(Animal):
    def __init__(self, view, name, age, colour, ability):
        super().__init__(view, name, age, colour)
        self._ability = ability

    @property
    def get_ability(self):
        return self._ability


class Dog(Animal):
    def __init__(self, view, name, age, colour, ability):
        super().__init__(view, name, age, colour)
        self._ability = ability

    @property
    def get_ability(self):
        return self._ability


class Perrot(Animal):
    def __init__(self, view, name, age, colour, ability):
        super().__init__(view, name, age, colour)
        self._ability = ability

    @property
    def get_ability(self):
        return self._ability


if __name__ == '__main__':
    cat = Cat('Кот', 'Пушок', '5', 'Полосатый', 'Мяу')
    dog = Dog('Пёс', 'Граф', '3', 'Коричневый', 'Гав')
    perrot = Perrot('Попугай', 'Кеша', '1', 'Лютинос', 'Чирик')

    print(cat.get_animal)
    print(cat.get_ability)

    print(dog.get_animal)
    print(dog.get_ability)

    print(perrot.get_animal)
    print(perrot.get_ability)