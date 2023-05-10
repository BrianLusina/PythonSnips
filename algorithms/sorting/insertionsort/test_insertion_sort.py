import unittest

from . import insertion_sort


class InsertionSortTestCase(unittest.TestCase):
    def test_1(self):
        """should sort a collection of [4,2,7,3,1] to [1,2,3,4,7]"""
        collection = [4, 2, 7, 3, 1]
        expected = [1, 2, 3, 4, 7]
        actual = insertion_sort(collection)

        self.assertEqual(expected, actual)

    def test_2(self):
        """should sort a collection of [10, 0, 4, 2, 7, 3, 1, -9] to [-9, 0, 1, 2, 3, 4, 7, 10]"""
        collection = [10, 0, 4, 2, 7, 3, 1, -9]
        expected = [-9, 0, 1, 2, 3, 4, 7, 10]
        actual = insertion_sort(collection)

        self.assertEqual(expected, actual)

    def test_3(self):
        """should sort a collection of [10] to [10]"""
        collection = [10]
        expected = [10]
        actual = insertion_sort(collection)

        self.assertEqual(expected, actual)

    def test_4(self):
        """should sort a collection of [10.3, 0.5, 4.6, 2.4, 7.3, 3.2, 1.5, -9.6] to [-9.6, 0.5, 1.5, 2.4, 3.2, 4.6, 7.3, 10.3]"""
        collection = [10.3, 0.5, 4.6, 2.4, 7.3, 3.2, 1.5, -9.6]
        expected = [-9.6, 0.5, 1.5, 2.4, 3.2, 4.6, 7.3, 10.3]
        actual = insertion_sort(collection)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
