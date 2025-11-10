import unittest
from . import group_anagrams


class GroupAnagramsTestCase(unittest.TestCase):
    def test_1(self):
        strs = ["eat", "beat", "neat", "tea"]
        expected = [["eat", "tea"], ["beat"], ["neat"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)

    def test_2(self):
        strs = ["duel", "dule", "speed", "spede", "deul", "cars"]
        expected = [["duel", "dule", "deul"], ["speed", "spede"], ["cars"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)

    def test_3(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected = [["eat","tea","ate"],["tan","nat"],["bat"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)

    def test_4(self):
        strs = ["word","sword","drow","rowd","iced","dice"]
        expected = [["word","drow","rowd"],["sword"],["iced","dice"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)

    def test_5(self):
        strs = ["eat","drink","sleep","repeat"]
        expected = [["eat"],["drink"],["sleep"],["repeat"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)

    def test_6(self):
        strs = ["hello","ohlle","dark"]
        expected = [["hello","ohlle"],["dark"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)

    def test_7(self):
        strs = ["eat","beat","neat","tea"]
        expected = [["eat","tea"],["beat"],["neat"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
