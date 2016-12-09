"""
check to see that each character in the first string actually occurs in the second. If it is possible to “checkoff” each character, then the two strings must be anagrams. Checking off a character will be accomplished by replacing it with the special Python value None. However, since strings in Python are immutable, the first step in the process will be to convert the second string to a list. Each character from the first string can be checked against the characters in the list and if found, checked off by replacement.
"""


def detect_anagrams(word, word_list):
    res, word = [], word.lower()
    for x in word_list:
        if len(word) == len(x.lower()) and word != x.lower():
            if is_anagram(word, x.lower()):
                res.append(x)
    return res


def is_anagram(s1, s2):
    alist = list(s2)
    pos1 = 0
    flag = True

    while pos1 < len(s1) and flag:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            flag = False

        pos1 += 1

    return flag
