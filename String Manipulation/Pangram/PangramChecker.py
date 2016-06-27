"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

Alternatively
is_pangram = lambdas: not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())
"""
import string
class Pangram:
    def __init__(self,s):
        self.s = s

    @staticmethod
    def is_pangram(s):
        return not set(string.lowercase) - set(s.lower())


print "TESTING FOR pangram(s) function"
print Pangram.is_pangram("The quick brown fox jumps over the lazy dog")

"""Longest Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, return value must be 0.

Example:

"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0"""
def longest_palindrome (s):
	if s == "":
		return 0
	else:
		newList = s.split()
		palindromeList = []
		for i in newList:
			length = len(i)
			if i[0:length] == i[::-1]:
				palindromeList = palindromeList.append()
				for n in palindromeList:
					len(n)