import unittest
from . import non_constructible_change


class NonConstructibleChangeTestCase(unittest.TestCase):
    def test_1(self):
        """should return 20 for input of [5, 7, 1, 1, 2, 3, 22]"""
        coins = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_2(self):
        """should return 6 for input of [1, 1, 1, 1, 1]"""
        coins = [1, 1, 1, 1, 1]
        expected = 6
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_3(self):
        """should return 55 for input of [1, 5, 1, 1, 1, 10, 15, 20, 100]"""
        coins = [1, 5, 1, 1, 1, 10, 15, 20, 100]
        expected = 55
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_4(self):
        """should return 3 for input of [6, 4, 5, 1, 1, 8, 9]"""
        coins = [6, 4, 5, 1, 1, 8, 9]
        expected = 3
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_5(self):
        """should return 1 for input of []"""
        coins = []
        expected = 1
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_6(self):
        """should return 1 for input of [87]"""
        coins = [87]
        expected = 1
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_7(self):
        """should return 32 for input of [5, 6, 1, 1, 2, 3, 4, 9]"""
        coins = [5, 6, 1, 1, 2, 3, 4, 9]
        expected = 32
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_8(self):
        """should return 19 for input of [5, 6, 1, 1, 2, 3, 43]"""
        coins = [5, 6, 1, 1, 2, 3, 43]
        expected = 19
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_9(self):
        """should return 3 for input of [1, 1]"""
        coins = [1, 1]
        expected = 3
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_10(self):
        """should return 1 for input of [2]"""
        coins = [2]
        expected = 1
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_11(self):
        """should return 2 for input of [1]"""
        coins = [1]
        expected = 2
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_12(self):
        """should return 87 for input of [109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]"""
        coins = [109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]
        expected = 87
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_13(self):
        """should return 29 for input of [1, 2, 3, 4, 5, 6, 7]"""
        coins = [1, 2, 3, 4, 5, 6, 7]
        expected = 29
        actual = non_constructible_change(coins)
        self.assertEqual(actual, expected)

    def test_input_not_mutated(self):
       """should not mutate the input coins list"""
       coins = [5, 7, 1, 1, 2, 3, 22]
       snapshot = coins[:]
       _ = non_constructible_change(coins)
       self.assertEqual(coins, snapshot)

if __name__ == '__main__':
    unittest.main()
