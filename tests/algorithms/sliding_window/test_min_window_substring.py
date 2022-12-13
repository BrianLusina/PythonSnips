import unittest
from algorithms.sliding_window.minimum_window_substring import min_window


class MinWindowSubstringTestCase(unittest.TestCase):
    def test_s_is_ADOBECODEBANC_and_t_is_ABC(self):
        """s=ADOBECODEBANC and t = ABC should return BANC"""
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"
        actual = min_window(s, t)
        self.assertEqual(expected, actual)

    def test_s_is_a_and_t_is_a(self):
        """s=a and t = a should return a"""
        s = "a"
        t = "a"
        expected = "a"
        actual = min_window(s, t)
        self.assertEqual(expected, actual)

    def test_s_is_a_and_t_is_aa(self):
        """s=a and t = aa should return ''"""
        s = "a"
        t = "aa"
        expected = ""
        actual = min_window(s, t)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
