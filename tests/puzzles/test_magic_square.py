import unittest

from puzzles.magic_square import magic_square


class MagicSquareTestCases(unittest.TestCase):
    def test_empty_array_input_should_return_false(self):
        """>>>> Empty array input should return false"""
        self.assertEqual(magic_square([]), False)

    def test_none_type_input_should_return_false(self):
        """>>>> None inputs should return False"""
        self.assertFalse(magic_square(None))

    def test_none_list_object_inputs_should_return_false(self):
        """>>>> Inputs that are not lists should return false"""
        self.assertFalse(magic_square(5))

    def test_valid_array_should_return_true(self):
        """>>>> Valid input array should return true"""
        arr = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
        self.assertTrue(magic_square(arr))

    def test_valid_array_should_return_false(self):
        """>>>> Valid array input should return False"""
        arr = [[8, 6, 1], [3, 5, 7], [4, 9, 2]]
        self.assertFalse(magic_square(arr))

    def test_valid_arr_should_return_false(self):
        """>>>> Valid array should return false"""
        arr = [[9, 14, 7], [8, 10, 12], [13, 6, 11]]
        self.assertTrue(magic_square(arr))


if __name__ == '__main__':
    unittest.main()
