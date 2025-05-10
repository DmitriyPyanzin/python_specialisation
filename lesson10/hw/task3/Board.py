from lesson10.hw.task3.Cell import Cell


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display_board(self):
        print('-------------')
        for i in range(0, 9, 3):
            print(f'| {self.cells[i].symbol} | {self.cells[i + 1].symbol} | {self.cells[i + 2].symbol} |')
            print('-------------')

    def change_cell(self, cell_number, symbol):
        cell = self.cells[cell_number - 1]
        if cell.occupied:
            return False
        cell.symbol = symbol
        cell.occupied = True
        return True

    def check_game_over(self):
        win_position = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for pos in win_position:
            if self.cells[pos[0]].symbol != ' ' and self.cells[pos[0]].symbol == self.cells[pos[1]].symbol == \
                    self.cells[pos[2]].symbol:
                return True
            return False
        return None

    def reset_board(self):
        for cell in self.cells:
            cell.symbol = ' '
            cell.occupied = False
