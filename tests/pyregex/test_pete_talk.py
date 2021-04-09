import unittest

from pyregex.pete_talk import PeteTalk


@unittest.skip
class PeteTalkTestCases(unittest.TestCase):
    def shortDescription(self):
        return "{} test cases.".format(PeteTalk.__name__)

    def test_1(self):
        pete = PeteTalk("I want to punch someone in the face")
        self.assertEqual(pete.pete_talk(), "I w**t to p***h s*****e in t*e f**e")

    def test_2(self):
        pete = PeteTalk("uh!")
        self.assertEqual(pete.pete_talk(), "Uh!")

    def test_3(self):
        pete = PeteTalk("What the hell am I doing here? And where is my wallet? PETE SMASH!")
        self.assertEqual(pete.pete_talk(), "W**t t*e h**l am i d***g h**e? A*d w***e is my w****t? P**e s***h!")

    def test_4(self):
        pete = PeteTalk("I want to punch someone in the face", ["someone", "face"])
        self.assertEqual(pete.pete_talk(), "I w**t to p***h someone in t*e face")

    def test_5(self):
        pete = PeteTalk("I want to punch someone in the face", ["drink", "job", "girls"])
        self.assertEqual(pete.pete_talk(), "I w**t to p***h s*****e in t*e f**e")
