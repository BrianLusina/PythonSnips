import unittest

from datastructures.arrays.array_from_permutation import build_array


class BuildArrayFromPermTestCases(unittest.TestCase):
    def test_one(self):
        nums = [0, 2, 1, 5, 3, 4]
        actual = build_array(nums)
        expected = [0, 1, 2, 4, 5, 3]
        self.assertEqual(expected, actual)

    def test_two(self):
        nums = [5, 0, 1, 2, 3, 4]
        actual = build_array(nums)
        expected = [4, 5, 0, 1, 2, 3]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
