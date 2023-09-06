import unittest

from . import interpolation_search


class InterpolationSearchTestCase(unittest.TestCase):
    def test_12_33_11_99_22_55_90_with_target_12(self):
        """should return 1 for a list of [11, 12, 22, 33, 55, 90, 99] with a target of 12"""
        collection = [11, 12, 22, 33, 55, 90, 99]
        target = 12
        expected = 1
        actual = interpolation_search(collection, target)

        self.assertEqual(expected, actual)

    def test_raises_exception_if_target_is_not_in_collection(self):
        """should raise exception if target is not in collection"""
        collection = [11, 12, 22, 33, 55, 90, 99]
        target = 1

        with self.assertRaises(Exception):
            interpolation_search(collection, target)

    def test_raises_exception_for_empty_collection_with_provided_target(self):
        """should raise exception if target is not in collection"""
        collection = []
        target = 1

        with self.assertRaises(Exception):
            interpolation_search(collection, target)


if __name__ == '__main__':
    unittest.main()
