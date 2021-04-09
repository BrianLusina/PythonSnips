import unittest

from pystrings.hexadecimal import Hexadecimal


class HexadecimalTest(unittest.TestCase):
    def setUp(self):
        self.hexa = Hexadecimal()
        self.hexa_prcpl = Hexadecimal()

    def test_valid_hexa1(self):
        self.assertEqual(1, self.hexa.hex_built_in('1'))

    def test_valid_hexa2(self):
        self.assertEqual(12, self.hexa.hex_built_in('c'))

    def test_valid_hexa3(self):
        self.assertEqual(16, self.hexa.hex_built_in('10'))

    def test_valid_hexa4(self):
        self.assertEqual(175, self.hexa.hex_built_in('af'))

    def test_valid_hexa5(self):
        self.assertEqual(256, self.hexa.hex_built_in('100'))

    def test_valid_hexa6(self):
        self.assertEqual(105166, self.hexa.hex_built_in('19ACE'))

    def test_valid_hexa7(self):
        self.assertEqual(0, self.hexa.hex_built_in('000000'))

    def test_valid_hexa8(self):
        self.assertEqual(16776960, self.hexa.hex_built_in('ffff00'))

    def test_valid_hexa9(self):
        self.assertEqual(65520, self.hexa.hex_built_in('00fff0'))

    def test_invalid_hexa(self):
        with self.assertRaises(ValueError):
            self.hexa.hex_built_in('carrot')

    def test_valid_hexa1_1st_principles(self):
        self.assertEqual(1, self.hexa_prcpl.hexa_first_principles('1'))

    def test_valid_hexa2_1st_principles(self):
        self.assertEqual(12, self.hexa_prcpl.hexa_first_principles('c'))

    def test_valid_hexa3_1st_principles(self):
        self.assertEqual(16, self.hexa_prcpl.hexa_first_principles('10'))

    def test_valid_hexa4_1st_principles(self):
        self.assertEqual(175, self.hexa_prcpl.hexa_first_principles('af'))

    def test_valid_hexa5_1st_principles(self):
        self.assertEqual(256, self.hexa_prcpl.hexa_first_principles('100'))

    def test_valid_hexa6_1st_principles(self):
        self.assertEqual(105166, self.hexa_prcpl.hexa_first_principles('19ACE'))

    def test_valid_hexa7_1st_principles(self):
        self.assertEqual(0, self.hexa_prcpl.hexa_first_principles('000000'))

    def test_valid_hexa8_1st_principles(self):
        self.assertEqual(16776960, self.hexa_prcpl.hexa_first_principles('ffff00'))

    def test_valid_hexa9_1st_principles(self):
        self.assertEqual(65520, self.hexa_prcpl.hexa_first_principles('00fff0'))

    def test_invalid_hexa_1st_principles(self):
        with self.assertRaises(ValueError):
            self.hexa_prcpl.hexa_first_principles('carrot')


if __name__ == '__main__':
    unittest.main()
