import unittest

from pymath.xbonacci.fibonacci import fib


class FibonacciTestCase(unittest.TestCase):
    def test1(self):
        self.assertEquals(fib(0, 1, 1), [0, 1, 1])

    def test5(self):
        self.assertEqual(fib(5, 8, 89), [5, 8, 13, 21, 34, 55, 89])

    def test2(self):
        self.assertEquals(fib(0, 1, 34), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test3(self):
        self.assertEquals(fib(0, 1, 610), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610])

    def test4(self):
        self.assertEquals(fib(5, 8, 144), [5, 8, 13, 21, 34, 55, 89, 144])


if __name__ == '__main__':
    unittest.main()
