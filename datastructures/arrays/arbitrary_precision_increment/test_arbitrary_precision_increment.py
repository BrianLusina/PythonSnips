import unittest
from utils.benchmark import func_timer
from . import arbitrary_precision_increment, arbitrary_precision_increment_two


class ArbitraryPrecisionIncrementTestCase(unittest.TestCase):
    def test_1_1(self):
        """should return [1,5,0] for [1,4,9], when adding 1"""
        a = [1, 4, 9]
        expected = [1, 5, 0]

        actual = func_timer(arbitrary_precision_increment)(a)
        self.assertEqual(expected, actual)

    def test_1_2(self):
        """should return [1,0, 0, 0] for [9,9,9], when adding 1"""
        a = [9, 9, 9]
        expected = [1, 0, 0, 0]

        actual = arbitrary_precision_increment(a)
        self.assertEqual(expected, actual)

    def test_2_1(self):
        """should return [1,5,0] for [1,4,9], when adding 1"""
        a = [1, 4, 9]
        expected = [1, 5, 0]

        actual = arbitrary_precision_increment_two(a)
        self.assertEqual(expected, actual)

    def test_2_2(self):
        """should return [1,0, 0, 0] for [9,9,9], when adding 1"""
        a = [9, 9, 9]
        expected = [1, 0, 0, 0]

        actual = arbitrary_precision_increment_two(a)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
