import unittest


def palindrome_pairs(words):
    for x in words:


def is_palindrome(a):
    return str(a) == str(a)[::-1]


class PalindromePairsTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(palindrome_pairs(["bat", "tab", "cat"]), [[0, 1], [1, 0]])

    def test_two(self):
        self.assertEqual(palindrome_pairs(["dog", "cow", "tap", "god", "pat"]), [[0, 3], [2, 4], [3, 0], [4, 2]])


    def test_three(self):
        self.assertEqual(palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]), [[0, 1], [1, 0], [2, 4], [3, 2]])
