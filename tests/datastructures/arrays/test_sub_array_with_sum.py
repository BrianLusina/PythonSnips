import unittest

from datastructures.arrays.sub_array_with_sum import sub_array_sum


class SubArrayWithSumTestCase(unittest.TestCase):
    def test_one(self):
        """should return [2, 4] for input of [1, 4, 20, 3, 10, 5] and sum of 33"""
        arr = [1, 4, 20, 3, 10, 5]
        s = 33
        expected = [2, 4]
        actual = sub_array_sum(arr, s)

        self.assertEqual(actual, expected)

    def test_two(self):
        """should return [1, 4] for input of [1, 4, 0, 0, 3, 10, 5] and sum of 7"""
        arr = [1, 4, 0, 0, 3, 10, 5]
        s = 7
        expected = [1, 4]
        actual = sub_array_sum(arr, s)

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
