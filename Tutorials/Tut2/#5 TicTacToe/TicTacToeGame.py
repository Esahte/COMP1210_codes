from TicTacToeCode import TicTacToe
from random import *

game = TicTacToe()
playerOne, playerTwo = input('Enter your name: ').split(',')

def player():
    if (playing := choice((playerOne, playerTwo))) == playerOne:
        stand_by = playerTwo
    else:
        stand_by = playerOne
    print(f'The first player is {playing} and the second player is {stand_by}')
    return [playing, stand_by]

players = player()
while not game.win() and (play := input(f'{players[0]} Enter "S" to start and "Q" to quit: ').upper()) != 'Q' and (aQuitter := True):
    print(game)
    coordinate1, x, y = input(f'Enter "x" or "o" to play your coordinates (x, y) on the board '
                                        f'and "p" to play each seperated by a comma e.g. X, 0, 1: ').split(',')

    game.play(coordinate1, int(x), int(y))
    if game.win():
        print(f'{players[0]} has won')

    if players[0] == playerOne:
        players[0], players[1] = playerTwo, playerOne
    else:
        players[0], players[1] = playerOne, playerTwo

print(game)
