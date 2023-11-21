import unittest

from . import count_bits


class CountBitsTestCase(unittest.TestCase):
    def test_2(self):
        """input of 2 should return [0,1,1]"""
        n = 2
        expected = [0, 1, 1]
        actual = count_bits(n)
        self.assertEqual(expected, actual)

    def test_5(self):
        """input of 5 should return [0,1,1,2,1,2]"""
        n = 5
        expected = [0, 1, 1, 2, 1, 2]
        actual = count_bits(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
