import unittest
from parameterized import parameterized
from algorithms.stack.longest_valid_parentheses import longest_valid_parentheses

LONGEST_VALID_PARENTHESES_TEST_CASES = [
    ("(()", 2),
    (")()())", 4),
    ("", 0),
    ("())()", 2),
    ("(())", 4),
    (")(", 0),
    ("(", 0),
    ("()", 2),
    ("))(((", 0),
    ("(()())", 6),
    (")()((()))((((", 8),
    ("()(()))", 6),
    ("(()))())(", 4),
]


class LongestValidParenthesesTestCase(unittest.TestCase):
    @parameterized.expand(LONGEST_VALID_PARENTHESES_TEST_CASES)
    def test_longest_valid_parentheses(self, s: str, expected: int):
        actual = longest_valid_parentheses(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
