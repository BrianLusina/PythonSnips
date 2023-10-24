import unittest

from . import letter_combination


class LetterCombinationTestCases(unittest.TestCase):
    def test_1(self):
        """should return ['a', 'b'] for n=1"""
        n = 1
        expected = ['a', 'b']
        actual = letter_combination(n)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return ['aa', 'ab', 'ba', 'bb'] for n=2"""
        n = 2
        expected = ['aa', 'ab', 'ba', 'bb']
        actual = letter_combination(n)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return ['aaa','aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'] for n=3"""
        n = 3
        expected = ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
        actual = letter_combination(n)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return [] for n=0"""
        n = 0
        expected = []
        actual = letter_combination(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
