import unittest
from pysnips.math_pysnips.climb_sequence import climb


class Tests(unittest.TestCase):
    def Test_13(self):
        self.assertEqual(climb(13), [1, 3, 6, 13])
