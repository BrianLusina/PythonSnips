from typing import Dict
from functools import reduce
from string import ascii_letters

from pymath.primes.is_prime import is_prime_with_re


def is_anagram(s1: str, s2: str) -> bool:
    """
    Check if s1 is an anagram of s2.
    Args:
        s1 (str): first string to check
        s2 (str): second string to check
    Return:
        bool: Whether the strings are anagrams of each other. If they are True is returned, False otherwise
    """
    # first normalize the strings by removing white spaces which might result in uneven lengths if s1 and s2 are anagrams
    # of each other
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # check the length of the strings. If the strings are not of the same length, then it's not possible for them to be
    # anagrams of each other
    if len(s1) != len(s2):
        return False

    # This dictionary is used to keep track of the character count in the strings to check if the strings are anagrams
    # of each other, the character count must be equal in both strings. This enables the algorithm to keep track of this
    # count.
    ht: Dict[str, int] = dict()

    # Loop through each character in the first string to count the number of characters and store them in the dictionary
    # this is linear, so, O(n) where n is the number of characters in the string as the loop has to iterate over each
    # character
    for char in s1:
        if char in ht:
            ht[char] += 1
        else:
            ht[char] = 1

    # Loops through each character in the second string checking for the existence of that character in the already
    # populated dictionary. If a character, exists, the count is decremented, if not, the count is incremented. This
    # will be used to show the discrepancy in character count between the two strings
    for char in s2:
        if char in ht:
            ht[char] -= 1
        else:
            ht[char] = 1

    # Finally, check each key in the dictionary. If a given key's count is not equal to 0, then the algorithm exits
    # early as it's not possible to have a character count of more than 0 for strings that are anagrams, since the above
    # loop should have reduced the character count to 0. This shows a discrepancy, meaning there is an extra character
    # in a string that is not in another string
    for key in ht:
        if ht[key] != 0:
            return False

    # return true if all the checks above check out.
    return True


class Anagrams:
    """
    Anagram class to detect anagrams for letters
    """

    def __init__(self):
        pass

    def detect_anagrams(self, word, word_list):
        """
        check to see that each character in the first string actually occurs in the second. If it is possible to
        “checkoff” each character, then the two strings must be anagrams.
        Checking off a character will be accomplished by replacing it with the special Python value None.
        However, since strings in Python are immutable, the first step in
        the process will be to convert the second string to a list.
        Each character from the first string can be checked against the characters in the list and if found,
        checked off by replacement."""
        res, word = [], word.lower()
        for x in word_list:
            if len(word) == len(x.lower()) and word != x.lower():
                if is_anagram(word, x.lower()):
                    res.append(x)
        return res

    def anagram_count(self, parent, child):
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

        # if the child is longer than the parent, return 0, it does not make sense for child to be > than parent
        if len(child) > len(parent):
            return 0

        # if the child and the parent are exactly the same, return 1
        if child == parent:
            return 1

        # if the child's length is the same as the parent length AND the child and parent are not the same
        # check if it is an anagram
        if len(child) == len(parent) and child != parent:
            if is_anagram(child, parent):
                return 1
            else:
                return 0
        for i in range(0, len(parent) - child_slice):
            if self.hash_string(parent[i : i + child_slice]) == anagram:
                count += 1
        return count

    def hash_string(self, word):
        """
        Map ascii letters to prime numbers, then hashes the string
        This is used to check if a parent string has an anagram of a child string.
        Used because hashes will remain unique and will be easier to check against
        :return: The character map for each letter to corresponding prime number
        :rtype int
        """
        # prime number length will depend on ascii_letters length
        char_map = {}
        char_map_zip = zip(ascii_letters, self.generate_primes(len(ascii_letters)))
        for let, prime in char_map_zip:
            char_map[let] = prime
        return reduce(lambda memo, char: memo * char_map[char], word, 1)

    @staticmethod
    def generate_primes(length):
        """
        Generates the prime numbers based on the length of the ascii characters
        :param length, Length of the ascii letters list, which is the length of the prime numbers wanted
        :return: list of prime numbers
        :rtype: list
        """
        # upper bound of search space
        upper_bound = 100
        # result list
        primes = list()

        while len(primes) < length:
            primes += filter(is_prime_with_re, range(upper_bound - 100, upper_bound))
            upper_bound += 100

        return primes[:length]
