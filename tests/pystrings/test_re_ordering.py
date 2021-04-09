import unittest

from pystrings.re_ordering import re_ordering

BASIC_TESTS = [
    ('ming Yao', 'Yao ming'),
    ('Mano donowana', 'Mano donowana'),
    ('wario LoBan hello', 'LoBan wario hello'),
    ('bull color pig Patrick', 'Patrick bull color pig'),
    ('jojo ddjajdiojdwo ana G nnibiial', 'G jojo ddjajdiojdwo ana nnibiial'),
    ('is one of those rare names that s both exotic and simple Adira',
     'Adira is one of those rare names that s both exotic and simple'),
    ('is an older name than annabel Amabel and a lot more distinctive',
     'Amabel is an older name than annabel and a lot more distinctive')
]


class Test(unittest.TestCase):
    def test1(self):
        for input_str, result in BASIC_TESTS:
            self.assertEquals(result, re_ordering(input_str))
