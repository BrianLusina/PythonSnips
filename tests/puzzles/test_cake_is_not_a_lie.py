import unittest
from puzzles.cake_is_not_a_lie import cake_is_not_a_lie


class CakeIsNotALieTestCases(unittest.TestCase):
    def test_abcabcabcabc_returns_4(self):
        """abcabcabcabc should return 4"""
        s = "abcabcabcabc"
        actual = cake_is_not_a_lie(s)
        expected = 4
        self.assertEqual(expected, actual)

    def test_abccbaabccba_returns_2(self):
        """abccbaabccba should return 2"""
        s = "abccbaabccba"
        actual = cake_is_not_a_lie(s)
        expected = 2
        self.assertEqual(expected, actual)

    def test_empty_string_returns_0(self):
        """'' should return 0"""
        s = ""
        actual = cake_is_not_a_lie(s)
        expected = 0
        self.assertEqual(expected, actual)

    def test_repeating_character_returns_1(self):
        """ccccccccc should return 1"""
        s = "ccccccccc"
        actual = cake_is_not_a_lie(s)
        expected = 9
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
