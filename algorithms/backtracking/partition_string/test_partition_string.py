import unittest

from . import partition


class PartitionTestCase(unittest.TestCase):
    def test_aab(self):
        """should return [["aa","b"], ["a","a","b"]] from aab"""
        s = "aab"
        expected = [["aa", "b"], ["a", "a", "b"]]
        actual = partition(s)

        self.assertEqual(sorted(expected), sorted(actual))

    def test_aba(self):
        """should return [["aa","b"], ["a","a","b"]] from aba"""
        s = "aba"
        expected = [["aba"], ["a", "b", "a"]]
        actual = partition(s)

        self.assertEqual(sorted(expected), sorted(actual))


if __name__ == "__main__":
    unittest.main()
