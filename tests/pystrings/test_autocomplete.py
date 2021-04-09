import unittest

from pystrings.auto_complete import autocomplete

dictionary = ['abnormal',
              'arm-wrestling',
              'absolute',
              'airplane',
              'airport',
              'amazing',
              'apple',
              'ball']


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(autocomplete('ai', dictionary), ['airplane', 'airport'])

    def test_2(self):
        self.assertEqual(autocomplete('a', dictionary),
                         ['abnormal', 'arm-wrestling', 'absolute', 'airplane', 'airport'])


if __name__ == '__main__':
    unittest.main()
