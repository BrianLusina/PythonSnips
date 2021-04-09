import unittest

from pyregex.password_validation import password_validation


class PassTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual("ABd1234@1", password_validation("ABd1234@1,a F1#,2w3E*,2We3345"))
