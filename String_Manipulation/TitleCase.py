import unittest


def title_case(title, minor_words=None):
    t, m = title.title(), []
    if minor_words:
        return t
    else:
        c = 0
        while c < len(t.split()[1:]):
            e = [i.title() for i in minor_words.split()]
            m.append(t.replace(i.title(), i.lower()) for i in e if i in t.split()[1:])
            c += 1
    return "".join(m)


class TitleTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')

    def test_2(self):
        self.assertEqual(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')

    def test_3(self):
        self.assertEqual(title_case('the quick brown fox'), 'The Quick Brown Fox')
