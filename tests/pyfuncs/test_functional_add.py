import unittest
from random import randint
from pyfuncs.functional_add import add


class FunctionalAddTestCases(unittest.TestCase):
    def test_one(self):
        input_one = 1
        input_two = 3
        add_one = add(input_one)
        actual = add_one(input_two)
        expected = 4
        self.assertEqual(actual, expected)

    def test_random_tests(self):
        for i in range(100):
            a = randint(-1000, 1000)
            b = randint(-1000, 1000)
            self.assertEqual(add(a)(b), a + b, "Wrong result for " + str(a) + " + " + str(b))


if __name__ == '__main__':
    unittest.main()
