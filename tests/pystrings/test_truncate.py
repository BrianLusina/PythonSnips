import unittest

from pystrings.truncate_string import truncate_string


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(truncate_string("pippi", 3), "pip...")

    def test_2(self):
        self.assertEqual(truncate_string("Peter Piper picked a peck of pickled peppers", 14), "Peter Piper...")

    def test_3(self):
        self.assertEqual(truncate_string("A-tisket a-tasket A green and yellow basket", 11), "A-tisket...")

    def test_4(self):
        self.assertEqual(truncate_string("A-tisket a-tasket A green and yellow basket", 43),
                         "A-tisket a-tasket A green and yellow basket")

    def test_5(self):
        self.assertEqual(truncate_string("A-tisket a-tasket A green and yellow basket", 45),
                         "A-tisket a-tasket A green and yellow basket")

    def test_6(self):
        self.assertEqual(truncate_string("A-", 1), "A...")

    def test_7(self):
        self.assertEqual(truncate_string("Absolutely Longer", 2), "Ab...")

    def test_8(self):
        self.assertEqual(truncate_string("Chingel loves his Angel so much!!!", 27), "Chingel loves his Angel ...")

    def test_9(self):
        self.assertEqual(truncate_string("I like ice-cream.Do you?", 19), "I like ice-cream...")

    def test_10(self):
        self.assertEqual(truncate_string("Seems like you have passed the final test. Congratulations", 53),
                         "Seems like you have passed the final test. Congrat...")


if __name__ == '__main__':
    unittest.main()
