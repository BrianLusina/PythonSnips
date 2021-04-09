import unittest

from pyregex.custom_username import email_parser


class CustomUsernameTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(email_parser(email="brian@gmail.com"), "<Username: 'brian'>, <Domain: 'gmail.com'>")
