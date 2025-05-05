from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_name(self):
        pass

    def get_surname(self):
        pass


class Bird(Animal):
    def get_name(self):
        pass


b = Bird()
b.get_name()
b.get_surname()
