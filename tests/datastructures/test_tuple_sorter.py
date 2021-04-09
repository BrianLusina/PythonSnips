import unittest

from datastructures.tuples.tuple_sorter import sorter


class SorterTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual([('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)],
                         sorter(("Tom", 19, 80), ("John", 20, 90), ("Jony", 17, 91), ("Jony", 17, 93),
                                ("Json", 21, 85)))
