import unittest

from algorithms.arrays.remove_element import remove_element


class RemoveElementTestCase(unittest.TestCase):
    def test_3223_and_3(self):
        arr = [3, 2, 2, 3]
        val = 3
        actual = remove_element(arr, val)
        expected = 2
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
