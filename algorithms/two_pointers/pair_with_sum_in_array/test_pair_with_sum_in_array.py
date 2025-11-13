import unittest
from . import pair_with_sum_in_collection


class PairWithSumTestCase(unittest.TestCase):
    def test_1(self):
        """should return for array of collection = [2,3,5,7,11,13], target = 13"""
        collection = [2, 3, 5, 7, 11, 13]
        target = 13
        expected = (0, 4)
        actual = pair_with_sum_in_collection(collection, target)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return for array of collection = [2,3,5,7,11,13], target = 13"""
        collection = [2, 3, 5, 7, 11, 13]
        target = 14
        expected = (1, 4)
        actual = pair_with_sum_in_collection(collection, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
