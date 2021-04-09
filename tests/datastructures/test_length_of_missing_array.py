import unittest

from datastructures.lists.missing_array import get_length_of_missing_array

tests = (
    ([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]], 3),
    ([[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]], 2),
    ([[None], [None, None, None]], 2),
    ([['a', 'a', 'a'], ['a', 'a'], ['a', 'a', 'a', 'a'], ['a'], ['a', 'a', 'a', 'a', 'a', 'a']], 5)
)


class MyTestCase(unittest.TestCase):
    def test_all(self):
        for case in tests:
            inp, exp = case
            self.assertEqual(get_length_of_missing_array(inp), exp)


if __name__ == '__main__':
    unittest.main()
