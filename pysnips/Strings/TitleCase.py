import unittest


def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join(word if word in minor_words else word.capitalize() for word in title)


class TitleTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual('A Clash of Kings', title_case('a clash of KINGS', 'a an the of'))

    def test_2(self):
        self.assertEqual('The Wind in the Willows', title_case('THE WIND IN THE WILLOWS', 'The In'))

    def test_3(self):
        self.assertEqual('The Quick Brown Fox', title_case('the quick brown fox'))
