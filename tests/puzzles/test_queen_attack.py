import unittest

from puzzles.queen_attack import QueenAttack


class QueenAttackTest(unittest.TestCase):
    def test_board1(self):
        queen_attack = QueenAttack((2, 3), (5, 6))
        ans = ['________',
               '________',
               '___W____',
               '________',
               '________',
               '______B_',
               '________',
               '________']
        self.assertEqual(ans, queen_attack.board())

    def test_board2(self):
        queen_attack = QueenAttack((0, 6), (1, 7))

        ans = ['______W_',
               '_______B',
               '________',
               '________',
               '________',
               '________',
               '________',
               '________']
        self.assertEqual(ans, queen_attack.board())

    def test_attack_true1(self):
        queen_attack = QueenAttack((2, 3), (5, 6))
        self.assertEqual(True, queen_attack.can_attack())

    def test_attack_true2(self):
        queen_attack = QueenAttack((2, 6), (5, 3))
        self.assertEqual(True, queen_attack.can_attack())

    def test_attack_true3(self):
        queen_attack = QueenAttack((2, 4), (2, 7))
        self.assertEqual(True, queen_attack.can_attack())

    def test_attack_true4(self):
        queen_attack = QueenAttack((5, 4), (2, 4))
        self.assertEqual(True, queen_attack.can_attack())

    def test_attack_true5(self):
        queen_attack = QueenAttack((1, 1), (6, 6))
        self.assertEqual(True, queen_attack.can_attack())

    def test_attack_true6(self):
        queen_attack = QueenAttack((0, 6), (1, 7))
        self.assertEqual(True, queen_attack.can_attack())

    def test_attack_false1(self):
        queen_attack = QueenAttack((4, 2), (0, 5))
        self.assertEqual(False, queen_attack.can_attack())

    def test_attack_false2(self):
        queen_attack = QueenAttack((2, 3), (4, 7))
        self.assertEqual(False, queen_attack.can_attack())

    # If either queen_attack.board or queen_attack.can_attack are called with an invalid queen_attack.board position
    # they should raise a ValueError with a meaningful error message.
    def test_invalid_position_board(self):
        queen_attack = QueenAttack((0, 0), (7, 8))
        with self.assertRaises(ValueError):
            queen_attack.board()

    def test_invalid_position_can_attack(self):
        queen_attack = QueenAttack((0, 0), (7, 8))
        with self.assertRaises(ValueError):
            queen_attack.can_attack()

    def test_queens_same_position_board(self):
        queen_attack = QueenAttack((2, 2), (2, 2))
        with self.assertRaises(ValueError):
            queen_attack.board()

    def test_queens_same_position_can_attack(self):
        queen_attack = QueenAttack((2, 2), (2, 2))
        with self.assertRaises(ValueError):
            queen_attack.can_attack()


if __name__ == '__main__':
    unittest.main()
