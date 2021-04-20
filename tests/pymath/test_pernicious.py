import unittest

from pymath.pernicious import Pernicious


class PerniciousTests(unittest.TestCase):
    def test_1(self):
        pern = Pernicious(4)
        self.assertEqual(pern.is_pernicious(), [3])

    def test_2(self):
        pern = Pernicious(5)
        self.assertEqual(pern.is_pernicious(), [3, 5])

    def test_3(self):
        pern = Pernicious(232)
        self.assertEqual(pern.is_pernicious(),
                         [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 24, 25, 26, 28, 31, 33, 34, 35, 36,
                          37, 38, 40, 41, 42, 44, 47, 48, 49, 50, 52, 55, 56, 59, 61, 62, 65, 66, 67, 68, 69, 70, 72,
                          73, 74, 76, 79, 80, 81, 82, 84, 87, 88, 91, 93, 94, 96, 97, 98, 100, 103, 104, 107, 109, 110,
                          112, 115, 117, 118, 121, 122, 124, 127, 129, 130, 131, 132, 133, 134, 136, 137, 138, 140, 143,
                          144, 145, 146, 148, 151, 152, 155, 157, 158, 160, 161, 162, 164, 167, 168, 171, 173, 174, 176,
                          179, 181, 182, 185, 186, 188, 191, 192, 193, 194, 196, 199, 200, 203, 205, 206, 208, 211, 213,
                          214, 217, 218, 220, 223, 224, 227, 229, 230])

    def test_4(self):
        pern = Pernicious(0)
        self.assertEqual(pern.is_pernicious(), "No pernicious numbers")

    def test_5(self):
        pern = Pernicious(1)
        self.assertEqual(pern.is_pernicious(), "No pernicious numbers")

    def test_6(self):
        pern = Pernicious(-54)
        self.assertEqual(pern.is_pernicious(), "No pernicious numbers")

    def test_7(self):
        pern = Pernicious(6.99)
        self.assertEqual(pern.is_pernicious(), [3, 5, 6])

    def test_8(self):
        pern = Pernicious(-6.99)
        self.assertEqual(pern.is_pernicious(), "No pernicious numbers")

    def test_9(self):
        pern = Pernicious(42.42424242)
        self.assertEqual(pern.is_pernicious(),
                         [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 24, 25, 26, 28, 31, 33, 34, 35, 36,
                          37, 38, 40, 41, 42])

    def test_10(self):
        pern = Pernicious(2)
        self.assertEqual(pern.is_pernicious(), "No pernicious numbers")
