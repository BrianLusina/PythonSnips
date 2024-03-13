import unittest
from . import str_str


class StrStrTestCase(unittest.TestCase):
    def test_sadbutsad_sad(self):
        """sadbutsad, needle = sad"""
        haystack = "sadbutsad"
        needle = "sad"
        expected = 0
        actual = str_str(haystack, needle)

        self.assertEqual(expected, actual)

    def test_leetcode_leeto(self):
        """leetcode, needle = leeto"""
        haystack = "leetcode"
        needle = "leeto"
        expected = -1
        actual = str_str(haystack, needle)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
