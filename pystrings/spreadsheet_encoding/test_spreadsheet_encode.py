import unittest
from . import spreadsheet_encode_column


class SpreadsheetEncodeColumnTestCases(unittest.TestCase):
    def test_zz(self):
        """ZZ should return 702"""
        column_name = "ZZ"
        expected = 702
        actual = spreadsheet_encode_column(column_name)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
