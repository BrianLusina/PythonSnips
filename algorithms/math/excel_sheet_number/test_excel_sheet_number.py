import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.math.excel_sheet_number import (
    title_to_number,
)

EXCEL_SHEET_NUMBER_TEST_CASES = [
    ("A", 1),
    ("AB", 28),
    ("ZY", 701),
    ("AA", 27),
    ("Z", 26),
]


class ExcelSheetNumberTestCase(unittest.TestCase):
    @parameterized.expand(
        EXCEL_SHEET_NUMBER_TEST_CASES, name_func=custom_test_name_func
    )
    def test_excel_sheet_number(self, column_title: str, expected: int):
        actual = title_to_number(column_title)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
