import unittest

from pystrings.seven_ate9 import seven_ate9


class SevenAte9Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(seven_ate9('165561786121789797'), '16556178612178977')

    def test_2(self):
        self.assertEqual(seven_ate9('797'), "77")

    def test_3(self):
        self.assertEqual(seven_ate9('7979797'), "7777")
