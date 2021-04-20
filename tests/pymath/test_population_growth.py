import unittest

from pymath.population_growth import nb_year


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(nb_year(1500, 5, 100, 5000), 15)

    def test_2(self):
        self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)

    def test_3(self):
        self.assertEqual(nb_year(1500000, 0.25, 1000, 2000000), 94)
