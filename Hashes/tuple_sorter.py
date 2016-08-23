from operator import itemgetter, attrgetter
import unittest

"""
We use itemgetter to enable multiple sort keys.
"""


def sorter(*params):
    return sorted(params, key=itemgetter(0, 1, 2))


class SorterTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual([('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)], sorter(("Tom", 19, 80), ("John", 20, 90), ("Jony", 17, 91), ("Jony", 17, 93), ("Json", 21, 85)))



