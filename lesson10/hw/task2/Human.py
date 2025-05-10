import random


class Human:
    def __init__(self, name, house):
        self.name = name
        self.hunger = 50
        self.house = house

    def eat(self):
        if self.house.food >= 10:
            self.hunger += 10
            self.house.food -= 10
            print(f'{self.name} поел. Сытость увеличилась до {self.hunger}, еда уменьшилась до {self.house.food}.')

    def work(self):
        self.hunger -= 10
        self.house.earn_money(50)
        print(f'{self.name} поработал. Сытость уменьшилась до {self.hunger}.')

    def play(self):
        self.hunger -= 5
        print(f'{self.name} поиграл. Сытость уменьшилась до {self.hunger}.')

    def shop_for_food(self):
        self.house.buy_food(15, 50)

    def live_day(self):
        cube = random.randint(1, 6)
        print(f'\nСегодняшний кубик: {cube}')

        if self.hunger < 20:
            self.eat()
        elif self.house.food < 10:
            self.shop_for_food()
        elif self.house.money < 50:
            self.work()
        elif cube == 1:
            self.work()
        elif cube == 2:
            self.eat()
        else:
            self.play()

        if self.hunger <= 0:
            print(f'{self.name} умер от голода.')
            return False
        return True
