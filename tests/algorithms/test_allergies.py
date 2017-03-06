import unittest

from pysnips.algorithms.allergies import Allergies


class AllergiesTests(unittest.TestCase):
    def test_no_allergies_means_not_allergic(self):
        allergies = Allergies(0)
        self.assertFalse(allergies.is_allergic_to('peanuts'))
        self.assertFalse(allergies.is_allergic_to('cats'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    def test_is_allergic_to_eggs(self):
        self.assertTrue(Allergies(1).is_allergic_to('eggs'))

    def test_has_the_right_allergies(self):
        allergies = Allergies(5)
        self.assertTrue(allergies.is_allergic_to('eggs'))
        self.assertTrue(allergies.is_allergic_to('shellfish'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    def test_no_allergies_at_all(self):
        self.assertEqual(Allergies(0).allergies(), [])

    def test_allergic_to_just_peanuts(self):
        self.assertEqual( Allergies(2).allergies(), ['peanuts'])

    def test_allergic_to_everything(self):
        self.assertEqual(Allergies(255).allergies(),
                         sorted(('eggs peanuts shellfish strawberries tomatoes '
                                 'chocolate pollen cats').split())
                         )

    def test_ignore_non_allergen_score_parts(self):
        self.assertEqual(['eggs'], Allergies(257).allergies())

    def test_not_allergic_at_score_256(self):
        self.assertEqual(Allergies(256).allergies(), [])

    def test_allergic_at_eggs_score_257(self):
        self.assertEqual(Allergies(257).allergies(), ["eggs"])

    def test_allergic_peanuts_at_score_258(self):
        self.assertEqual(Allergies(258).allergies(), ["peanuts"])

    def test_allergic_to_eggs_peanuts_at_score_259(self):
        self.assertEqual(Allergies(259).allergies(), ["eggs", "peanuts"])

    def test_allergic_to_shellfish_at_score_260(self):
        self.assertEqual(Allergies(260).allergies(), ["shellfish"])


if __name__ == '__main__':
    unittest.main()
