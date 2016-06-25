# -*- coding: utf-8 -*-
"""
Find the length of the longest substring in the given string s that is the same in reverse.
As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.
If the length of the input string is 0, return value must be 0.
Example:

"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""
class Palindrome(object):
    def __init__(self,n):
        self.n = n

    @staticmethod
    def longest_palindrome(s):
        s,finalStr = s.lower(), ""
        isPalindrome = lambda s: s == s[::-1] #check if palindrome
        if s == "":
            return 0
        else:
            for y, item in enumerate(s):
                for x, item in enumerate(s):
                    testStr = s[y:x + 1]
                    if isPalindrome(testStr) and (len(testStr) > len(finalStr)):
                        finalStr = testStr

        return len(finalStr)

#function to test the function
def test(n, m):
    return n == m

print test(Palindrome.longest_palindrome("a"), 1)
print test(Palindrome.longest_palindrome("aa"), 2)
print test(Palindrome.longest_palindrome("baa"), 2)
print test(Palindrome.longest_palindrome("aab"), 2)
print test(Palindrome.longest_palindrome("abcdefghba"), 1)
print test(Palindrome.longest_palindrome("baablkj12345432133d"), 9)

print list(enumerate("baablkj12345432133d"))