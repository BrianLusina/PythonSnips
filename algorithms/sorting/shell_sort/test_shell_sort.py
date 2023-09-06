from unittest import TestCase, main

from . import shell_sort


class ShellSortTestCase(TestCase):
    def test_1(self):
        """should sort a list of [26, 17, 20, 11, 23, 21, 13, 18, 24, 14, 12, 22, 16, 15, 19, 25]"""
        collection = [26, 17, 20, 11, 23, 21, 13, 18, 24, 14, 12, 22, 16, 15, 19, 25]
        expected = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        actual = shell_sort(collection=collection)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
