import unittest
from . import longest_self_contained_substring, max_substring_length


class LongestSelfContainedSubstringTestCase(unittest.TestCase):
    def test_1(self):
        s = "xyyx"
        expected = 2
        actual = longest_self_contained_substring(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "xyxy"
        expected = -1
        actual = longest_self_contained_substring(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "abacd"
        expected = 4
        actual = longest_self_contained_substring(s)
        self.assertEqual(expected, actual)

    def test_4(self):
        s = "aabbcc"
        expected = 4
        actual = longest_self_contained_substring(s)
        self.assertEqual(expected, actual)

    def test_5(self):
        s = "xyzxy"
        expected = 1
        actual = longest_self_contained_substring(s)
        self.assertEqual(expected, actual)

    def test_6(self):
        s = "abcde"
        expected = 4
        actual = longest_self_contained_substring(s)
        self.assertEqual(expected, actual)

    def test_7(self):
        s = "aaaa"
        expected = -1
        actual = longest_self_contained_substring(s)
        self.assertEqual(expected, actual)

    def test_8(self):
        s = "aabccbdd"
        expected = 6
        actual = longest_self_contained_substring(s)
        self.assertEqual(expected, actual)

    def test_9(self):
        s = "abcdefghigklmnopqrstuvwxyz"
        expected = 25
        actual = longest_self_contained_substring(s)
        self.assertEqual(expected, actual)

    def test_10(self):
        s = "abcabcabc"
        expected = -1
        actual = longest_self_contained_substring(s)
        self.assertEqual(expected, actual)

    def test_11(self):
        s = "aaabbbcccddd"
        expected = 9
        actual = longest_self_contained_substring(s)
        self.assertEqual(expected, actual)


class MaxSelfContainedSubstringTestCase(unittest.TestCase):
    def test_1(self):
        s = "xyyx"
        expected = 2
        actual = max_substring_length(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "xyxy"
        expected = -1
        actual = max_substring_length(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "abacd"
        expected = 4
        actual = max_substring_length(s)
        self.assertEqual(expected, actual)

    def test_4(self):
        s = "aabbcc"
        expected = 4
        actual = max_substring_length(s)
        self.assertEqual(expected, actual)

    def test_5(self):
        s = "xyzxy"
        expected = 1
        actual = max_substring_length(s)
        self.assertEqual(expected, actual)

    def test_6(self):
        s = "abcde"
        expected = 4
        actual = max_substring_length(s)
        self.assertEqual(expected, actual)

    def test_7(self):
        s = "aaaa"
        expected = -1
        actual = max_substring_length(s)
        self.assertEqual(expected, actual)

    def test_8(self):
        s = "aabccbdd"
        expected = 6
        actual = max_substring_length(s)
        self.assertEqual(expected, actual)

    def test_9(self):
        s = "abcdefghigklmnopqrstuvwxyz"
        expected = 25
        actual = max_substring_length(s)
        self.assertEqual(expected, actual)

    def test_10(self):
        s = "abcabcabc"
        expected = -1
        actual = max_substring_length(s)
        self.assertEqual(expected, actual)

    def test_11(self):
        s = "aaabbbcccddd"
        expected = 9
        actual = max_substring_length(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
