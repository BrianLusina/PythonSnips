import unittest


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(pattern(1), "1")

    def test2(self):
        self.assertEqual(pattern(2), "1\n22")

    def test3(self):
        self.assertEqual(pattern(5), "1\n22\n333\n4444\n55555")
