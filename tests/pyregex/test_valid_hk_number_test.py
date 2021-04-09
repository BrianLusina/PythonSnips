import unittest

from pyregex.valid_hk_number import is_valid_HK_phone_number, has_valid_HK_phone_number


class MyTestCase(unittest.TestCase):
    def test_is_valid_1(self):
        self.assertEqual(is_valid_HK_phone_number("1234 5678"), True)

    def test_is_valid_2(self):
        self.assertEqual(is_valid_HK_phone_number("1234 5678"), True)

    def test_is_valid_3(self):
        self.assertEqual(is_valid_HK_phone_number("2359 1478"), True)

    def test_is_valid_4(self):
        self.assertEqual(is_valid_HK_phone_number("85748475"), False)

    def test_is_valid_5(self):
        self.assertEqual(is_valid_HK_phone_number("3857  4756"), False)

    def test_is_valid_6(self):
        self.assertEqual(is_valid_HK_phone_number("sklfjsdklfjsf"), False)

    def test_is_valid_7(self):
        self.assertEqual(is_valid_HK_phone_number("     1234 5678   "), False)

    def test_is_valid_8(self):
        self.assertEqual(is_valid_HK_phone_number("123456789"), False)

    def test_is_valid_9(self):
        self.assertEqual(is_valid_HK_phone_number(" 987 634 "), False)

    def test_is_valid_10(self):
        self.assertEqual(is_valid_HK_phone_number("    6    "), False)

    def test_is_valid_11(self):
        self.assertEqual(is_valid_HK_phone_number("9684 2396"), True)

    def test_is_valid_12(self):
        self.assertEqual(is_valid_HK_phone_number("0000 0000"), True)

    def test_is_valid_13(self):
        self.assertEqual(is_valid_HK_phone_number("abcd efgh"), False)

    def test_is_valid_14(self):
        self.assertEqual(is_valid_HK_phone_number("836g 2986"), False)

    def test_is_valid_15(self):
        self.assertEqual(is_valid_HK_phone_number("8A65 2986"), False)

    def test_is_valid_16(self):
        self.assertEqual(is_valid_HK_phone_number("8c65 2i86"), False)

    def test_is_valid_17(self):
        self.assertEqual(is_valid_HK_phone_number("8368 2aE6"), False)

    def test_is_valid_18(self):
        self.assertEqual(is_valid_HK_phone_number("83680 28968"), False)

    def test_has_valid_0(self):
        self.assertEqual(has_valid_HK_phone_number("Hello, my phone number is 1234 5678"), True)

    def test_has_valid_1(self):
        self.assertEqual(has_valid_HK_phone_number("I wonder if 2359 1478 is a valid phone number?"), True)

    def test_has_valid_2(self):
        self.assertEqual(has_valid_HK_phone_number("85748475 is definitely invalid"), False)

    def test_has_valid_3(self):
        self.assertEqual(has_valid_HK_phone_number("'3857  4756' is so close to a valid phone number!"), False)

    def test_has_valid_4(self):
        self.assertEqual(has_valid_HK_phone_number("sklfjsdklfjsf"), False)

    def test_has_valid_5(self):
        self.assertEqual(has_valid_HK_phone_number("     1234 5678   "), True)

    def test_has_valid_6(self):
        self.assertEqual(has_valid_HK_phone_number("What about abcd efgh?"), False)

    def test_has_valid_7(self):
        self.assertEqual(has_valid_HK_phone_number("What about 9684 2396?"), True)

    def test_has_valid_8(self):
        self.assertEqual(has_valid_HK_phone_number("And 836g 2986?"), False)

    def test_has_valid_9(self):
        self.assertEqual(has_valid_HK_phone_number("skldfjsdklfjs0000 0000skldfjslkdfjs"), True)

    def test_has_valid_10(self):
        self.assertEqual(has_valid_HK_phone_number("123456789 is invalid"), False)

    def test_has_valid_11(self):
        self.assertEqual(has_valid_HK_phone_number("sdfssdfsdfdf 987 634 sdfsddsds"), False)

    def test_has_valid_12(self):
        self.assertEqual(has_valid_HK_phone_number("\n\n    6    \n\n"), False)

    def test_has_valid_13(self):
        self.assertEqual(has_valid_HK_phone_number("sdfsdsdfdf8A65 2986sdfsddfs"), False)

    def test_has_valid_14(self):
        self.assertEqual(has_valid_HK_phone_number("iwoeurwoeuwo8368 2aE6"), False)

    def test_has_valid_15(self):
        self.assertEqual(has_valid_HK_phone_number("8c65 2i86wioeruwioeruweoi"), False)


if __name__ == '__main__':
    unittest.main()
