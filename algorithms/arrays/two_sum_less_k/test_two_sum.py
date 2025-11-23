import unittest
from . import two_sum_less_than_k


class TwoSumLessKTestCase(unittest.TestCase):
    def test_1(self):
        """numbers = [4,2,11,2,5,3,5,8], target = 7"""
        numbers = [4,2,11,2,5,3,5,8]
        target = 7
        expected = 6
        actual = two_sum_less_than_k(numbers, target)
        self.assertEqual(expected, actual)

    def test_2(self):
        """numbers = [10,20,30], target = 15"""
        numbers = [10, 20, 30]
        target = 15
        expected = -1
        actual = two_sum_less_than_k(numbers, target)
        self.assertEqual(expected, actual)

    def test_3(self):
        """numbers = [34,23,1,24,75,33,54,8], k = 60"""
        numbers = [34,23,1,24,75,33,54,8]
        k = 60
        expected = 58
        actual = two_sum_less_than_k(numbers, k)
        self.assertEqual(expected, actual)

    def test_4(self):
        """numbers = [5,5,5,5,5,5], k = 15"""
        numbers = [5,5,5,5,5,5]
        k = 15
        expected = 10
        actual = two_sum_less_than_k(numbers, k)
        self.assertEqual(expected, actual)

    def test_5(self):
        """numbers = [1,2,3,4,5], k = 3"""
        numbers = [1,2,3,4,5]
        k = 3
        expected = -1
        actual = two_sum_less_than_k(numbers, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
