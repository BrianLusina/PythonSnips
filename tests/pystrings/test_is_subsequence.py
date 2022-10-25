import unittest

from pystrings.issubsequence import is_subsequence, is_subsequence_v2


class IsSubsequenceTestCases(unittest.TestCase):
    def test_one(self):
        """Test s=abc & t=ahbgdc"""
        s = "abc"
        t = "ahbgdc"
        self.assertTrue(is_subsequence(s, t))

    def test_two(self):
        """Test s=axc & t=ahbgdc"""
        s = "axc"
        t = "ahbgdc"
        self.assertFalse(is_subsequence(s, t))

    def test_three(self):
        """Test s='' & t=ahbgdc"""
        s = ""
        t = "ahbgdc"
        self.assertTrue(is_subsequence(s, t))

    def test_four(self):
        """Test s='b' & t=abc"""
        s = "b"
        t = "abc"
        self.assertTrue(is_subsequence(s, t))


class IsSubsequenceV2TestCases(unittest.TestCase):
    def test_one(self):
        """Test s=abc & t=ahbgdc"""
        s = "abc"
        t = "ahbgdc"
        self.assertTrue(is_subsequence_v2(s, t))

    def test_two(self):
        """Test s=axc & t=ahbgdc"""
        s = "axc"
        t = "ahbgdc"
        self.assertFalse(is_subsequence_v2(s, t))

    def test_three(self):
        """Test s='' & t=ahbgdc"""
        s = ""
        t = "ahbgdc"
        self.assertTrue(is_subsequence_v2(s, t))

    def test_four(self):
        """Test s='b' & t=abc"""
        s = "b"
        t = "abc"
        self.assertTrue(is_subsequence_v2(s, t))


if __name__ == '__main__':
    unittest.main()
