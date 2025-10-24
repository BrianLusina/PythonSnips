import unittest

from pystrings.count_consonants import count_consonants_iterative, count_consonants_recursive


class CountConsonantsTestCases(unittest.TestCase):
    def test_1_iterative(self):
        """should return 9 from Welcome to Educative!"""
        input_str = "Welcome to Educative!"
        expected = 9
        actual = count_consonants_iterative(input_str)
        self.assertEqual(expected, actual)

    def test_1_recursive(self):
        """should return 9 from Welcome to Educative!"""
        input_str = "Welcome to Educative!"
        expected = 9
        actual = count_consonants_recursive(input_str)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
