import unittest
from . import knapsack_01


class MaxDuffleBagValueTestCase(unittest.TestCase):
    def test_1(self):
        """should return 220 for [(10, 60), (20, 100), (30,120)] and capacity of 50"""
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        expected = 220
        actual = knapsack_01(values, weights, capacity)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 220 for [(10, 60), (20, 100), (30,120)] and capacity of 10"""
        values = [10, 20, 30, 40]
        weights = [12, 13, 15, 19]
        capacity = 10
        expected = 0
        actual = knapsack_01(values, weights, capacity)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 220 for [(96, 359), (43, 963), (28, 465), (37, 706), (92, 146), (5, 282), (3, 828), (54, 962), (93, 492)] and capacity of 383"""
        values = [359, 963, 465, 706, 146, 282, 828, 962, 492]
        weights = [96, 43, 28, 37, 92, 5, 3, 54, 93]
        capacity = 383
        expected = 5057
        actual = knapsack_01(values, weights, capacity)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
