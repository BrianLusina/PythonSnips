import unittest

from algorithms.arrays.next_permutation import next_permutation


class NextPermutationTestCase(unittest.TestCase):
    def test_123(self):
        arr = [1, 2, 3]
        expected = [1, 3, 2]
        next_permutation(arr)
        self.assertEqual(expected, arr)

    def test_321(self):
        arr = [3, 2, 1]
        expected = [1, 2, 3]
        next_permutation(arr)
        self.assertEqual(expected, arr)

    def test_115(self):
        arr = [1, 1, 5]
        expected = [1, 5, 1]
        next_permutation(arr)
        self.assertEqual(expected, arr)

    def test_1(self):
        arr = [1]
        expected = [1]
        next_permutation(arr)
        self.assertEqual(expected, arr)


if __name__ == '__main__':
    unittest.main()
