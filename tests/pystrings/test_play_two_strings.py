import unittest

from pystrings.play_two_strings import work_on_strings


class PlayOnStringsTestCase(unittest.TestCase):
    @unittest.skip("Until the algorithm is properly resolved")
    def test_basic(self):
        self.assertEqual(work_on_strings("abcdeFgtrzw", "defgGgfhjkwqe"), "abcDeFGtrzWDEFGgGFhjkWqE")
        self.assertEqual(work_on_strings("abc", "cde"), "abCCde")
        self.assertEqual(work_on_strings("abab", "bababa"), "ABABbababa")
        self.assertEqual(work_on_strings("abcdeFg", "defgG"), "abcDEfgDEFGg")


if __name__ == '__main__':
    unittest.main()
