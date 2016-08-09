import re
import unittest


class PeteTalk(object):
    """
    Rules
    > start of each sentence has a capitalized word at the beginning.
    > take an additional parameter consisting of an array/list of allowed words which are not to be replaced.
    > any words longer than 2 characters need to have every character which is not the first or the last) changed into *
    > every uppercase letter not at the beginning of the string or coming after a punctuation mark among [".","!","?"]
    is lowered; spaces and other punctuation are ignored
    """
    def __init__(self, speech, ok_words=None):
        self.speech = speech
        self.ok_words = ok_words

    """
    splits the string at these punctuation marks [".","!","?"]
    :returns hashed speech
    """
    def pete_talk(self):
        speech, ok = self.speech, self.ok_words
        re.split(r'\.+|,+|!+|\?+', speech)


class Tests(unittest.TestCase):
    def test_desc(self):
        self.shortDescription()

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
