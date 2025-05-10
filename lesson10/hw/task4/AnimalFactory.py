from lesson10.hw.task4.Cat import Cat
from lesson10.hw.task4.Dog import Dog


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        animal_classes = {
            'Dog': Dog,
            'Cat': Cat
        }

        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            raise ValueError(f'Unknown animal type: {animal_type}')
