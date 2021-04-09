import unittest

from datastructures.dicts.word_frequency import frequency


class FreqTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual("2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1", frequency(
            "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."))


if __name__ == '__main__':
    unittest.main()
