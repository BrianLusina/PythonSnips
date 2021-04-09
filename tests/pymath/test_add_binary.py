import unittest

from pymath.binary.add_binary import add_binary


class AddBinaryTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add_binary(1, 1), "10")

    def test_2(self):
        self.assertEqual(add_binary(0, 1), "1")

    def test_3(self):
        self.assertEqual(add_binary(1, 0), "1")

    def test_4(self):
        self.assertEqual(add_binary(2, 2), "100")

    def test_5(self):
        self.assertEqual(add_binary(51, 12), "111111")
