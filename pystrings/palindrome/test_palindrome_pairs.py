import unittest
from .palindrome_pairs import palindrome_pairs, palindrome_pairs_2


class PalindromePairsTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(palindrome_pairs(["bat", "tab", "cat"]), [[0, 1], [1, 0]])

    def test_two(self):
        self.assertEqual(
            palindrome_pairs(["dog", "cow", "tap", "god", "pat"]),
            [[0, 3], [2, 4], [3, 0], [4, 2]],
        )

    def test_three(self):
        self.assertEqual(
            palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]),
            [[0, 1], [1, 0], [2, 4], [3, 2]],
        )

    def test_four(self):
        """should return [[0,1],[1,0],[3,2],[2,4]] for words=["abcd","dcba","lls","s","sssll"]"""
        words = ["abcd", "dcba", "lls", "s", "sssll"]
        expected = [[0, 1], [1, 0], [2, 4], [3, 2]]
        actual = palindrome_pairs(words)

        self.assertEqual(expected, actual)

    def test_five(self):
        """should return [[0,1],[1,0]] for words=["a",""]"""
        words = ["a", ""]
        expected = [[0, 1], [1, 0]]
        actual = palindrome_pairs(words)

        self.assertEqual(expected, actual)


class PalindromePairs2Tests(unittest.TestCase):
    def test_one(self):
        """Should return [[0, 1], [1, 0]] for words = ["bat", "tab", "cat"]"""
        words = ["bat", "tab", "cat"]
        expected = [[0, 1], [1, 0]]
        actual = palindrome_pairs_2(words)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return [[0, 3], [2, 4], [3, 0], [4, 2]] for words = ["dog", "cow", "tap", "god", "pat"]"""
        words = ["dog", "cow", "tap", "god", "pat"]
        expected = [[0, 3], [2, 4], [3, 0], [4, 2]]
        actual = palindrome_pairs_2(words)

        self.assertEqual(expected, actual)

    def test_three(self):
        """should return [[0, 1], [1, 0], [2, 4], [3, 2]] for words ["abcd", "dcba", "lls", "s", "sssll"]"""
        words = ["abcd", "dcba", "lls", "s", "sssll"]
        expected = [[0, 1], [1, 0], [3, 2], [2, 4]]
        actual = palindrome_pairs_2(words)
        self.assertEqual(expected, actual)

    def test_four(self):
        """should return [[0,1],[1,0],[3,2],[2,4]] for words=["abcd","dcba","lls","s","sssll"]"""
        words = ["abcd", "dcba", "lls", "s", "sssll"]
        expected = [[0, 1], [1, 0], [3, 2], [2, 4]]
        actual = palindrome_pairs_2(words)

        self.assertEqual(expected, actual)

    def test_five(self):
        """should return [[0,1],[1,0]] for words=["a",""]"""
        words = ["a", ""]
        expected = [[0, 1], [1, 0]]
        actual = palindrome_pairs_2(words)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
