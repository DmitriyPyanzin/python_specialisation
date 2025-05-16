# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """Класс архив"""

    def __init__(self, num, word):
        """Конструктор класса"""
        self.lst = [[num, word]]

    def app_lst(self, num, word):
        """Добавление архива"""
        return self.lst.append([num, word])

    @property
    def get_lst(self):
        """Получение архива"""
        return self.lst

    def __str__(self):
        return f'В архиве хранятся {self.lst}'

    def __repr__(self):
        for i, el in enumerate(self.lst, start=1):
            print(f'Элемент {i} - {el}')
        return f'Длина архива {len(self.lst)} элемента'


a = Archive(1, 'a')
a.app_lst(2, 'b')
print(a.get_lst)
print(a.__doc__)
print(help(a))
print(Archive.__dict__)

print(a)
print(repr(a))
