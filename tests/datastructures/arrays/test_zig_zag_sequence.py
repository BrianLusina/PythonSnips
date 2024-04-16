import unittest
from datastructures.arrays.zig_zag_sequence import zig_zag_sequence


class ZigZagSequenceTestCase(unittest.TestCase):
    def test_2_3_5_1_4_returns_1_2_5_3_4(self):
        """input of [2,3,5,1,4] should return [1,2,5,3,4]"""
        a = [2, 3, 5, 1, 4]
        expected = [1, 2, 5, 4, 3]
        actual = zig_zag_sequence(a)
        self.assertEqual(expected, actual)

    def test_7_2_5_4_3_6_1_returns_1_2_3_7_6_5_4(self):
        """input of [7, 2, 5, 4, 3, 6, 1] should return [1, 2, 3, 7, 6, 5, 4]"""
        a = [7, 2, 5, 4, 3, 6, 1]
        expected = [1, 2, 3, 7, 6, 5, 4]
        actual = zig_zag_sequence(a)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
