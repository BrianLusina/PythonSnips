import unittest
from . import count_subarrays


class SubarraysWithFixedBoundsTestCase(unittest.TestCase):
    def test_1(self):
        nums = [2,1,4,3,2]
        min_k = 2
        max_k = 3
        expected = 1
        actual = count_subarrays(nums=nums, min_k=min_k, max_k=max_k)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1,2,3,2,1]
        min_k = 1
        max_k = 3
        expected = 5
        actual = count_subarrays(nums=nums, min_k=min_k, max_k=max_k)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [4,4,4]
        min_k = 4
        max_k = 4
        expected = 6
        actual = count_subarrays(nums=nums, min_k=min_k, max_k=max_k)
        self.assertEqual(expected, actual)

    def test_4(self):
        nums = [2,2,2]
        min_k = 4
        max_k = 4
        expected = 0
        actual = count_subarrays(nums=nums, min_k=min_k, max_k=max_k)
        self.assertEqual(expected, actual)

    def test_5(self):
        nums = [1,3,5,2,7,5]
        min_k = 1
        max_k = 5
        expected = 2
        actual = count_subarrays(nums=nums, min_k=min_k, max_k=max_k)
        self.assertEqual(expected, actual)

    def test_6(self):
        nums = [3,3,3]
        min_k = 3
        max_k = 3
        expected = 6
        actual = count_subarrays(nums=nums, min_k=min_k, max_k=max_k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
