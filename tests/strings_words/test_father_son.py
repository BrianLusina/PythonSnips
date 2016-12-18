from strings_words.father_son import sc
import unittest


class FatherSonTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sc("Aab"), "Aa")

    def test_2(self):
        self.assertEqual(sc("AabBc"), "AabB")

    def test_3(self):
        self.assertEqual(sc("SONson"), "SONson")

    def test_4(self):
        self.assertEqual(sc("FfAaTtHhEeRr"), "FfAaTtHhEeRr")

    def test_5(self):
        self.assertEqual(sc("SONsonfather"), "SONson")

    def test_6(self):
        self.assertEqual(sc("sonfather"), "")

    def test_7(self):
        self.assertEqual(sc("DONKEYmonkey"), "ONKEYonkey")

    def test_8(self):
        self.assertEqual(sc("monkeyDONKEY"), "onkeyONKEY")

    def test_9(self):
        self.assertEqual(sc("BANAna"), "ANAna")

