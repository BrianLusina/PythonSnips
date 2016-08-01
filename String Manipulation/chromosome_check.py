import unittest

def chromosoneCheck(sperm):
    #Your code here

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(chromosoneCheck('XY'), 'Congratulations! You\'re going to have a son.')

    def test2(self):
        self.assertEqual(chromosoneCheck('XX'), 'Congratulations! You\'re going to have a daughter.')