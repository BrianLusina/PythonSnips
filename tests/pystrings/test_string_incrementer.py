import unittest
from pystrings.string_incrementer import increment_string


class StringIncrementerTestCase(unittest.TestCase):
    def test_foo_returns_foo1(self):
        """foo returns foo1"""
        word = "foo"
        expected = "foo1"
        actual = increment_string(word)
        self.assertEqual(expected, actual)

    def test_foobar001_returns_foobar002(self):
        """foobar001 returns foobar002"""
        word = "foobar001"
        expected = "foobar002"
        actual = increment_string(word)
        self.assertEqual(expected, actual)

    def test_foobar1_returns_foobar2(self):
        """foobar1 returns foobar2"""
        word = "foobar1"
        expected = "foobar2"
        actual = increment_string(word)
        self.assertEqual(expected, actual)

    def test_foobar00_returns_foobar01(self):
        """foobar00 returns foobar01"""
        word = "foobar00"
        expected = "foobar01"
        actual = increment_string(word)
        self.assertEqual(expected, actual)

    def test_foobar99_returns_foobar100(self):
        """foobar99 returns foobar100"""
        word = "foobar99"
        expected = "foobar100"
        actual = increment_string(word)
        self.assertEqual(expected, actual)

    def test_foobar099_returns_foobar100(self):
        """foobar099 returns foobar100"""
        word = "foobar099"
        expected = "foobar100"
        actual = increment_string(word)
        self.assertEqual(expected, actual)

    def test_fo99obar99_returns_fo99obar100(self):
        """fo99obar99 returns fo99obar100"""
        word = "fo99obar99"
        expected = "fo99obar100"
        actual = increment_string(word)
        self.assertEqual(expected, actual)

    def test_empty_string_returns_1(self):
        """'' returns 1"""
        word = ""
        expected = "1"
        actual = increment_string(word)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
