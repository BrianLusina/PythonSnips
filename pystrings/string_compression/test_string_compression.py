import unittest

from . import compress


class StringCompressionTestCases(unittest.TestCase):
    def test_a_a_b_b_c_c_c(self):
        """should return 6 for chars = ["a","a","b","b","c","c","c"]"""
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        expected = 6
        actual = compress(chars)
        self.assertEqual(expected, actual)

    def test_a(self):
        """should return 1 for chars = ["a"]"""
        chars = ["a"]
        expected = 1
        actual = compress(chars)
        self.assertEqual(expected, actual)

    def test_a_b_b_b_b_b_b_b_b_b_b_b_b(self):
        """should return 6 for chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]"""
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        expected = 4
        actual = compress(chars)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
