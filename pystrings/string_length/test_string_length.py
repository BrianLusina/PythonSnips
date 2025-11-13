import unittest
from . import iterative_string_len, recursive_string_len


class StringLengthTestCases(unittest.TestCase):
    def test_1_iterative(self):
        """should return 16 for input of LucidProgramming"""
        input_str = "LucidProgramming"
        expected = len(input_str)
        actual = iterative_string_len(input_str)
        self.assertEqual(expected, actual)

    def test_1_recursive(self):
        """should return 16 for input of LucidProgramming"""
        input_str = "LucidProgramming"
        expected = len(input_str)
        actual = recursive_string_len(input_str)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
