import unittest

from pymath.split_even_numbers import split_all_even_numbers


@unittest.skip
class SplitEvenNumbersTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEquals(split_all_even_numbers([1, 10, 1, 3], 0), [1, 5, 5, 1, 3])

    def test_2(self):
        self.assertEquals(split_all_even_numbers([1, 10, 1, 3], 1), [1, 1, 9, 1, 3])

    def test_3(self):
        self.assertEquals(split_all_even_numbers([1, 10, 1, 3], 2), [1, 5, 5, 1, 3])

    def test_4(self):
        self.assertEquals(split_all_even_numbers([1, 10, 1, 3], 3), [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3])

    def test_5(self):
        self.assertEquals(split_all_even_numbers([1, 1, 3, 8], 0), [1, 1, 3, 3, 5])

    def test_6(self):
        self.assertEquals(split_all_even_numbers([1, 1, 3, 8], 1), [1, 1, 3, 1, 7])

    def test_7(self):
        self.assertEquals(split_all_even_numbers([1, 1, 3, 8], 2), [1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1])

    def test_8(self):
        self.assertEquals(split_all_even_numbers([1, 1, 3, 8], 3), [1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
