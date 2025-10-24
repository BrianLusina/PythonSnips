import unittest
from . import is_valid_subsequence, is_valid_subsequence_v2


class IsValidSubsequenceTestCase(unittest.TestCase):
    def test_1(self):
        """array = [5, 1, 22, 25, 6, -1, 8, 10], sequence = [1, 6, -1, 10]"""
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        actual = is_valid_subsequence(array, sequence)
        self.assertTrue(actual)

    def test_2(self):
        """should return True for array = [5, 1, 22, 25, 6, -1, 8, 10], sequence = [5, 1, 22, 6, -1, 8, 10]"""
        array =  [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 6, -1, 8, 10]
        actual = is_valid_subsequence(array, sequence)
        self.assertTrue(actual)

    def test_3(self):
        """should return False for array = [5, 1, 22, 25, 6, -1, 8, 10], sequence = [5, 6, 1, 10, 22, 8, -1, 25]"""
        array =  [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 6, 1, 10, 22, 8, -1, 25]
        actual = is_valid_subsequence(array, sequence)
        self.assertFalse(actual)

    def test_4(self):
        """should return True for array = [1,2,3,4], sequence = [1,3,4]"""
        array =  [1,2,3,4]
        sequence = [1,3,4]
        actual = is_valid_subsequence(array, sequence)
        self.assertTrue(actual)

    def test_5(self):
        """should return True for array = [1,2,3,4], sequence = [2,4]"""
        array =  [1,2,3,4]
        sequence = [2,4]
        actual = is_valid_subsequence(array, sequence)
        self.assertTrue(actual)

class IsValidSubsequenceV2TestCase(unittest.TestCase):
    def test_1(self):
        """array = [5, 1, 22, 25, 6, -1, 8, 10], sequence = [1, 6, -1, 10]"""
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        actual = is_valid_subsequence_v2(array, sequence)
        self.assertTrue(actual)

    def test_2(self):
        """should return True for array = [5, 1, 22, 25, 6, -1, 8, 10], sequence = [5, 1, 22, 6, -1, 8, 10]"""
        array =  [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 6, -1, 8, 10]
        actual = is_valid_subsequence_v2(array, sequence)
        self.assertTrue(actual)

    def test_3(self):
        """should return False for array = [5, 1, 22, 25, 6, -1, 8, 10], sequence = [5, 6, 1, 10, 22, 8, -1, 25]"""
        array =  [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 6, 1, 10, 22, 8, -1, 25]
        actual = is_valid_subsequence_v2(array, sequence)
        self.assertFalse(actual)

    def test_4(self):
        """should return True for array = [1,2,3,4], sequence = [1,3,4]"""
        array =  [1,2,3,4]
        sequence = [1,3,4]
        actual = is_valid_subsequence_v2(array, sequence)
        self.assertTrue(actual)

    def test_5(self):
        """should return True for array = [1,2,3,4], sequence = [2,4]"""
        array =  [1,2,3,4]
        sequence = [2,4]
        actual = is_valid_subsequence_v2(array, sequence)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
