from lesson10.hw.task4.Animal import Animal


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return 'Woof!'

    def __str__(self):
        return f'{super().__str__()} of breed {self.breed}'
