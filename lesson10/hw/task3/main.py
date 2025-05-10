from lesson10.hw.task3.Game import Game
from lesson10.hw.task3.Player import Player

player1 = Player('Димок', 'Х')
player2 = Player('Евгений', 'O')

game = Game(player1, player2)
game.start_games()
