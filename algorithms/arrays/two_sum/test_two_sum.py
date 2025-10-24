import unittest
from . import two_sum, two_sum_with_pointers


class TwoSumTestCase(unittest.TestCase):
    def test_1(self):
        """numbers = [2,7,11,15], target = 9"""
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]
        actual = two_sum(numbers, target)
        self.assertEqual(expected, actual)

    def test_2(self):
        """numbers = [2,3,4], target = 6"""
        numbers = [2, 3, 4]
        target = 6
        expected = [1, 3]
        actual = two_sum(numbers, target)
        self.assertEqual(expected, actual)

    def test_3(self):
        """numbers = [-1,0], target = -1"""
        numbers = [-1, 0]
        target = -1
        expected = [1, 2]
        actual = two_sum(numbers, target)
        self.assertEqual(expected, actual)


class TwoSumWithPointersTestCase(unittest.TestCase):
    def test_1(self):
        """numbers = [2,7,11,15], target = 9"""
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        actual = two_sum_with_pointers(numbers, target)
        self.assertEqual(expected, actual)

    def test_2(self):
        """numbers = [2,3,4], target = 6"""
        numbers = [2, 3, 4]
        target = 6
        expected = [0, 2]
        actual = two_sum_with_pointers(numbers, target)
        self.assertEqual(expected, actual)

    def test_3(self):
        """numbers = [-1,0], target = -1"""
        numbers = [-1, 0]
        target = -1
        expected = [0, 1]
        actual = two_sum_with_pointers(numbers, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
