# Palindrome

Find the length of the longest substring in the given string s that is the same in reverse. As an example, if the input
was “I like racecars that go fast”, the substring (racecar) length would be 7. If the length of the input string is 0,
return value must be 0. Example:

"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0

## Palindrome Pairs

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list so that the concatenation of
the two words, i.e. words[i] + words[j] is a palindrome.

Examples:

```plain
["bat", "tab", "cat"]  # [[0, 1], [1, 0]]
["dog", "cow", "tap", "god", "pat"]  # [[0, 3], [2, 4], [3, 0], [4, 2]]
["abcd", "dcba", "lls", "s", "sssll"]  # [[0, 1], [1, 0], [2, 4], [3, 2]]
```

Non-string inputs should be converted to strings.

Return an array of arrays containing pairs of distinct indices that form palindromes. Pairs should be reutrned in the
order they appear in the original list.

## Palindrome Products

Write a program that can detect palindrome products in a given range.

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 x 99.

### Source

Problem 4 at Project Euler [http://projecteuler.net/problem=4](http://projecteuler.net/problem=4)

## Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can
be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

## Palindrome Index

Given a string of lowercase letters in the range ascii[a-z], determine a character that can be removed to make the
string a palindrome. There may be more than one solution, but any will do. For example, if your string is "bcbc", you
can either remove 'b' at index or 'c' at index . If the word is already a palindrome or there is no solution, return -1.
Otherwise, return the index of a character to remove.

Sample Input:

```plain
aaab
baa
aaa
```

Sample Output:

```plain
3
0
-1
```

Explanation:

```plain
Explanation

Query 1: "aaab"
Removing 'b' at index  results in a palindrome, so we print  on a new line.

Query 2: "baa"
Removing 'b' at index  results in a palindrome, so we print  on a new line.

Query 3: "aaa"
This string is already a palindrome, so we print . Removing any one of the characters would result in a palindrome, but this test comes first.
```

---

## Longest Palindromic Substring

Problem Description

Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:

A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).

Input Format
First and only argument is a string A.

Output Format
Return a string denoting the longest palindromic substring of string A.

Example Input
A = "aaaabaaa"

Example Output
"aaabaaa"

Example Explanation
We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".

### Related Topics

- String
- Dynamic Programming
