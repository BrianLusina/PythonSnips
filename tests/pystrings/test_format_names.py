import unittest

from pystrings.format_names import name_list


class FormatNamesTestCases(unittest.TestCase):
    def test_one_multiple_names(self):
        names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]
        actual = name_list(names)
        expected = 'Bart, Lisa, Maggie, Homer & Marge'

        self.assertEqual(expected, actual)

    def test_two_with_three_names(self):
        names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
        actual = name_list(names)
        expected = 'Bart, Lisa & Maggie'

        self.assertEqual(expected, actual)

    def test_adds_ampersand_with_two_names_only(self):
        names = [{'name': 'Bart'}, {'name': 'Lisa'}]
        actual = name_list(names)
        expected = 'Bart & Lisa'

        self.assertEqual(expected, actual)

    def test_properly_formats_one_name(self):
        names = [{'name': 'Bart'}]
        actual = name_list(names)
        expected = 'Bart'

        self.assertEqual(expected, actual)

    def test_returns_empty_string_when_list_is_empty(self):
        names = []
        actual = name_list(names)
        expected = ''

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
