import unittest
from random import randint

from pymath.circle_of_numbers import circle_of_numbers


class CircleOfNumbersTestCase(unittest.TestCase):
    def test_10_and_2_should_return_7(self):
        self.assertEqual(circle_of_numbers(10, 2), 7)

    def test_10_and_7_should_return_2(self):
        self.assertEqual(circle_of_numbers(10, 7), 2)

    def test_4_and_1_should_return_3(self):
        self.assertEqual(circle_of_numbers(4, 1), 3)

    def test_6_and_3_should_return_0(self):
        self.assertEqual(circle_of_numbers(6, 3), 0)

    def test_100_random_tests(self):
        def an(n, fst):
            return (n / 2 + fst) % n

        for _ in range(100):
            ddd = randint(2, 500) * 2
            eee = randint(0, ddd - 1)

            print(f"Testing for: n = {ddd}, fst= {eee}")

            ans = an(ddd, eee)
            self.assertEqual(circle_of_numbers(ddd, eee), ans, "It should work for random inputs too")


if __name__ == '__main__':
    unittest.main()
