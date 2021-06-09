import random
import unittest

from pymath.power_of_i import pofi


class PowerOfITestCase(unittest.TestCase):

    @classmethod
    def solution(cls, n):
        return ['1', 'i', '-1', '-i'][n % 4]

    def test_random_tests(self):
        for i in range(200):
            num = random.randint(1, 500)
            self.assertEquals(pofi(num), self.solution(num))

    def test_basic_tests(self):
        self.assertEqual(pofi(0), '1')
        self.assertEqual(pofi(1), 'i')
        self.assertEqual(pofi(2), '-1')
        self.assertEqual(pofi(3), '-i')
        self.assertEqual(pofi(4), '1')
        self.assertEqual(pofi(5), 'i')
        self.assertEqual(pofi(6), '-1')
        self.assertEqual(pofi(7), '-i')
        self.assertEqual(pofi(8), '1')
        self.assertEqual(pofi(9), 'i')
        self.assertEqual(pofi(10), '-1')


if __name__ == '__main__':
    unittest.main()
