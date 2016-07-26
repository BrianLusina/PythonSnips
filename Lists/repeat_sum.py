import unittest
"""
pseudo code
create an empty list to store the unpacked lists
perform a for loop to iterate through the list of lists and another to unpack them into the concat lists
count the occurrences of each number in the concat and add to the counter list
sum the counter list
"""


def repeat_sum(list_lists):
    concat = []
    for x in list_lists:
        for i in set(x):
            concat.append(i)
    counter = set([y for y in concat if concat.count(y) >= 2])
    return sum(list(counter))


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]]), 10)

    def test2(self):
        self.assertEqual(repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]]), 0)

    def test3(self):
        self.assertEqual(repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]), 9)

    def test4(self):
        self.assertEqual(repeat_sum([[1]]), 0)