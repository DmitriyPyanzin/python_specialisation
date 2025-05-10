class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = False
        self.hungry = True

    def get_status(self):
        calm_status = 'спокоен' if self.calm else 'не спокоен'
        hungry_status = 'сыт' if not self.hungry else 'голоден'
        print(f'Ребёнок {self.name} {calm_status} и {hungry_status}')

    def __str__(self):
        return f'Ребёнок {self.name}, {self.age} лет'
