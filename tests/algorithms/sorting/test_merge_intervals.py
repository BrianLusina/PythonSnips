import unittest

from algorithms.sorting.merge_intervals import merge


class MergeIntervalsTestCase(unittest.TestCase):
    def test_1_3_2_6_8_10_15_18(self):
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(expected, merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

    def test_1_4_4_5(self):
        expected = [[1, 5]]
        self.assertEqual(expected, merge([[1, 4], [4, 5]]))


if __name__ == '__main__':
    unittest.main()
