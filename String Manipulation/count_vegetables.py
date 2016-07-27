from collections import Counter
import unittest

lst1 = [(2, 'tofu'),
        (2, 'potato'),
        (2, 'cucumber'),
        (2, 'cabbage'),
        (1, 'turnip'),
        (1, 'pepper'),
        (1, 'onion'),
        (1, 'mushroom'),
        (1, 'celery'),
        (1, 'carrot')]

s1 = 'potato tofu cucumber cabbage turnip pepper onion carrot celery mushroom potato tofu cucumber cabbage'

lst2 = [(15, 'turnip'),
        (15, 'mushroom'),
        (13, 'cabbage'),
        (10, 'carrot'),
        (9, 'potato'),
        (7, 'onion'),
        (6, 'tofu'),
        (6, 'pepper'),
        (5, 'cucumber'),
        (4, 'celery')]

s2 = "mushroom chopsticks chopsticks turnip mushroom carrot mushroom cabbage mushroom carrot tofu pepper cabbage potato cucumber mushroom mushroom mushroom potato turnip chopsticks cabbage celery celery turnip pepper chopsticks potato potato onion cabbage cucumber onion pepper onion cabbage potato tofu carrot cabbage cabbage turnip mushroom cabbage cabbage cucumber cabbage chopsticks turnip pepper onion pepper onion mushroom turnip carrot carrot tofu onion tofu chopsticks chopsticks chopsticks mushroom cucumber chopsticks carrot potato cabbage cabbage carrot mushroom chopsticks mushroom celery turnip onion carrot turnip cucumber carrot potato mushroom turnip mushroom cabbage tofu turnip turnip turnip mushroom tofu potato pepper turnip potato turnip celery carrot turnip"

lst3 = [(2,"potato"),(1,'tofu'),(2,'kales'),(1,'tomatoes'),(1,'celery'),(3,'cucumber')]
s3 = "potato potato tofu kales kales tomatoes celery cucumber cucumber cucumber"

"""
split string and use Counter object to count each string, convert them to a dictionary
for each Key value pare in dictionary, add to a list,
sort the list in descending order by count, then by alphabetical order by using sorted
return this list

"""


def count_vegetables(s):
    p = s.split()
    valid = ["cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"]
    m = set([(p.count(x), x) for x in p if x in valid])
    return sorted(m, key=lambda tup: (tup[0], tup[1]), reverse=True)


class Tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(count_vegetables(s1), lst1)

    def test2(self):
        self.assertEqual(count_vegetables(s2), (lst2))
"""
    def test3(self):
        self.assertEqual(count_vegetables(s3), lst3)
"""
