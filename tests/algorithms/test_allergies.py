import random
import unittest

from algorithms.allergies import Allergies


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
        self.assertEqual(Allergies(2).allergies(), ['peanuts'])

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

    def test_allergic_throws_error(self):
        self.assertRaises(TypeError, Allergies, "")

    def test_allergic_throws_error_for_non_integer_input(self):
        self.assertRaises(TypeError, Allergies, 5.2)

    def test_allergic_throws_error_for_none_inputs(self):
        with self.assertRaises(TypeError):
            Allergies(None)

    def test_allergic_with_score_of_1000(self):
        self.assertEqual(Allergies(1000).allergies(), ["cats", "chocolate", "pollen", "strawberries"])

    class MyAllergies(object):
        ALLERGY_SCORES = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
        }

        def __init__(self, score):
            if score is None or not isinstance(score, int):
                raise TypeError("Score must be an integer")
            self.score = score

        def is_allergic_to(self, allergen):
            """
            Checks if Tom is allergic to this particular allergen. Does a bitwise AND to perform the check
            :param allergen: the allergen to check for
            :return: True/False if Tom is allergic
            :rtype: bool
            """
            return self.ALLERGY_SCORES[allergen] & self.score

        def allergies(self):
            """
            Sorts the list of allergies in alphabetic order and returns them
            :return: a sorted list of all the allergies
             :rtype: list
            """
            return sorted(list(allergy for allergy in self.ALLERGY_SCORES if
                               self.is_allergic_to(allergy)))

    def test_random_number_input(self):
        x = random.randrange(255, 2000)
        self.assertEqual(Allergies(x).allergies(), self.MyAllergies(x).allergies())

    def test_negative_numbers(self):
        self.assertEqual(Allergies(-1).allergies(), ['cats', 'chocolate', 'eggs', 'peanuts',
                                                     'pollen', 'shellfish', 'strawberries', 'tomatoes'])

    def test_random_numbers(self):
        for x in range(1000, 1500):
            y = random.choice(range(x, x + 3))
            self.assertEqual(Allergies(y).allergies(), self.MyAllergies(y).allergies())


if __name__ == '__main__':
    unittest.main()
