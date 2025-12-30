# -*- coding: utf-8 -*-
import unittest
from random import choice, randint
from string import ascii_letters
from typing import Union
from parameterized import parameterized
from pystrings.palindrome import (
    is_palindrome,
    smallest_palindrome,
    largest_palindrome,
    is_palindrome_number,
    is_palindrome_number_2,
)
from pystrings.palindrome.longest_palindrome import longest_palindrome


class LongestPalindromeTests(unittest.TestCase):
    def single_letter(self):
        self.assertEqual(longest_palindrome("a"), 1)

    def test_double_letter(self):
        self.assertEqual(longest_palindrome("aa"), 2)

    def test_3(self):
        self.assertEqual(longest_palindrome("baa"), 2)

    def test_4(self):
        self.assertEqual(longest_palindrome("aab"), 2)

    def test_5(self):
        self.assertEqual(longest_palindrome("abcdefghba"), 1)

    def test_6(self):
        self.assertEqual(longest_palindrome("baablkj12345432133d"), 9)


class IsPalindromeTests(unittest.TestCase):
    def test_7(self):
        self.assertEqual(is_palindrome("anna"), True)

    def test_8(self):
        self.assertEqual(is_palindrome("walter"), False)

    def test_9(self):
        self.assertEqual(is_palindrome("12321"), True)

    def test_10(self):
        self.assertEqual(is_palindrome("123456"), False)

    def test_11(self):
        word = "Was it a cat I saw?"
        actual = is_palindrome(word)
        self.assertTrue(actual)

    def test_12(self):
        word = "Never odd or even"
        actual = is_palindrome(word)
        self.assertTrue(actual)

    def test_13(self):
        word = "radar"
        actual = is_palindrome(word)
        self.assertTrue(actual)

    def test_14(self):
        word = "Live on time, emit no evil"
        actual = is_palindrome(word)
        self.assertTrue(actual)

    @staticmethod
    def generate_test_case() -> Union[str, int]:
        if randint(0, 1000):
            test_case = randint(0, 10000000)
        else:
            test_case = "".join(choice(ascii_letters) for _ in range(randint(1, 1000)))
            if randint(0, 1000):
                test_case = "%s%s" % (test_case, test_case[::-1])

        return test_case

    @staticmethod
    def reference(s):
        return str(s) == str(s)[::-1]

    def test_15(self):
        for _ in range(100):
            test_case = self.generate_test_case()
            self.assertEqual(is_palindrome(str(test_case)), self.reference(test_case))


IS_PALINDROME_TEST_CASES = [
    (353, True),
    (-353, False),
    (90, False),
    (12321, True),
    (10101, True),
    (1000021, False),
    (0, True),
    (2147447412, True),
]


class IsPalindromeNumber(unittest.TestCase):
    @parameterized.expand(IS_PALINDROME_TEST_CASES)
    def test_is_palindrome_number(self, x: int, expected: bool):
        actual = is_palindrome_number(x)
        self.assertEqual(actual, expected)

    @parameterized.expand(IS_PALINDROME_TEST_CASES)
    def test_is_palindrome_number_2(self, x: int, expected: bool):
        actual = is_palindrome_number_2(x)
        self.assertEqual(actual, expected)


class SmallestPalindromeTests(unittest.TestCase):
    def test_smallest_palindrome_from_double_digit_factors(self):
        value, factors = smallest_palindrome(max_factor=99, min_factor=10)
        self.assertEqual(121, value)
        self.assertEqual({11}, set(factors))

    def test_smallest_palindrome_from_triple_digit_factors(self):
        value, factors = smallest_palindrome(max_factor=999, min_factor=100)
        self.assertEqual(10201, value)
        self.assertEqual({101, 101}, set(factors))


class LargestPalindromeTests(unittest.TestCase):
    def test_largest_palindrome_from_single_digit_factors(self):
        value, factors = largest_palindrome(max_factor=9)
        self.assertEqual(9, value)
        self.assertIn(set(factors), [{1, 9}, {3, 3}])

    def test_largest_palindrome_from_double_digit_factors(self):
        value, factors = largest_palindrome(max_factor=99, min_factor=10)
        self.assertEqual(9009, value)
        self.assertEqual({91, 99}, set(factors))

    def test_largest_palindrome_from_triple_digit_factors(self):
        value, factors = largest_palindrome(max_factor=999, min_factor=100)
        self.assertEqual(906609, value)
        self.assertEqual({913, 993}, set(factors))


if __name__ == "__main__":
    unittest.main()
