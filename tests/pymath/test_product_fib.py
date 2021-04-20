import unittest

from pymath.xbonacci.product_fib import productFib


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(productFib(4895), [55, 89, True])

    def test_2(self):
        self.assertEqual(productFib(5895), [89, 144, False])

    def test_3(self):
        self.assertEqual(productFib(714), [21, 34, True])

    def test_4(self):
        self.assertEqual(productFib(800), [34, 55, False])

    def test_5(self):
        self.assertEqual(productFib(20), [5, 8, False])


if __name__ == '__main__':
    unittest.main()
