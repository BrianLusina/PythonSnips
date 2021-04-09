import unittest

from puzzles.yacht import score, BIG_STRAIGHT, YACHT, ONES, THREES, TWOS, LITTLE_STRAIGHT, CHOICE, FULL_HOUSE, \
    SIXES, FOUR_OF_A_KIND, FIVES, FOURS


class YachtTests(unittest.TestCase):
    def test_yacht(self):
        self.assertEqual(score([5, 5, 5, 5, 5], YACHT), 50)

    def test_not_yacht(self):
        self.assertEqual(score([1, 3, 3, 2, 5], YACHT), 0)

    def test_ones(self):
        self.assertEqual(score([1, 1, 1, 3, 5], ONES), 3)

    def test_ones_out_of_order(self):
        self.assertEqual(score([3, 1, 1, 5, 1], ONES), 3)

    def test_no_ones(self):
        self.assertEqual(score([4, 3, 6, 5, 5], ONES), 0)

    def test_twos(self):
        self.assertEqual(score([2, 3, 4, 5, 6], TWOS), 2)

    def test_fours(self):
        self.assertEqual(score([1, 4, 1, 4, 1], FOURS), 8)

    def test_yacht_counted_as_threes(self):
        self.assertEqual(score([3, 3, 3, 3, 3], THREES), 15)

    def test_yacht_of_threes_counted_as_fives(self):
        self.assertEqual(score([3, 3, 3, 3, 3], FIVES), 0)

    def test_sixes(self):
        self.assertEqual(score([2, 3, 4, 5, 6], SIXES), 6)

    def test_full_house_two_small_three_big(self):
        self.assertEqual(score([2, 2, 4, 4, 4], FULL_HOUSE), 16)

    def test_full_house_three_small_two_big(self):
        self.assertEqual(score([5, 3, 3, 5, 3], FULL_HOUSE), 19)

    def test_two_pair_is_not_a_full_house(self):
        self.assertEqual(score([2, 2, 4, 4, 5], FULL_HOUSE), 0)

    def test_yacht_is_not_a_full_house(self):
        self.assertEqual(score([2, 2, 2, 2, 2], FULL_HOUSE), 0)

    def test_four_of_a_kind(self):
        self.assertEqual(score([6, 6, 4, 6, 6], FOUR_OF_A_KIND), 24)

    def test_yacht_can_be_scored_as_four_of_a_kind(self):
        self.assertEqual(score([3, 3, 3, 3, 3], FOUR_OF_A_KIND), 12)

    def test_full_house_is_not_four_of_a_kind(self):
        self.assertEqual(score([3, 5, 4, 1, 2], FOUR_OF_A_KIND), 0)

    def test_little_straight(self):
        self.assertEqual(score([3, 5, 4, 1, 2], LITTLE_STRAIGHT), 30)

    def test_little_straight_as_big_straight(self):
        self.assertEqual(score([1, 2, 3, 4, 5], BIG_STRAIGHT), 0)

    def test_four_in_order_but_not_a_little_straight(self):
        self.assertEqual(score([1, 1, 2, 3, 4], LITTLE_STRAIGHT), 0)

    def test_no_pairs_but_not_a_little_straight(self):
        self.assertEqual(score([1, 2, 3, 4, 6], LITTLE_STRAIGHT), 0)

    def test_min_1_max_5_but_not_a_little_straight(self):
        self.assertEqual(score([1, 1, 3, 4, 5], LITTLE_STRAIGHT), 0)

    def test_big_straight(self):
        self.assertEqual(score([4, 6, 2, 5, 3], BIG_STRAIGHT), 30)

    def test_big_straight_as_little_straight(self):
        self.assertEqual(score([6, 5, 4, 3, 2], LITTLE_STRAIGHT), 0)

    def test_choice(self):
        self.assertEqual(score([3, 3, 5, 6, 6], CHOICE), 23)

    def test_yacht_as_choice(self):
        self.assertEqual(score([2, 2, 2, 2, 2], CHOICE), 10)


if __name__ == '__main__':
    unittest.main()
