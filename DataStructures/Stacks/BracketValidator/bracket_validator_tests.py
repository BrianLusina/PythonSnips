import unittest
from DataStructures.Stacks.BracketValidator.bracket_validator import count


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, count('((()))'))

    def test2(self):
        self.assertEqual(True, count('(()())'))

    def test3(self):
        self.assertEqual(False, count('((()'))

    def test4(self):
        self.assertEqual(False, count('())('))

if __name__ == '__main__':
    unittest.main()
