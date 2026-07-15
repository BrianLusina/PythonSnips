# Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

## Examples

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

## Solution

This solution uses a variable-length sliding window to consider all substrings without repeating characters, and returns
the length of the longest one at the end.
We represent the state of the current window with a dictionary state which maps each character to the number of times it
appears in the window.

![Solution 1](./images/solutions/length_longest_substring_without_repeating_characters_solution_1.png)
![Solution 2](./images/solutions/length_longest_substring_without_repeating_characters_solution_2.png)

We use a for-loop to increment end to repeatedly expand the window. Each time we expand the window, we first increment
the count of s[end] in state. As long as the character at end is not a duplicate character in the window, we can compare
the length of the current window to the longest window we've seen so far, and continue expanding. The character at end
is a duplicate if state[s[end]] > 1.

![Solution 3](./images/solutions/length_longest_substring_without_repeating_characters_solution_3.png)
![Solution 4](./images/solutions/length_longest_substring_without_repeating_characters_solution_4.png)
![Solution 5](./images/solutions/length_longest_substring_without_repeating_characters_solution_5.png)
![Solution 6](./images/solutions/length_longest_substring_without_repeating_characters_solution_6.png)
![Solution 7](./images/solutions/length_longest_substring_without_repeating_characters_solution_7.png)
![Solution 8](./images/solutions/length_longest_substring_without_repeating_characters_solution_8.png)
![Solution 9](./images/solutions/length_longest_substring_without_repeating_characters_solution_9.png)

At this point, we have to contract the window because it contains more than one g. We do this by removing the leftmost
character (start += 1) from the window, and decrementing its count in state until there is only one g left in the window.

![Solution 10](./images/solutions/length_longest_substring_without_repeating_characters_solution_10.png)
![Solution 11](./images/solutions/length_longest_substring_without_repeating_characters_solution_11.png)

At this point, our window is valid again, and we can continue this process of expanding and contracting the window until
end reaches the end of the string.

![Solution 12](./images/solutions/length_longest_substring_without_repeating_characters_solution_12.png)
![Solution 13](./images/solutions/length_longest_substring_without_repeating_characters_solution_13.png)
![Solution 14](./images/solutions/length_longest_substring_without_repeating_characters_solution_14.png)
![Solution 15](./images/solutions/length_longest_substring_without_repeating_characters_solution_15.png)
![Solution 16](./images/solutions/length_longest_substring_without_repeating_characters_solution_16.png)
![Solution 17](./images/solutions/length_longest_substring_without_repeating_characters_solution_17.png)
![Solution 18](./images/solutions/length_longest_substring_without_repeating_characters_solution_18.png)
![Solution 19](./images/solutions/length_longest_substring_without_repeating_characters_solution_19.png)
![Solution 20](./images/solutions/length_longest_substring_without_repeating_characters_solution_20.png)
![Solution 21](./images/solutions/length_longest_substring_without_repeating_characters_solution_21.png)
![Solution 22](./images/solutions/length_longest_substring_without_repeating_characters_solution_22.png)
![Solution 23](./images/solutions/length_longest_substring_without_repeating_characters_solution_23.png)
![Solution 24](./images/solutions/length_longest_substring_without_repeating_characters_solution_24.png)
![Solution 25](./images/solutions/length_longest_substring_without_repeating_characters_solution_25.png)
