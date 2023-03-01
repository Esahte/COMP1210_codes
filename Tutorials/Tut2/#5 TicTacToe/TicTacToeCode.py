class TicTacToe:
    def __init__(self):
        self.__board = [['0-0','0-1','0-2'], ['1-0','1-1','1-2'], ['2-0','2-1','2-2']]

    def __str__(self):
        rows = [' | '.join(self.__board[r]) for r in range(3)]
        return '\n---------------\n'.join(rows)

    def win(self):
        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2] or self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
            return True
        elif self.__board[0][0] == self.__board[1][0] == self.__board[2][0] or self.__board[0][1] == self.__board[1][1] == self.__board[2][1] or self.__board[0][2] == self.__board[1][2] == self.__board[2][2]:
            return True
        elif self.__board[0][0] == self.__board[0][1] == self.__board[0][2] or self.__board[1][0] == self.__board[1][1] == self.__board[1][2] or self.__board[2][0] == self.__board[2][1] == self.__board[2][2]:
            return True

    def play(self, a='', x=0, y=0):
        if self.__board[x][y] == f'{x}-{y}':
            self.__board[x][y] = a.upper()
        else:
            print('Position filed try new position')
        return self



# game = TicTacToe()
# game.play('x', 2, 0)
# game.play('0', 2, 0)
# # game
# print(game)