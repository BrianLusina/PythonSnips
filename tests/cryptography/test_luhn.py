import unittest
from collections import Counter

from cryptography.luhn import Luhn


class LuhnTests(unittest.TestCase):
    def test_addends(self):
        # uses a Counter to avoid specifying order of return value
        self.assertEqual(Counter([1, 4, 1, 4, 1]),
                         Counter(Luhn(12121).
                                 addends()))

    def test_addends_large(self):
        # uses a Counter to avoid specifying order of return value
        self.assertEqual(Counter([7, 6, 6, 1]),
                         Counter(Luhn(8631).addends()))

    def test_checksum1(self):
        self.assertEqual(22, Luhn(4913).checksum())

    def test_ckecksum2(self):
        self.assertEqual(21, Luhn(201773).checksum())

    def test_invalid_number(self):
        self.assertFalse(Luhn(738).is_valid())

    def test_valid_number(self):
        self.assertTrue(Luhn(8739567).is_valid())

    def test_create_valid_number1(self):
        self.assertEqual(1230, Luhn.create(123))

    def test_create_valid_number2(self):
        self.assertEqual(8739567, Luhn.create(873956))

    def test_create_valid_number3(self):
        self.assertEqual(8372637564, Luhn.create(837263756))

    def test_is_valid_can_be_called_repeatedly(self):
        # This test was added, because we saw many implementations
        # in which the first call to is_valid() worked, but the
        # second call failed().
        number = Luhn(8739567)
        self.assertTrue(number.is_valid())
        self.assertTrue(number.is_valid())

    def test_1(self):
        self.assertEqual(Luhn.is_card_valid("5457 6238 9823 4311"), True)

    def test_2(self):
        self.assertEqual(Luhn.is_card_valid("8895 6238 9323 4311"), False)

    def test_3(self):
        self.assertEqual(Luhn.is_card_valid("5457 6238 5568 4311"), False)

    def test_4(self):
        self.assertEqual(Luhn.is_card_valid("5457 6238 9323 4311"), False)

    def test_5(self):
        self.assertEqual(Luhn.is_card_valid("5457 1125 9323 4311"), False)

    def test_6(self):
        self.assertEqual(Luhn.is_card_valid("0000 0300 0000 0000"), False)

    def test_7(self):
        self.assertEqual(Luhn.is_card_valid("5457 6238 1251 4311"), False)

    def test_8(self):
        self.assertEqual(Luhn.is_card_valid("5457 6238 0254 4311"), False)

    def test_9(self):
        self.assertEqual(Luhn.is_card_valid("0000 0000 0000 0000"), True)

    def test_10(self):
        self.assertEqual(Luhn.is_card_valid("5457 1111 9323 4311"), False)

    def test_11(self):
        self.assertEqual(Luhn.is_card_valid("5457 6238 9823 4311"), True)

    def test_12(self):
        self.assertEqual(Luhn.is_card_valid("1145 6238 9323 4311"), False)

    def test_13(self):
        self.assertEqual(Luhn.is_card_valid("8888 8888 8888 8888"), True)

    def test_14(self):
        self.assertEqual(Luhn.is_card_valid("0025 2521 9323 4311"), False)

    def test_15(self):
        self.assertEqual(Luhn.is_card_valid("5457 6238 9323 4311"), False)

    def test_16(self):
        self.assertEqual(Luhn.is_card_valid("5458 4444 9323 4311"), False)

    def test_17(self):
        self.assertEqual(Luhn.is_card_valid("5457 6238 3333 4311"), False)

    def test_18(self):
        self.assertEqual(Luhn.is_card_valid("0123 4567 8901 2345"), False)

    def test_19(self):
        self.assertEqual(Luhn.is_card_valid("2222 2222 2222 2224"), True)

    def test_20(self):
        self.assertEqual(Luhn.is_card_valid("1252 6238 9323 4311"), False)

    def test_21(self):
        self.assertEqual(Luhn.is_card_valid("9999 9999 9999 9995"), True)

    def test_22(self):
        self.assertEqual(Luhn.is_card_valid("4444 4444 4444 4448"), True)

    def test_23(self):
        self.assertEqual(Luhn.is_card_valid("5457 6238 9323 1252"), False)

    def test_24(self):
        self.assertEqual(Luhn.is_card_valid("5555 5555 5555 5557"), True)

    def test_25(self):
        self.assertEqual(Luhn.is_card_valid("1234 5678 9012 3452"), True)

    def test_26(self):
        self.assertEqual(Luhn.is_card_valid("1111 1111 1111 1117"), True)

    def test_27(self):
        self.assertEqual(Luhn.is_card_valid("3333 3333 3333 3331"), True)

    def test_28(self):
        self.assertEqual(Luhn.is_card_valid("6666 6666 6666 6664"), True)


if __name__ == '__main__':
    unittest.main()
