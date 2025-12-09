import unittest
from typing import List
from parameterized import parameterized
from pystrings.parenthesis.remove_invalid_parenthesis import (
    remove_invalid_parentheses,
    remove_invalid_parentheses_2,
)


class RemoveInvalidParenthesisTestCases(unittest.TestCase):
    @parameterized.expand(
        [
            ("a())b()x(", ["a()b()x"]),
            ("(bn)())()", ["(bn)()()", "(bn())()"]),
            ("ae)i)o((u", ["aeiou"]),
            ("(()()((", ["()()", "(())"]),
            ("()())()", ["()()()", "(())()"]),
            ("())()(", ["()()"]),
            ("()())()", ["()()()", "(())()"]),
            ("))((", [""]),
            ("()())()", ["()()()", "(())()"]),
        ]
    )
    def test_remove_invalid_parenthesis(self, s: str, expected: List[str]):
        actual = remove_invalid_parentheses(s)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            ("a())b()x(", ["a()b()x"]),
            ("(bn)())()", ["(bn)()()", "(bn())()"]),
            ("ae)i)o((u", ["aeiou"]),
            ("(()()((", ["()()", "(())"]),
            ("()())()", ["()()()", "(())()"]),
            ("())()(", ["()()"]),
            ("()())()", ["()()()", "(())()"]),
            ("))((", [""]),
            ("()())()", ["()()()", "(())()"]),
        ]
    )
    def test_remove_invalid_parenthesis_2(self, s: str, expected: List[str]):
        actual = remove_invalid_parentheses_2(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
