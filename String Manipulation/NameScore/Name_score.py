import unittest

alpha={'ABCDE':1,'FGHIJ':2,'KLMNO':3,'PQRST':4,'UVWXY':5}

def name_score(name):
    #your code here

class NameScoreTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(name_score('Mary Jane'), {"Mary Jane":20})

    def test2(self):
        self.assertEqual(name_score('Luke Skywalker'), {"Luke Skywalker":41})

    def test3(self):
        self.assertEqual(name_score('Zoe Andrews'), {"Zoe Andrews":23})

    def test4(self):
        self.assertEqual(name_score('Double  Space'), {"Double  Space":25})

    def test5(self):
        self.assertEqual(name_score('Greg Z MacDonald'), {"Greg Z MacDonald":26})