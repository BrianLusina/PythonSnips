import unittest
from random import randint

from fundamentals.count_inner_calls import count_calls


def add(a, b):
    return a + b


def add_ten(a):
    return add(a, 10)


def misc_fun():
    return add(add_ten(3), add_ten(9))


def recurse_till_ten(i):
    if i == 10:
        return i
    return recurse_till_ten(i + 1)


def add_three(i):
    if i > 50:
        return i
    return substract_two(i + 3)


def substract_two(i):
    return add_three(i - 2)


def add_three_random(i, n):
    if i > n: return i
    return substract_two_random(i + 3, n)


def substract_two_random(i, n):
    return add_three_random(i - 2, n)


def random_wrapper(b):
    return lambda a: add_three_random(a, b)


class CountInnerCallsTestCase(unittest.TestCase):
    def test_sub_call_add(self):
        self.assertEqual(count_calls(add, 8, 12), (0, 20))

    def test_sub_call_add_ten(self):
        self.assertEqual(count_calls(add_ten, 5), (1, 15))

    def test_sub_call_misc_fun(self):
        self.assertEqual(count_calls(misc_fun), (5, 32))

    def test_recurse(self):
        self.assertEqual(count_calls(recurse_till_ten, 0), (10, 10))
        self.assertEqual(count_calls(recurse_till_ten, 7), (3, 10))
        self.assertEqual(count_calls(recurse_till_ten, 10), (0, 10))

    def test_trampoline_func_add_three(self):
        self.assertEqual(count_calls(add_three, 2), (98, 51))
        self.assertEqual(count_calls(add_three, 49), (4, 51))

    def test_trampoline_func_subtract_two(self):
        self.assertEqual(count_calls(substract_two, 0), (107, 51))
        self.assertEqual(count_calls(substract_two, 51), (5, 51))

    def test_random(self):
        a = randint(0, 40)
        b = randint(50, 100)
        self.assertEqual(count_calls(random_wrapper(b), a), (2 * (b - a) + 3, b + 1))


if __name__ == '__main__':
    unittest.main()
