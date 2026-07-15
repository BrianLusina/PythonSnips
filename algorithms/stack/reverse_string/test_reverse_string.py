import unittest
from typing import List
import copy
from parameterized import parameterized
from algorithms.stack.reverse_string import reverse_string, reverse_string_char_array

REVERSE_STRING_CHAR_ARRAY_TEST_CASES = [
    (["a", "e", "i", "o", "u"], ["u", "o", "i", "e", "a"]),
    (["A", "l", "e", "x"], ["x", "e", "l", "A"]),
    (["p", "y", "t", "h", "o", "n"], ["n", "o", "h", "t", "y", "p"]),
    (["x"], ["x"]),
]


class ReverseStringTestCase(unittest.TestCase):
    def test_one(self):
        text = "!evitacudE ot emocleW"
        actual = reverse_string(text)
        expected = "Welcome to Educative!"
        self.assertEqual(expected, actual)

    @parameterized.expand(REVERSE_STRING_CHAR_ARRAY_TEST_CASES)
    def test_reverse_string_char_array(self, s: List[str], expected: List[str]):
        s_copy = copy.deepcopy(s)
        reverse_string_char_array(s_copy)
        self.assertEqual(expected, s_copy)


if __name__ == "__main__":
    unittest.main()
