import unittest
from random import randint

from pymath.primes.backward_read_primes import backwards_prime


class BackwardsPrimesTestCase(unittest.TestCase):
    def test_between_7000_and_7100(self):
        start = 7000
        end = 7100
        expected = [7027, 7043, 7057]
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_400_and_503(self):
        start = 400
        end = 503
        expected = []
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_2_and_100(self):
        start = 2
        end = 100
        expected = [13, 17, 31, 37, 71, 73, 79, 97]
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_9900_and_10000(self):
        start = 9900
        end = 10000
        expected = [9923, 9931, 9941, 9967]
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_501_and_599(self):
        start = 501
        end = 599
        expected = []
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_70000_and_70245(self):
        start = 70000
        end = 70245
        expected = [70001, 70009, 70061, 70079, 70121, 70141, 70163, 70241]
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_70485_and_70600(self):
        start = 70485
        end = 70600
        expected = [70489, 70529, 70573, 70589]
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_60000_and_70000(self):
        start = 60000
        end = 70000
        expected = []
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_109500_and_109700(self):
        start = 109500
        end = 109700
        expected = [109537, 109579, 109583, 109609, 109663]
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_100_and_403(self):
        start = 100
        end = 403
        expected = [107, 113, 149, 157, 167, 179, 199, 311, 337, 347, 359, 389]
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_7048500_and_7048600(self):
        start = 7048500
        end = 7048600
        expected = [7048519, 7048579]
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_1048500_and_1048600(self):
        start = 1048500
        end = 1048600
        expected = [1048571, 1048583]
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_1000001_and_1000100(self):
        start = 1000001
        end = 1000100
        expected = [1000033, 1000037, 1000039]
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_between_700000008_and_700000050(self):
        start = 700000008
        end = 700000050
        expected = [700000031]
        actual = backwards_prime(start, end)
        self.assertEqual(expected, actual)

    def test_random(self):
        def prime_si(a):
            if a == 2:
                return True
            if a < 2 or a % 2 == 0:
                return False
            return not any(a % x == 0 for x in range(3, int(a**0.5) + 1, 2))

        def backwards_prime_si(start, nd):
            return [
                x
                for x in range(start, nd + 1)
                if (str(x) != str(x)[::-1])
                and prime_si(x)
                and prime_si(int(str(x)[::-1]))
            ]

        i = 0
        while i < 40:
            n = randint(100, 10000000)
            m = n + randint(2000, 6000)
            exp = backwards_prime_si(n, m)
            actual = backwards_prime(n, m)
            self.assertEqual(exp, actual)
            i += 1


if __name__ == "__main__":
    unittest.main()
