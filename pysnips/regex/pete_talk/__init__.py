import re


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

    def pete_talk(self):
        """
        splits the string at these punctuation marks [".","!","?"]
        :returns hashed speech
        """
        speech, ok = self.speech, self.ok_words
        re.split(r'\.+|,+|!+|\?+', speech)
