import unittest

from pystrings.accum import accum


class AccumTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(accum("ZpglnRxqenU"),
                         "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")

    def test_2(self):
        self.assertEqual(accum("NyffsGeyylB"),
                         "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")

    def test_3(self):
        self.assertEqual(accum("MjtkuBovqrU"),
                         "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")

    def test_4(self):
        self.assertEqual(accum("EvidjUnokmM"),
                         "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")

    def test_5(self):
        self.assertEqual(accum("HbideVbxncC"),
                         "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")
