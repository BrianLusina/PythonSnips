import unittest

from pystrings.isomorphic_strings import is_isomorphic, is_isomorphic_v2


class IsIsomorphicTestCases(unittest.TestCase):
    def test_aab_and_xxy(self):
        str1 = "aab"
        str2 = "xxy"
        actual = is_isomorphic(str1, str2)

        self.assertTrue(actual)

    def test_aab_and_xyz(self):
        str1 = "aab"
        str2 = "xyz"
        actual = is_isomorphic(str1, str2)

        self.assertFalse(actual)

    def test_unequal_lengths(self):
        str1 = "aabx"
        str2 = "xyz"
        actual = is_isomorphic(str1, str2)

        self.assertFalse(actual)

    def test_invalid_input(self):
        str1 = None
        str2 = "xyz"
        actual = is_isomorphic(str1, str2)

        self.assertFalse(actual)

    def test_aab_and_xxy_v2(self):
        str1 = "aab"
        str2 = "xxy"
        actual = is_isomorphic_v2(str1, str2)

        self.assertTrue(actual)

    def test_aab_and_xyz_v2(self):
        str1 = "aab"
        str2 = "xyz"
        actual = is_isomorphic_v2(str1, str2)

        self.assertFalse(actual)

    def test_unequal_lengths_v2(self):
        str1 = "aabx"
        str2 = "xyz"
        actual = is_isomorphic_v2(str1, str2)

        self.assertFalse(actual)

    def test_invalid_input_v2(self):
        str1 = None
        str2 = "xyz"
        actual = is_isomorphic_v2(str1, str2)

        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
