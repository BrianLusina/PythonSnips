import unittest
from . import sorted_squared_array, sorted_squared_array_2


class SortedSquaredArrayTestCases(unittest.TestCase):
    def test_1(self):
        """for an input of [1,2,3,5,6,8,9] it should return [1, 4, 9,25, 36, 64, 81]"""
        input_array = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sorted_squared_array(input_array)
        self.assertEqual(expected, actual)

    def test_2(self):
        """for an input of [1] it should return [1]"""
        input_array = [1]
        expected = [1]
        actual = sorted_squared_array(input_array)
        self.assertEqual(expected, actual)

    def test_3(self):
        """for an input of [-7,-3,2,3,11] it should return [4,9,9,49,121]"""
        input_array = [-7,-3,2,3,11]
        expected = [4,9,9,49,121]
        actual = sorted_squared_array(input_array)
        self.assertEqual(expected, actual)


class SortedSquaredArray2TestCases(unittest.TestCase):
    def test_1(self):
        """for an input of [1,2,3,5,6,8,9] it should return [1, 4, 9,25, 36, 64, 81]"""
        input_array = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sorted_squared_array_2(input_array)
        self.assertEqual(expected, actual)

    def test_2(self):
        """for an input of [1] it should return [1]"""
        input_array = [1]
        expected = [1]
        actual = sorted_squared_array_2(input_array)
        self.assertEqual(expected, actual)

    def test_3(self):
        """for an input of [-7,-3,2,3,11] it should return [4,9,9,49,121]"""
        input_array = [-7,-3,2,3,11]
        expected = [4,9,9,49,121]
        actual = sorted_squared_array_2(input_array)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
