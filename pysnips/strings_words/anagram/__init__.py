from string import ascii_letters
from math_numbers.is_prime import is_prime
from functools import reduce


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
        Obtains the length of the child string and slices the parent string by that length,
        checks if the slices are anagrams and increases the count variable.
        If the child string is longer than parent, string, it returns a 0 automatically
        :return:  Number of times a child anagram string appears in a parent string
        :rtype int
        """
        count = 0
        child_slice = len(child)
        anagram = self.hash_string(child)

        if len(child) > len(parent):
            return 0
        if child == parent:
            return 1
        for i in range(0, len(parent) - child_slice):
            
            if self.hash_string(parent[i: i + child_slice]) == anagram:
                count += 1
        return count

    def hash_string(self, word):
        """
        Map ascii letters to prime numbers, then hashes the string
        :return: The character map for each letter to corresponding prime number
        :rtype int
        """
        # prime number length will depend on ascii_letters length
        char_map = {}
        count = 0
        for num in range(2, (ord(ascii_letters[25]) * 2)):
            # check if prime
            if is_prime(num):
                if len(char_map) == 52:
                    break
                char_map[ascii_letters[count]] = num
                count += 1
        return reduce(lambda memo, char: memo * char_map[char], word, 1)
