import unittest
import re


def pig_it(text):
    return " ".join(x.replace(x[0], "") + x[0] + "ay" for x in text.split(" ") if re.match('\w+', x))


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')

    def test_two(self):
        self.assertEqual(pig_it('This is my string'), 'hisTay siay ymay tringsay')


if __name__ == '__main__':
    unittest.main()
