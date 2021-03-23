import re
from string import punctuation


# todo: check on this pete talk function
class PeteTalk(object):
    """
    Rules
    > start of each sentence has a capitalized word at the beginning.
    > take an additional parameter consisting of an array/list of allowed words which are not to be replaced.
    > any words longer than 2 characters need to have every character which is not the first or the last) changed
    into *
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
        :rtype: str
        """
        speech_words, ok = self.speech.split(" "), self.ok_words
        result = []

        # if ok words is not none
        if ok is not None:
            for word in speech_words:
                if word not in ok and len(word) > 2:
                    middle = word[1: len(word) - 1]
                    word = re.sub(middle, "*" * len(middle), word)
        else:
            # split the string into words, loop through each word checking if it is longer than length of 2
            # and not in ok_words then hash the middle characters
            for word in speech_words:

                # check if the word is a word with no trailing punctuation marks
                # and has a length greater than 2
                if re.match(r"([a-zA-z]+)", word) and len(word) > 2:
                    # get the middle section, exclude the punctuation mark
                    # checks if the word ends with a punctuation mark and gets the middle section accordingly
                    if word.endswith(tuple(punctuation)):
                        middle = word[1: len(word) - 2]
                    else:
                        middle = word[1: len(word) - 1]
                    word = re.sub(middle, "*" * len(middle), word)
                    result.append(word.lower())
                else:
                    result.append(word.lower())

        # final_result = ""
        # # split the result at punctuation marks and capitalize each section
        # # for sentence in re.split("\?|!|\.", " ".join(result)):
        # #     final_result += sentence.capitalize()
        # # return final_result

        return " ".join(result).capitalize()


pete = PeteTalk("What the hell am I doing here? And where is my wallet? PETE SMASH!")
print(pete.pete_talk(), "W**t t*e h**l am i d***g h**e? A*d w***e is my w****t? P**e s***h!")
