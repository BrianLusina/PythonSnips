from collections import Counter
from . import is_palindrome


def longest_palindrome(s):
    s, final_str = s.lower(), ""
    if s == "":
        return 0
    else:
        for y, _ in enumerate(s):
            for x, _ in enumerate(s):
                tr = s[y: x + 1]
                if is_palindrome(tr) and (len(tr) > len(final_str)):
                    final_str = tr

    return len(final_str)


def longest_palindrome_one(s: str) -> int:
    """
    Finds the longest palindrome that can be formed from a given string. The string is case-sensitive so 'A' & 'a; are
    not the same.
    This uses a set() to determine if we have encountered a character in the string before, if we have, we increase the
    number of pairs count and remove that character from the set. If we have not encountered that character, we add it
    to the set.
    In the end we return the pairs count * 2 + 1 if we still have characters in the set, meaning they did not have any
    pairs or the pairs * 2 if there are no characters left in the set

    Complexity:
    Time Complexity: O(n) where n is the number of characters in the string, as we have to iterate through each char
    Space Complexity: O(n) as we are using a set to store the characters that we have encountered in the string before

    >>> longest_palindrome_one('a')
    1
    >>> longest_palindrome_one("abccccdd")
    7
    @param s: alphabetic string
    @return: length of the longest palindrome that can be formed from the string
    @rtype: int
    """
    pairs, unpaired_chars = 0, set()

    if len(s) == 1:
        return 1

    for char in s:
        if char in unpaired_chars:
            pairs += 1
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)

    return pairs * 2 + 1 if unpaired_chars else pairs * 2


def longest_palindrome_two(s: str) -> int:
    """
    Finds the longest palindrome that can be formed from a given string. The string is case-sensitive so 'A' & 'a; are
    not the same.
    Intuition:
    A palindrome consists of letters with equal partners, plus possibly a unique center (without a partner). The letter
    i from the left has its partner i from the right. For example in 'abcba', 'aa' and 'bb' are partners, and 'c' is a
    unique center.

    Imagine we built our palindrome. It consists of as many partnered letters as possible, plus a unique center if
    possible. This motivates a greedy approach.

    Algorithm:

    For each letter, say it occurs v times. We know we have v // 2 * 2 letters that can be partnered for sure.
    For example, if we have 'aaaaa', then we could have 'aaaa' partnered, which is 5 // 2 * 2 = 4 letters partnered.

    At the end, if there was any v % 2 == 1, then that letter could have been a unique center. Otherwise, every letter
    was partnered. To perform this check, we will check for v % 2 == 1 and ans % 2 == 0, the latter meaning we haven't
    yet added a unique center to the answer.

    Complexity Analysis

    Time Complexity: O(N), where N is the length of s. We need to count each letter.
    Space Complexity: O(1), the space for our count, as the alphabet size of s is fixed. We should also consider that
    in a bit complexity model, technically we need O(logN) bits to store the count values.

    @param s: alphabetic string
    @return: length of the longest palindrome that can be formed from the string
    @rtype: int
    """
    ans = 0
    if len(s) == 1:
        return 1

    for v in Counter(s).values():
        ans += v // 2 * 2
        if ans % 2 == 0 and v % 2 == 1:
            ans += 1

    return ans
