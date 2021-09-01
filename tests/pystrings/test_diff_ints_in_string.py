import unittest

from pystrings.diff_ints_in_string import num_different_integers


class NumberOfDifferentIntsInStringTestCase(unittest.TestCase):
    def test_a123bc34d8ef34(self):
        word = "a123bc34d8ef34"
        actual = num_different_integers(word)
        expected = 3
        self.assertEqual(expected, actual)

    def test_leet1234code234(self):
        word = "leet1234code234"
        actual = num_different_integers(word)
        expected = 2
        self.assertEqual(expected, actual)

    def test_a1b01c001(self):
        word = "a1b01c001"
        actual = num_different_integers(word)
        expected = 1
        self.assertEqual(expected, actual)

    def test_4(self):
        word = "4"
        actual = num_different_integers(word)
        expected = 1
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
