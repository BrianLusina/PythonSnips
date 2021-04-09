import unittest

from pystrings.alternate_case import to_alternating_case


class AlternateCaseTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(to_alternating_case("hello world"), "HELLO WORLD")

    def test_2(self):
        self.assertEqual(to_alternating_case("HELLO WORLD"), "hello world")

    def test_3(self):
        self.assertEqual(to_alternating_case("hello WORLD"), "HELLO world")

    def test_4(self):
        self.assertEqual(to_alternating_case("HeLLo WoRLD"), "hEllO wOrld")

    def test_5(self):
        self.assertEqual(to_alternating_case("12345"), "12345")

    def test_6(self):
        self.assertEqual(to_alternating_case("1a2b3c4d5e"), "1A2B3C4D5E")

    def test_7(self):
        self.assertEqual(to_alternating_case("String.prototype.toAlternatingCase"),
                         "sTRING.PROTOTYPE.TOaLTERNATINGcASE")

    def test_8(self):
        self.assertEqual(to_alternating_case(to_alternating_case("Hello World")), "Hello World")

    title1 = "altERnaTIng cAsE"

    # title2 becomes ALTerNAtiNG CaSe
    title2 = to_alternating_case(title1)

    def test_9(self):
        self.assertEqual(to_alternating_case(self.title2), self.title1)

    # title3 becomes altERnaTIng cAsE, back to title1
    title3 = to_alternating_case(title2)

    def test_10(self):
        self.assertEqual(to_alternating_case(self.title3), "ALTerNAtiNG CaSe")

    # title4 becomes ALTerNAtiNG CaSe
    title4 = to_alternating_case(title3)

    def test_11(self):
        self.assertEqual(to_alternating_case(self.title4), "altERnaTIng cAsE")

    # title5 becomes altERnaTIng cAsE
    title5 = to_alternating_case(title4)

    def test_12(self):
        self.assertEqual(to_alternating_case(self.title5), self.title4)

    title6 = "altERnaTIng cAsE <=> ALTerNAtiNG CaSe"
    # title7 becomes "ALTerNAtiNG CaSe <=> altERnaTIng cAsE"
    title7 = to_alternating_case(title6)

    def test_13(self):
        self.assertEqual(to_alternating_case(self.title7), self.title6)

    # title8 changes to title6
    title8 = to_alternating_case(title7)

    def test_14(self):
        self.assertEqual(to_alternating_case(self.title8), self.title7)

    # title9 changes to title7
    title9 = to_alternating_case(title8)

    def test_15(self):
        self.assertEqual(to_alternating_case(self.title9), self.title8)

    # title10 changes to title8
    title10 = to_alternating_case(title9)

    def test_16(self):
        self.assertEqual(to_alternating_case(self.title10), self.title9)
