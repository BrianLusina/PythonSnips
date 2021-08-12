import unittest

from generators_and_iterators.iterators.recur_iter import replicate_iter, replicate_recur


class ReplicateIterTestCases(unittest.TestCase):
    def test_it_returns_a_list_of_replicated_numbers(self):
        result = replicate_iter(3, 5)
        self.assertEqual(result, [5, 5, 5], msg='It should produce a list of three fives for the input 3, 5')

    def test_it_returns_an_empty_list_for_0_times(self):
        result = replicate_iter(0, 5)
        self.assertEqual(result, [], msg='It should return an empty list if times == 0')

    def test_it_returns_an_empty_list_for_negative_times(self):
        result = replicate_iter(-1, 20)
        self.assertEqual(result, [], msg='It should return an empty list for negative times.')

    def test_it_raises_value_error_if_invalid_input(self):
        with self.assertRaises(ValueError):
            replicate_iter(1, [])

    def test_it_raises_value_error_if_invalid_number_of_times_to_repeat(self):
        with self.assertRaises(ValueError):
            replicate_iter([], 3)

    def test_it_can_repeat_strings(self):
        result = replicate_iter(3, 'str')
        self.assertEqual(result, ['str', 'str', 'str'], msg='Should replicate strings too')


class ReplicateRecurTestCases(unittest.TestCase):
    def test_it_returns_a_list_of_replicated_numbers(self):
        result = replicate_recur(4, 5)
        self.assertEqual(result, [5, 5, 5, 5], msg='It should produce a list of four fives for the input 4, 5')

    def test_it_returns_an_empty_list_for_0_times(self):
        result = replicate_recur(0, 5)
        self.assertEqual(result, [], msg='It should return an empty list if times == 0')

    def test_it_returns_an_empty_list_for_negative_times(self):
        result = replicate_recur(-1, 20)
        self.assertEqual(result, [], msg='It should return an empty list for negative times.')

    def test_it_raises_value_error_if_invalid_input(self):
        with self.assertRaises(ValueError):
            replicate_recur(1, [])

    def test_it_raises_value_error_if_invalid_number_of_times_to_repeat(self):
        with self.assertRaises(ValueError):
            replicate_recur([], 3)
