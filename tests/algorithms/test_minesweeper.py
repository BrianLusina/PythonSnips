import unittest

from algorithms.minesweeper import Minesweeper


class MinesweeperTest(unittest.TestCase):

    def shortDescription(self):
        return "Tests for Minesweeper"

    def setUp(self):
        self.minesweeper = Minesweeper()

    def tearDown(self):
        self.minesweeper = None

    def test_board1(self):
        inp = ["+------+",
               "| *  * |",
               "|  *   |",
               "|    * |",
               "|   * *|",
               "| *  * |",
               "|      |",
               "+------+"]
        out = ["+------+",
               "|1*22*1|",
               "|12*322|",
               "| 123*2|",
               "|112*4*|",
               "|1*22*2|",
               "|111111|",
               "+------+"]
        self.assertEqual(out, self.minesweeper.board(inp))

    def test_board2(self):
        inp = ["+-----+",
               "| * * |",
               "|     |",
               "|   * |",
               "|  * *|",
               "| * * |",
               "+-----+"]
        out = ["+-----+",
               "|1*2*1|",
               "|11322|",
               "| 12*2|",
               "|12*4*|",
               "|1*3*2|",
               "+-----+"]
        self.assertEqual(out, self.minesweeper.board(inp))

    def test_board3(self):
        inp = ["+-----+",
               "| * * |",
               "+-----+"]
        out = ["+-----+",
               "|1*2*1|",
               "+-----+"]
        self.assertEqual(out, self.minesweeper.board(inp))

    def test_board4(self):
        inp = ["+-+",
               "|*|",
               "| |",
               "|*|",
               "| |",
               "| |",
               "+-+"]
        out = ["+-+",
               "|*|",
               "|2|",
               "|*|",
               "|1|",
               "| |",
               "+-+"]
        self.assertEqual(out, self.minesweeper.board(inp))

    def test_board5(self):
        inp = ["+-+",
               "|*|",
               "+-+"]
        out = ["+-+",
               "|*|",
               "+-+"]
        self.assertEqual(out, self.minesweeper.board(inp))

    def test_board6(self):
        inp = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        out = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        self.assertEqual(out, self.minesweeper.board(inp))

    def test_board7(self):
        inp = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        out = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        self.assertEqual(out, self.minesweeper.board(inp))

    def test_board8(self):
        inp = ["+---+",
               "|***|",
               "|* *|",
               "|***|",
               "+---+"]
        out = ["+---+",
               "|***|",
               "|*8*|",
               "|***|",
               "+---+"]
        self.assertEqual(out, self.minesweeper.board(inp))

    def test_board9(self):
        inp = ["+-----+",
               "|     |",
               "|   * |",
               "|     |",
               "|     |",
               "| *   |",
               "+-----+"]
        out = ["+-----+",
               "|  111|",
               "|  1*1|",
               "|  111|",
               "|111  |",
               "|1*1  |",
               "+-----+"]
        self.assertEqual(out, self.minesweeper.board(inp))

    def test_different_len(self):
        inp = ["+-+",
               "| |",
               "|*  |",
               "|  |",
               "+-+"]
        self.assertRaises(ValueError, self.minesweeper.board, inp)

    def test_faulty_border(self):
        inp = ["+-----+",
               "*   * |",
               "+-- --+"]
        self.assertRaises(ValueError, self.minesweeper.board, inp)

    def test_invalid_char(self):
        inp = ["+-----+",
               "|X  * |",
               "+-----+"]
        self.assertRaises(ValueError, self.minesweeper.board, inp)


if __name__ == '__main__':
    unittest.main()
