import unittest

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

"""
Split the string into a list,
loop through the list, then loop through each word checking if any letter is capital
if so, obtain the index of the word insert it at the beginning and remove it from old position
"""


def re_ordering(s):
    k, reorder = s.split(), ""
    for x in k:
        for y in x:
            if y.isupper():
                ind = k.index(x)
                k.insert(0, k.pop(ind))
    return " ".join(k)


class Test(unittest.TestCase):
    def test1(self):
        for input_str, result in BASIC_TESTS:
            self.assertEquals(result, re_ordering(input_str))