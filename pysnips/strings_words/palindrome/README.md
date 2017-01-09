## Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.
As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.
If the length of the input string is 0, return value must be 0.
Example:

"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0

## Palindrome Pairs

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Examples:
```python
["bat", "tab", "cat"] # [[0, 1], [1, 0]]
["dog", "cow", "tap", "god", "pat"] # [[0, 3], [2, 4], [3, 0], [4, 2]]
["abcd", "dcba", "lls", "s", "sssll"] # [[0, 1], [1, 0], [2, 4], [3, 2]]
```
Non-string inputs should be converted to strings.

Return an array of arrays containing pairs of distinct indices that form palindromes. Pairs should be reutrned in the order they appear in the original list.
