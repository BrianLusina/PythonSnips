import unittest
from random import choice

from puzzles.chess_board_cell_color import chess_board_cell_color


class ChessBoardCellColorTestCase(unittest.TestCase):
    def test_fixed_basic_tests(self):
        tests = [
            # [[cell1, cell2], expected],
            [["A1", "C3"], True],
            [["A1", "H3"], False],
            [["A1", "A2"], False],
        ]

        for inp, exp in tests:
            self.assertEquals(chess_board_cell_color(*inp), exp)

    def test_random(self):
        def get_position(occupied=None):
            columns = "ABCDEFGH"
            rows = "12345678"
            position = "%s%s" % (choice(columns), choice(rows))
            if occupied is None:
                return position

            while position == occupied:
                position = "%s%s" % (choice(columns), choice(rows))

            return position

        def reference(c1, c2):
            c1c, c1r, c2c, c2r = map(ord, c1 + c2)
            return (c1c + c2c) % 2 == (c1r - c2r) % 2

        for _ in range(100):
            bishop = get_position()
            pawn = get_position(bishop)
            self.assertEquals(chess_board_cell_color(bishop, pawn), reference(bishop, pawn))


if __name__ == '__main__':
    unittest.main()
