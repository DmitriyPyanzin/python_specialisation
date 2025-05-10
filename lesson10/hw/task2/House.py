class House:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money

    def buy_food(self, quantity, price):
        if self.money >= price:
            self.food += quantity
            self.money -= price
            print(f'Купили {quantity} единиц еды за {price} денег.')
        else:
            print('Недостаточно денег для покупки еды!')

    def earn_money(self, salary):
        self.money += salary
        print(f'Заработали {salary} денег.')
