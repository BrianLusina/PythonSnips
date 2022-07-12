import unittest

from datastructures.arrays.find_unique import find_uniq


class FindUniqueTestCases(unittest.TestCase):
    def test_one(self):
        """Returns 2 for input of [1, 1, 1, 2, 1, 1]"""
        arr = [1, 1, 1, 2, 1, 1]
        actual = find_uniq(arr)
        expected = 2
        self.assertEqual(expected, actual)

    def test_two(self):
        """Returns 0.55 for input of [0, 0, 0.55, 0, 0]"""
        arr = [0, 0, 0.55, 0, 0]
        actual = find_uniq(arr)
        expected = 0.55
        self.assertEqual(expected, actual)

    def test_third(self):
        """Returns 0.55 for input of [3, 10, 3, 3, 3]"""
        arr = [3, 10, 3, 3, 3]
        actual = find_uniq(arr)
        expected = 10
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
