import unittest
from data_structures.stacks.bracket_validator import count, is_valid


class BracketsTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, is_valid('((()))'))

    def test2(self):
        self.assertEqual(True, is_valid('(()())'))

    def test3(self):
        self.assertEqual(False, is_valid('((()'))

    def test4(self):
        self.assertEqual(False, is_valid('())('))

if __name__ == '__main__':
    unittest.main()
