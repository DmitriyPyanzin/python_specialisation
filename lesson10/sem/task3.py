# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

from time import time


class Person:
    def __init__(self, name, patronymic, lastname, day_to_born):
        self.name = name
        self.lastname = lastname
        self.patronymic = patronymic
        self.day_to_born = day_to_born
        lst = [int(el) for el in self.day_to_born.split('.')]
        self.__year = self.year = round(time()) // 31536000 + 1970 - lst[2]

    def get_name(self):
        return f'Фамилия {self.lastname}\nИмя {self.name}\nОтчество {self.patronymic}\n'

    def get_birthday(self):
        return self.day_to_born

    @property
    def age(self):
        return self.__year

    @age.setter
    def age(self, value):
        if value > 80:
            raise ValueError('Пожилой')
        else:
            self.__year = value

    def birthday(self):
        self.year += 1


if __name__ == '__main__':
    p1 = Person('Дмитрий', 'Викторович', 'Пьянзин', '03.12.1900')
    print(p1.get_name())
    print(p1.get_birthday())
    print(p1.age)
    p1.birthday()
    print(p1.age)
