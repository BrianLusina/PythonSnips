from random import randint


class BattleShip(object):
    def __init__(self, board):
        self.board = board

    def print_board(self):
        for x in range(5):
            self.board.append(["O"] * 5)
        for row in self.board:
            print(" ".join(row))

    def random_row(self):
        return randint(0, len(self.board) - 1)

    def random_col(self):
        return randint(0, len(self.board[0]) - 1)
