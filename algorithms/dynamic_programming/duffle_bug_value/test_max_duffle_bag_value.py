import unittest
from . import max_duffel_bag_value


class MaxDuffleBagValueTestCase(unittest.TestCase):
    def test_1(self):
        """should return 220 for [(10, 60), (20, 100), (30,120)] and capacity of 50"""
        cake_tuples = [(10, 60), (20, 100), (30, 120)]
        capacity = 50
        expected = 220
        actual = max_duffel_bag_value(cake_tuples, capacity)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 220 for [(10, 60), (20, 100), (30,120)] and capacity of 10"""
        cake_tuples = [(12, 10), (13, 20), (15, 30), (19, 40)]
        capacity = 10
        expected = 0
        actual = max_duffel_bag_value(cake_tuples, capacity)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 5057 for [(96, 359), (43, 963), (28, 465), (37, 706), (92, 146), (5, 282), (3, 828), (54, 962), (93, 492)] and capacity of 383"""
        cake_tuples = [
            (96, 359),
            (43, 963),
            (28, 465),
            (37, 706),
            (92, 146),
            (5, 282),
            (3, 828),
            (54, 962),
            (93, 492),
        ]
        capacity = 383
        expected = 5057
        actual = max_duffel_bag_value(cake_tuples, capacity)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
