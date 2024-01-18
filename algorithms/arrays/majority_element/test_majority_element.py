import unittest

from . import majority_element, majority_element_two


class MajorityElementTestCases(unittest.TestCase):
    def test_one(self):
        """should return 3 from nums=[3,2,3]"""
        nums = [3, 2, 3]
        expected = 3
        actual = majority_element(nums)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return 2 from nums=[2,2,1,1,1,2,2]"""
        nums = [2, 2, 1, 1, 1, 2, 2]
        expected = 2
        actual = majority_element(nums)
        self.assertEqual(expected, actual)


class MajorityElementTwoTestCases(unittest.TestCase):
    def test_one(self):
        """should return 3 from nums=[3,2,3]"""
        nums = [3, 2, 3]
        expected = 3
        actual = majority_element_two(nums)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return 2 from nums=[2,2,1,1,1,2,2]"""
        nums = [2, 2, 1, 1, 1, 2, 2]
        expected = 2
        actual = majority_element_two(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
