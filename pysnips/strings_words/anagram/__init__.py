from string import ascii_letters


class Anagrams(object):
    def __init__(self):
        pass

    def detect_anagrams(self, word, word_list):
        """check to see that each character in the first string actually occurs in the second. If it is possible to
        “checkoff” each character, then the two strings must be anagrams.
        Checking off a character will be accomplished by replacing it with the special Python value None.
        However, since strings in Python are immutable, the first step in
        the process will be to convert the second string to a list.
        Each character from the first string can be checked against the characters in the list and if found,
        checked off by replacement. """
        res, word = [], word.lower()
        for x in word_list:
            if len(word) == len(x.lower()) and word != x.lower():
                if self.is_anagram(word, x.lower()):
                    res.append(x)
        return res

    def is_anagram(self, s1, s2):
        a_list = list(s2)
        pos1 = 0
        flag = True

        while pos1 < len(s1) and flag:
            pos2 = 0
            found = False
            while pos2 < len(a_list) and not found:
                if s1[pos1] == a_list[pos2]:
                    found = True
                else:
                    pos2 += 1

            if found:
                a_list[pos2] = None
            else:
                flag = False

            pos1 += 1

        return flag

    def anagram_count(self, parent: str, child: str) -> int:
        """
        Counts the number of times the anagram of a child string appears in a parent string
        :return:  Number of times a child anagram string appears in a parent string
        :rtype int
        """

        pass
