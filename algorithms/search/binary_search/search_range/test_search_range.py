import unittest

from . import search_range, search_range_v3, search_range_v2


class SearchRangeTestCases(unittest.TestCase):
    def test_1(self):
        """should return [3, 4] for nums=[5, 7, 7, 8, 8, 10] and target 8"""
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected = [3, 4]
        actual = search_range(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return [-1, -1] for nums=[5, 7, 7, 8, 8, 10] and target 6"""
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected = [-1, -1]
        actual = search_range(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return [-1, -1] for nums=[] and target 0"""
        nums = []
        target = 0
        expected = [-1, -1]
        actual = search_range(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return [0, 0] for nums=[1] and target 1"""
        nums = [1]
        target = 1
        expected = [0, 0]
        actual = search_range(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should return [0, 1] for nums=[2, 2] and target 2"""
        nums = [2, 2]
        target = 2
        expected = [0, 1]
        actual = search_range(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should return [0, 0] for nums=[1, 3] and target 1"""
        nums = [1, 3]
        target = 1
        expected = [0, 0]
        actual = search_range(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_7(self):
        """should return [1, 1] for nums=[1, 4] and target 4"""
        nums = [1, 4]
        target = 4
        expected = [1, 1]
        actual = search_range(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_8(self):
        """should return [1, 1] for nums=[1, 2, 3] and target 2"""
        nums = [1, 2, 3]
        target = 2
        expected = [1, 1]
        actual = search_range(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_9(self):
        """should return [0, 2] for nums=[3, 3, 3] and target 3"""
        nums = [3, 3, 3]
        target = 3
        expected = [0, 2]
        actual = search_range(nums=nums, target=target)
        self.assertEqual(expected, actual)


class SearchRangeV2TestCases(unittest.TestCase):
    def test_1(self):
        """should return [3, 4] for nums=[5, 7, 7, 8, 8, 10] and target 8"""
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected = [3, 4]
        actual = search_range_v2(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return [-1, -1] for nums=[5, 7, 7, 8, 8, 10] and target 6"""
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected = [-1, -1]
        actual = search_range_v2(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return [-1, -1] for nums=[] and target 0"""
        nums = []
        target = 0
        expected = [-1, -1]
        actual = search_range_v2(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return [0, 0] for nums=[1] and target 1"""
        nums = [1]
        target = 1
        expected = [0, 0]
        actual = search_range_v2(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should return [0, 1] for nums=[2, 2] and target 2"""
        nums = [2, 2]
        target = 2
        expected = [0, 1]
        actual = search_range_v2(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should return [0, 0] for nums=[1, 3] and target 1"""
        nums = [1, 3]
        target = 1
        expected = [0, 0]
        actual = search_range_v2(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_7(self):
        """should return [1, 1] for nums=[1, 4] and target 4"""
        nums = [1, 4]
        target = 4
        expected = [1, 1]
        actual = search_range_v3(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_8(self):
        """should return [1, 1] for nums=[1, 2, 3] and target 2"""
        nums = [1, 2, 3]
        target = 2
        expected = [1, 1]
        actual = search_range_v2(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_9(self):
        """should return [0, 2] for nums=[3, 3, 3] and target 3"""
        nums = [3, 3, 3]
        target = 3
        expected = [0, 2]
        actual = search_range_v2(nums=nums, target=target)
        self.assertEqual(expected, actual)


class SearchRangeV3TestCases(unittest.TestCase):
    def test_1(self):
        """should return [3, 4] for nums=[5, 7, 7, 8, 8, 10] and target 8"""
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected = [3, 4]
        actual = search_range_v3(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return [-1, -1] for nums=[5, 7, 7, 8, 8, 10] and target 6"""
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected = [-1, -1]
        actual = search_range_v3(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return [-1, -1] for nums=[] and target 0"""
        nums = []
        target = 0
        expected = [-1, -1]
        actual = search_range_v3(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return [0, 0] for nums=[1] and target 1"""
        nums = [1]
        target = 1
        expected = [0, 0]
        actual = search_range_v3(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should return [0, 1] for nums=[2, 2] and target 2"""
        nums = [2, 2]
        target = 2
        expected = [0, 1]
        actual = search_range_v3(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should return [0, 0] for nums=[1, 3] and target 1"""
        nums = [1, 3]
        target = 1
        expected = [0, 0]
        actual = search_range_v3(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_7(self):
        """should return [1, 1] for nums=[1, 4] and target 4"""
        nums = [1, 4]
        target = 4
        expected = [1, 1]
        actual = search_range_v3(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_8(self):
        """should return [1, 1] for nums=[1, 2, 3] and target 2"""
        nums = [1, 2, 3]
        target = 2
        expected = [1, 1]
        actual = search_range_v3(nums=nums, target=target)
        self.assertEqual(expected, actual)

    def test_9(self):
        """should return [0, 2] for nums=[3, 3, 3] and target 3"""
        nums = [3, 3, 3]
        target = 3
        expected = [0, 2]
        actual = search_range_v3(nums=nums, target=target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
