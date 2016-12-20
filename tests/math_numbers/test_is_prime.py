import unittest
from math_numbers.is_prime import is_prime, divisors


class PrimeTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_prime(0), False, "0 is not prime")

    def test_2(self):
        self.assertEqual(is_prime(1), False, "1 is not prime")

    def test_3(self):
        self.assertEqual(is_prime(2), True, "2 is prime")


class DivisorTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(divisors(4), 3)

    def test_2(self):
        self.assertEqual(divisors(5), 2)

    def test_3(self):
        self.assertEqual(divisors(12), 6)

    def test_4(self):
        self.assertEqual(divisors(30), 8)
