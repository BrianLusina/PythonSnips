import unittest
from . import find_first_occurrence


class FindFirstOccurrenceTestCase(unittest.TestCase):
    def test_1(self):
        """should return 1 from arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100] and target =3 """
        arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
        target = 3
        expected = 1
        actual = find_first_occurrence(arr, target)

        self.assertEqual(expected, actual)

    def test_2(self):
        """should return -1 from arr = [2, 3, 5, 7, 11, 13, 17, 19] and target = 6 """
        arr = [2, 3, 5, 7, 11, 13, 17, 19]
        target = 6
        expected = -1
        actual = find_first_occurrence(arr, target)

        self.assertEqual(expected, actual)

    def test_3(self):
        """should return -1 from arr = [1 1 1 1 1 1 1 1 1 1 1 1] and target = 1 """
        arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        target = 1
        expected = 0
        actual = find_first_occurrence(arr, target)

        self.assertEqual(expected, actual)

    def test_4(self):
        """should return 3 from arr = [1 22 22 33 50 100 20000] and target = 33 """
        arr = [1, 22, 22, 33, 50, 100, 20000]
        target = 33
        expected = 3
        actual = find_first_occurrence(arr, target)

        self.assertEqual(expected, actual)

    def test_5(self):
        """should return -1 from arr = [4 6 7 7 7 20] and target = 8 """
        arr = [4, 6, 7, 7, 7, 20]
        target = 8
        expected = -1
        actual = find_first_occurrence(arr, target)

        self.assertEqual(expected, actual)

    def test_6(self):
        """should return 3 from arr = [6 7 9 10 10 10 90] and target = 10 """
        arr = [6, 7, 9, 10, 10, 10, 90]
        target = 10
        expected = 3
        actual = find_first_occurrence(arr, target)

        self.assertEqual(expected, actual)

    def test_7(self):
        """should return 0 from arr = [4] and target = 4 """
        arr = [4]
        target = 4
        expected = 0
        actual = find_first_occurrence(arr, target)

        self.assertEqual(expected, actual)

    def test_8(self):
        """should return 0 from arr = [2 3 5 7 11] and target = 2 """
        arr = [2, 3, 5, 7, 11]
        target = 2
        expected = 0
        actual = find_first_occurrence(arr, target)

        self.assertEqual(expected, actual)

    def test_9(self):
        """should return -1 from arr = [1 3 5 8 13 21] and target = 40 """
        arr = [1, 3, 5, 8, 13, 21]
        target = 40
        expected = -1
        actual = find_first_occurrence(arr, target)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
