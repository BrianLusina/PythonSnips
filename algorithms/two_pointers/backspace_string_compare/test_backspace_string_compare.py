import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.two_pointers.backspace_string_compare import (
    backspace_compare_two_pointers,
    backspace_compare_two_pointers_2,
    backspace_compare_build_string,
)

BACKSPACE_STRING_COMPARE_TEST_CASES = [
    ("x##y", "y", True),
    ("abc###", "def###", True),
    ("hello#world", "hellworld", True),
    ("a##b##c", "c", True),
    ("coding", "coding", True),
    ("ab#c", "ac", True),
    ("ab#c", "bc", False),
    ("abc###", "xyz###", True),
    ("#", "#", True),
    ("ab#c", "ad#c", True),
    ("ab##", "c#d#", True),
    ("a#c", "b", False),
]


class BackspaceStringCompareTestCase(unittest.TestCase):
    @parameterized.expand(
        BACKSPACE_STRING_COMPARE_TEST_CASES, name_func=custom_test_name_func
    )
    def test_backspace_string_compare_two_pointers(
        self, s: str, t: str, expected: bool
    ):
        actual = backspace_compare_two_pointers(s, t)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        BACKSPACE_STRING_COMPARE_TEST_CASES, name_func=custom_test_name_func
    )
    def test_backspace_string_compare_two_pointers_2(
        self, s: str, t: str, expected: bool
    ):
        actual = backspace_compare_two_pointers_2(s, t)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        BACKSPACE_STRING_COMPARE_TEST_CASES, name_func=custom_test_name_func
    )
    def test_backspace_compare_build_string(self, s: str, t: str, expected: bool):
        actual = backspace_compare_build_string(s, t)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
