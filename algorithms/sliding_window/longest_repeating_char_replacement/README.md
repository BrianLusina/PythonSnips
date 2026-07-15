# Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Examples

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

## Solution

In order for a substring to be valid, k + the frequency of the most frequent character in the substring must be greater
than or equal to the length of the substring.

For example, if k = 2, and the substring is AABBB, then the most frequent character is B, which shows up 3 times. The
substring is valid because 2 + 3 >= 5.

![Solution Sample 1](./images/solutions/longest_repeating_char_replacement_solution_sample_1.png)

However, if k = 2 and the substring is AAABBB, then the substring is invalid because 2 + 3 < 6.

![Solution Sample 2](./images/solutions/longest_repeating_char_replacement_solution_sample_2.png)

We use this fact to solve this problem with a variable-length sliding window to iterate over all valid substrings, and
return the longest of those lengths at the end. To represent the state of the current window, we keep track of two
variables:

- `state`: A dictionary mapping each character to the number of times it appears in the current window.
- `max_freq`: The maximum number of times a single character has appeared in any window so far.

We start by extending the current window until it becomes invalid (i.e. `k` + `max_freq` < `window` length).

![Solution 1](./images/solutions/longest_repeating_char_replacement_solution_1.png)
![Solution 2](./images/solutions/longest_repeating_char_replacement_solution_2.png)
![Solution 3](./images/solutions/longest_repeating_char_replacement_solution_3.png)
![Solution 4](./images/solutions/longest_repeating_char_replacement_solution_4.png)
![Solution 5](./images/solutions/longest_repeating_char_replacement_solution_5.png)
![Solution 6](./images/solutions/longest_repeating_char_replacement_solution_6.png)
![Solution 7](./images/solutions/longest_repeating_char_replacement_solution_7.png)
![Solution 8](./images/solutions/longest_repeating_char_replacement_solution_8.png)
![Solution 9](./images/solutions/longest_repeating_char_replacement_solution_9.png)
![Solution 10](./images/solutions/longest_repeating_char_replacement_solution_10.png)
![Solution 11](./images/solutions/longest_repeating_char_replacement_solution_11.png)
![Solution 12](./images/solutions/longest_repeating_char_replacement_solution_12.png)
![Solution 13](./images/solutions/longest_repeating_char_replacement_solution_13.png)

At this point, the longest substring we have found so far is BCBAB, which has a length of 5 (max_freq = 3 + k = 2).
Now, whenever we try to extend the current window to length 6, it will be invalid unless the character we just included
in the window shows up 4 times. So each time we increase the window to length 6, we immediately shrink the window to
length 5 until we find a character which shows up 4 times.

![Solution 14](./images/solutions/longest_repeating_char_replacement_solution_14.png)
![Solution 15](./images/solutions/longest_repeating_char_replacement_solution_15.png)
![Solution 16](./images/solutions/longest_repeating_char_replacement_solution_16.png)
![Solution 17](./images/solutions/longest_repeating_char_replacement_solution_17.png)
![Solution 18](./images/solutions/longest_repeating_char_replacement_solution_18.png)
![Solution 19](./images/solutions/longest_repeating_char_replacement_solution_19.png)

This continues until we reach the end of the string, at which point we return the length of the longest substring we
have found so far.

![Solution 20](./images/solutions/longest_repeating_char_replacement_solution_20.png)
![Solution 21](./images/solutions/longest_repeating_char_replacement_solution_21.png)
![Solution 22](./images/solutions/longest_repeating_char_replacement_solution_22.png)
![Solution 23](./images/solutions/longest_repeating_char_replacement_solution_23.png)
