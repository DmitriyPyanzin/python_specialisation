class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def make_move(self):
        while True:
            try:
                move = int(input(f'{self.name}, введите номер клетки для вашего хода (1-9): '))
                if not 0 < move < 10:
                    raise ValueError
                return move
            except ValueError:
                print('Неправильный ввод. Пожалуйста, введите число от 1 до 9.')
