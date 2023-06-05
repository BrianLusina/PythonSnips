import unittest
from . import gcd_of_strings_brute_force, gcd_of_strings_gcd


class GcdOfStringsBruteForceTestCase(unittest.TestCase):
    def test_abcabc_and_abc(self):
        """should return ABC from str1=ABCABC and str2=ABC"""
        str1 = "ABCABC"
        str2 = "ABC"
        expected = "ABC"
        actual = gcd_of_strings_brute_force(str1, str2)
        self.assertEqual(expected, actual)

    def test_ababab_and_abab(self):
        """should return AB from str1=ABABAB and str2=ABAB"""
        str1 = "ABABAB"
        str2 = "ABAB"
        expected = "AB"
        actual = gcd_of_strings_brute_force(str1, str2)
        self.assertEqual(expected, actual)

    def test_leet_and_code(self):
        """should return '' from str1=LEET and str2=CODE"""
        str1 = "LEET"
        str2 = "CODE"
        expected = ""
        actual = gcd_of_strings_brute_force(str1, str2)
        self.assertEqual(expected, actual)


class GcdOfStringsGcdTestCase(unittest.TestCase):
    def test_abcabc_and_abc(self):
        """should return ABC from str1=ABCABC and str2=ABC"""
        str1 = "ABCABC"
        str2 = "ABC"
        expected = "ABC"
        actual = gcd_of_strings_gcd(str1, str2)
        self.assertEqual(expected, actual)

    def test_ababab_and_abab(self):
        """should return AB from str1=ABABAB and str2=ABAB"""
        str1 = "ABABAB"
        str2 = "ABAB"
        expected = "AB"
        actual = gcd_of_strings_gcd(str1, str2)
        self.assertEqual(expected, actual)

    def test_leet_and_code(self):
        """should return '' from str1=LEET and str2=CODE"""
        str1 = "LEET"
        str2 = "CODE"
        expected = ""
        actual = gcd_of_strings_gcd(str1, str2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
