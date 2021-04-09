import unittest

from pyregex.valid_card import valid_card


# todo: failing tests
@unittest.skip
class ValidCardTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(valid_card("5457 6238 9823 4311"), True)

    def test_2(self):
        self.assertEqual(valid_card("8895 6238 9323 4311"), False)

    def test_3(self):
        self.assertEqual(valid_card("5457 6238 5568 4311"), False)

    def test_4(self):
        self.assertEqual(valid_card("5457 6238 9323 4311"), False)

    def test_5(self):
        self.assertEqual(valid_card("5457 1125 9323 4311"), False)

    def test_6(self):
        self.assertEqual(valid_card("0000 0300 0000 0000"), False)

    def test_7(self):
        self.assertEqual(valid_card("5457 6238 1251 4311"), False)

    def test_8(self):
        self.assertEqual(valid_card("5457 6238 0254 4311"), False)

    def test_9(self):
        self.assertEqual(valid_card("0000 0000 0000 0000"), True)

    def test_10(self):
        self.assertEqual(valid_card("5457 1111 9323 4311"), False)

    def test_11(self):
        self.assertEqual(valid_card("5457 6238 9823 4311"), True)

    def test_12(self):
        self.assertEqual(valid_card("1145 6238 9323 4311"), False)

    def test_13(self):
        self.assertEqual(valid_card("8888 8888 8888 8888"), True)

    def test_14(self):
        self.assertEqual(valid_card("0025 2521 9323 4311"), False)

    def test_15(self):
        self.assertEqual(valid_card("5457 6238 9323 4311"), False)

    def test_16(self):
        self.assertEqual(valid_card("5458 4444 9323 4311"), False)

    def test_17(self):
        self.assertEqual(valid_card("5457 6238 3333 4311"), False)

    def test_18(self):
        self.assertEqual(valid_card("0123 4567 8901 2345"), False)

    def test_19(self):
        self.assertEqual(valid_card("2222 2222 2222 2224"), True)

    def test_20(self):
        self.assertEqual(valid_card("1252 6238 9323 4311"), False)

    def test_21(self):
        self.assertEqual(valid_card("9999 9999 9999 9995"), True)

    def test_22(self):
        self.assertEqual(valid_card("4444 4444 4444 4448"), True)

    def test_23(self):
        self.assertEqual(valid_card("5457 6238 9323 1252"), False)

    def test_24(self):
        self.assertEqual(valid_card("5555 5555 5555 5557"), True)

    def test_25(self):
        self.assertEqual(valid_card("1234 5678 9012 3452"), True)

    def test_26(self):
        self.assertEqual(valid_card("1111 1111 1111 1117"), True)

    def test_27(self):
        self.assertEqual(valid_card("3333 3333 3333 3331"), True)

    def test_28(self):
        self.assertEqual(valid_card("6666 6666 6666 6664"), True)
