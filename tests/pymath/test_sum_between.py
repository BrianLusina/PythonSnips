import unittest

from pymath.sum_between import sum_between


class SumBetweenTests(unittest.TestCase):
    def shortDescription(self):
        return "Tests for {} checks if function sums the array and all numbers in between".format(sum_between.__name__)

    def test_only_accepts_a_list(self):
        with self.assertRaises(TypeError):
            sum_between(0)

    def test_raises_error_if_array_is_longer_than_2(self):
        with self.assertRaises(TypeError):
            sum_between([1, 2, 3])

    def test_raises_error_if_array_is_less_than_2(self):
        with self.assertRaises(TypeError):
            sum_between([1])

    def test_first_element_is_smaller(self):
        self.assertEqual(sum(range(1, 4)), sum_between([1, 3]), "Expected 6")

    def test_second_element_is_smaller(self):
        expected = sum(range(5, 9))
        self.assertEqual(expected, sum_between([8, 5]), "Expected {}".format(expected))

    def test_both_elements_are_equal(self):
        expected = 2
        self.assertEqual(expected, sum_between([2, 2]), "Expected {}".format(expected))

    def test_one_elements_is_less_than_0(self):
        expected = sum(range(-5, 3))
        self.assertEqual(expected, sum_between([-5, 2]), "Expected {}".format(expected))

    def test_both_elements_are_less_than_0(self):
        expected = sum(range(-5, -1))
        self.assertEqual(expected, sum_between([-5, -2]), "Expected {}".format(expected))
