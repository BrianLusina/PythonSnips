import unittest
from . import full_justify


class FullJustifyTestCase(unittest.TestCase):
    def test_1(self):
        """words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16"""
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        max_width = 16
        expected = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        actual = full_justify(words, max_width)
        self.assertListEqual(expected, actual)

    def test_2(self):
        """words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16"""
        words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        max_width = 16
        expected = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        actual = full_justify(words, max_width)
        self.assertListEqual(expected, actual)

    def test_3(self):
        """words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art",
        "is","everything","else","we","do"], maxWidth = 20"""
        words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
                 "Art", "is", "everything", "else", "we", "do"]
        max_width = 20
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
        actual = full_justify(words, max_width)
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
