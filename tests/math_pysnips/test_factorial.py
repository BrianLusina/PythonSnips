import unittest
from pysnips.math_pysnips.factorial import Factorial


class Tests(unittest.TestCase):
    def test_8(self):
        self.assertEqual(40320, Factorial.fact(8))
