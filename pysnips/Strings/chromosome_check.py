import unittest


def chromosoneCheck(sperm):
    return "Congratulations! You're going to have a daughter." if sperm == "XX" else "Congratulations! You're going to have a son."


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(chromosoneCheck('XY'), 'Congratulations! You\'re going to have a son.')

    def test2(self):
        self.assertEqual(chromosoneCheck('XX'), 'Congratulations! You\'re going to have a daughter.')