import unittest

from pystrings.how_much_love import how_much_i_love_you


class MyTestCase(unittest.TestCase):
    def test_love(self):
        self.assertEqual(how_much_i_love_you(7), "I love you")

    def test_lot(self):
        self.assertEqual(how_much_i_love_you(3), "a lot")

    def test_not_at_all(self):
        self.assertEqual(how_much_i_love_you(6), "not at all")


if __name__ == '__main__':
    unittest.main()
