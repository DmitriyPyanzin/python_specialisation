from lesson10.hw.task4.Animal import Animal


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return 'Meow!'

    def __str__(self):
        return f'{super().__str__()} of breed {self.breed}'
