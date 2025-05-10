class Parent:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.children = []

    def info(self):
        print(f'Меня зовут {self._name}, мне {self._age} лет.')

    def add_children(self, child):
        if self._age - child.age >= 16:
            self.children.append(child)
            print(f'Ребенок {child.name} добавлен к {self._name}.')
        else:
            print(f'Ребёнок {child.name} не добавлен к {self._name}, т.к. разница в возрасте слишком мала.')

    def feed(self, child):
        if child in self.children:
            child.hungry = False
            print(f'{self._name} покормил(а) {child.name}.')
        else:
            print(f'{child.name} не является ребёнком {self._name}')

    def calm(self, child):
        if child in self.children:
            child.calm = True
            print(f'{self._name} успокоил(а) {child.name}')
        else:
            print(f'{child.name} не является ребёнком {self._name}')

    def list_children(self):
        if self.children:
            print(f'У {self._name} есть следующие дети: ')
            for child in self.children:
                print(f' - {child}')
        else:
            print(f'У {self._name} нет детей.')
