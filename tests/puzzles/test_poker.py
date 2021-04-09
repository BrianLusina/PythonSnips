import unittest

from puzzles.poker import poker


class PokerTest(unittest.TestCase):
    def test_one_hand(self):
        hand = '4S 5S 7H 8D JC'.split()
        self.assertEqual([hand], poker([hand]))

    def test_nothing_vs_one_pair(self):
        nothing = '4S 5H 6S 8D JH'.split()
        pair_of4 = '2S 4H 6S 4D JH'.split()
        self.assertEqual([pair_of4], poker([nothing, pair_of4]))

    def test_two_pair(self):
        pair_of2 = '4S 2H 6S 2D JH'.split()
        pair_of4 = '2S 4H 6S 4D JH'.split()
        self.assertEqual([pair_of4], poker([pair_of2, pair_of4]))

    def test_one_pair_vs_double_pair(self):
        pair_of8 = '2S 8H 6S 8D JH'.split()
        double_pair = '4S 5H 4S 8D 5H'.split()
        self.assertEqual([double_pair], poker([pair_of8, double_pair]))

    def test_two_double_pair(self):
        double_pair2and8 = '2S 8H 2S 8D JH'.split()
        double_pair4and5 = '4S 5H 4S 8D 5H'.split()
        self.assertEqual([double_pair2and8],
                         poker([double_pair2and8, double_pair4and5]))

    def test_double_pair_vs_three(self):
        double_pair2and8 = '2S 8H 2S 8D JH'.split()
        three_of4 = '4S 5H 4S 8D 4H'.split()
        self.assertEqual([three_of4], poker([double_pair2and8, three_of4]))

    def test_two_three(self):
        three_of2 = '2S 2H 2S 8D JH'.split()
        three_of1 = '4S AH AS 8D AH'.split()
        self.assertEqual([three_of1], poker([three_of2, three_of1]))

    def test_three_vs_straight(self):
        three_of4 = '4S 5H 4S 8D 4H'.split()
        straight = '3S 4H 2S 6D 5H'.split()
        self.assertEqual([straight], poker([three_of4, straight]))

    def test_two_straights(self):
        straight_to8 = '4S 6H 7S 8D 5H'.split()
        straight_to9 = '5S 7H 8S 9D 6H'.split()
        self.assertEqual([straight_to9], poker([straight_to8, straight_to9]))
        straight_to1 = 'AS QH KS TD JH'.split()
        straight_to5 = '4S AH 3S 2D 5H'.split()
        self.assertEqual([straight_to1], poker([straight_to1, straight_to5]))

    def test_straight_vs_flush(self):
        straight_to8 = '4S 6H 7S 8D 5H'.split()
        flush_to7 = '2S 4S 5S 6S 7S'.split()
        self.assertEqual([flush_to7], poker([straight_to8, flush_to7]))

    def test_two_flushes(self):
        flush_to8 = '3H 6H 7H 8H 5H'.split()
        flush_to7 = '2S 4S 5S 6S 7S'.split()
        self.assertEqual([flush_to8], poker([flush_to8, flush_to7]))

    def test_flush_vs_full(self):
        flush_to8 = '3H 6H 7H 8H 5H'.split()
        full = '4S 5H 4S 5D 4H'.split()
        self.assertEqual([full], poker([full, flush_to8]))

    def test_two_fulls(self):
        full_of4by9 = '4H 4S 4D 9S 9D'.split()
        full_of5by8 = '5H 5S 5D 8S 8D'.split()
        self.assertEqual([full_of5by8], poker([full_of4by9, full_of5by8]))

    def test_full_vs_square(self):
        full = '4S 5H 4S 5D 4H'.split()
        square_of3 = '3S 3H 2S 3D 3H'.split()
        self.assertEqual([square_of3], poker([full, square_of3]))

    def test_two_square(self):
        square_of2 = '2S 2H 2S 8D 2H'.split()
        square_of5 = '4S 5H 5S 5D 5H'.split()
        self.assertEqual([square_of5], poker([square_of2, square_of5]))

    def test_square_vs_straight_flush(self):
        square_of5 = '4S 5H 5S 5D 5H'.split()
        straight_flush_to9 = '5S 7S 8S 9S 6S'.split()
        self.assertEqual([straight_flush_to9],
                         poker([square_of5, straight_flush_to9]))

    def test_two_straight_flushes(self):
        straight_flush_to8 = '4H 6H 7H 8H 5H'.split()
        straight_flush_to9 = '5S 7S 8S 9S 6S'.split()
        self.assertEqual([straight_flush_to9],
                         poker([straight_flush_to8, straight_flush_to9]))

    def test_three_hand_with_tie(self):
        spade_straight_to9 = "9S 8S 7S 6S 5S".split()
        diamond_straight_to9 = "9D 8D 7D 6D 5D".split()
        three_of4 = "4D 4S 4H QS KS".split()
        self.assertEqual([spade_straight_to9, diamond_straight_to9],
                         poker([spade_straight_to9, diamond_straight_to9, three_of4]))


if __name__ == '__main__':
    unittest.main()
