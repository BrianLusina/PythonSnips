import unittest

from cryptography.maskify import maskify


class MaskifyTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(maskify("4556364607935616"), "############5616")

    def test_2(self):
        self.assertEqual(maskify("4556364607935616"), "############5616")

    def test_3(self):
        self.assertEqual(maskify("64607935616"), "#######5616")

    def test_4(self):
        self.assertEqual(maskify("1"), "1")

    def test_5(self):
        self.assertEqual(maskify(""), "")

    def test_6(self):
        self.assertEqual(maskify("Skippy"), "##ippy")

    def test_7(self):
        self.assertEqual(maskify("Nananananananananananananananana Batman!"),
                         "####################################man!")
