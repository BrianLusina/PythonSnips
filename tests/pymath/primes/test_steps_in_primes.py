import unittest
from random import randint

from pymath.primes.steps_in_primes import step


def prime_sol(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0: return False
    return True


def step_sol(g, m, n):
    res = []
    i = m
    while i <= n - g:
        if prime_sol(i) and prime_sol(i + g):
            res.append(i)
            res.append(i + g)
            return res
        i += 1
    return None


class StepsInPrimesTestCase(unittest.TestCase):
    def test_basic_tests(self):
        self.assertEqual(step(2, 100, 110), [101, 103])
        self.assertEqual(step(4, 100, 110), [103, 107])
        self.assertEqual(step(6, 100, 110), [101, 107])
        self.assertEqual(step(8, 300, 400), [359, 367])
        self.assertEqual(step(10, 300, 400), [307, 317])

        self.assertEqual(step(4, 30000, 100000), [30109, 30113])
        self.assertEqual(step(6, 30000, 100000), [30091, 30097])
        self.assertEqual(step(8, 30000, 100000), [30089, 30097])
        self.assertEqual(step(11, 30000, 100000), None)
        self.assertEqual(step(16, 5, 20), None)
        self.assertEqual(step(2, 10000000, 11000000), [10000139, 10000141])

        self.assertEqual(step(52, 1300, 15000), [1321, 1373])
        self.assertEqual(step(10, 4900, 5000), [4909, 4919])
        self.assertEqual(step(30, 4900, 5000), [4903, 4933])
        self.assertEqual(step(2, 4900, 5000), [4931, 4933])
        self.assertEqual(step(2, 104000, 105000), [104087, 104089])

        self.assertEqual(step(2, 4900, 4919), None)
        self.assertEqual(step(7, 4900, 4919), None)
        self.assertEqual(step(4, 30115, 100000), [30133, 30137])
        self.assertEqual(step(4, 30140, 100000), [30319, 30323])
        self.assertEqual(step(4, 30000, 30325), [30109, 30113])

    def test_random_tests(self):
        for _ in range(0, 50):
            n = randint(1000, 1000000)
            self.assertEqual(step(2, n, n + 100000), step_sol(2, n, n + 100000))
            self.assertEqual(step(4, n, n + 100000), step_sol(4, n, n + 100000))
            self.assertEqual(step(6, n, n + 100000), step_sol(6, n, n + 100000))
            self.assertEqual(step(8, n, n + 100000), step_sol(8, n, n + 100000))
            k = randint(0, 2)
            if k % 2 == 0:
                self.assertEqual(step(2, n + 1000, n + 10000), step_sol(2, n + 1000, n + 10000))
            else:
                self.assertEqual(step(4, n + 1000, n + 10000), step_sol(4, n + 1000, n + 10000))


if __name__ == '__main__':
    unittest.main()
