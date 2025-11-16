# Find Longest Self-Contained Substring

You are given a string, s, consisting of lowercase English letters. Your task is to find the length of the longest 
self-contained substring of s.

A substring t of s is called self-contained if:
- t is not equal to the entire string s.
- Every character in t does not appear anywhere else in s (outside of t).

In other words, all characters in t are completely unique to that substring within the string s.
Return the length of the longest self-contained substring. If no such substring exists, return -1.

Constraints:

- 2 ≤ s.length ≤ 1000
- s consists only of lowercase English letters.

## Examples

![Example 1](./images/longest_self_contained_substring_example_1.png)
![Example 2](./images/longest_self_contained_substring_example_2.png)
![Example 3](./images/longest_self_contained_substring_example_3.png)
![Example 4](./images/longest_self_contained_substring_example_4.png)
![Example 5](./images/longest_self_contained_substring_example_5.png)
![Example 6](./images/longest_self_contained_substring_example_6.png)
![Example 7](./images/longest_self_contained_substring_example_7.png)
![Example 8](./images/longest_self_contained_substring_example_8.png)

---

## Solution

We iterate through the string once to record where each character first appears and where it last appears. Two separate 
hash maps store each character’s first and last occurrence indices. Each unique character serves as a potential starting 
point, defining an initial window from its first to last occurrence. The window is adjusted based on the following 
conditions:

- As we iterate within this window, if we encounter a character whose last occurrence is further to the right than the 
current window’s end, we expand the window to include it. This ensures that the substring remains self-contained, 
meaning all occurrences of each character within it are included. The process continues until no more characters 
extend the window’s boundary. 

- As we expand the window, every character inside it must have its first occurrence within the current window’s start 
boundary. If we encounter a character whose first occurrence index is before the current window’s starting position, 
it means that an earlier part of the string contains an instance of that character, violating the self-contained 
property. When this happens, the current substring is invalid, and we discard it from consideration. 

The maximum valid window length is tracked and updated accordingly, ensuring the longest valid substring is returned.

The steps of the algorithm are as follows:

1. Create two hashmaps, first, and last, to store the first and last occurrence index of each character in the string. 
2. Iterate through the string once to populate these hash maps with each character’s first and last occurrence. 
3. Initialize max_len = -1 to keep track of the maximum length of a valid self-contained substring found. 
4. For each unique character c1 (processed once), start from its first occurrence index:

   - Initialize the start and end of the window by setting the starting point to the character’s first occurrence and the 
   ending point to its last occurrence in the string.

   - Iterate through the string from the starting position start, extending the endpoint end whenever a character’s last 
   occurrence is beyond the current endpoint end.

   - If a character c2 inside the window has its first occurrence before the window's start, the window is invalid.

5. Validate the substring:

   - When the current index j reaches the end, check if the window is valid and its length is less than the total string 
   length.

   - If the window is valid, update max_len with the maximum of its current value and the window’s length (end - start + 1).

6. After checking all potential starting characters, return the maximum valid length found. If no valid substring exists, 
return -1.

Let’s look at the illustration below to better understand the solution.

![Solution 1](./images/solution/longest_self_contained_substring_solution_1.png)
![Solution 2](./images/solution/longest_self_contained_substring_solution_2.png)
![Solution 3](./images/solution/longest_self_contained_substring_solution_3.png)
![Solution 4](./images/solution/longest_self_contained_substring_solution_4.png)
![Solution 5](./images/solution/longest_self_contained_substring_solution_5.png)
![Solution 6](./images/solution/longest_self_contained_substring_solution_6.png)
![Solution 7](./images/solution/longest_self_contained_substring_solution_7.png)
![Solution 8](./images/solution/longest_self_contained_substring_solution_8.png)
![Solution 9](./images/solution/longest_self_contained_substring_solution_9.png)
![Solution 10](./images/solution/longest_self_contained_substring_solution_10.png)
![Solution 11](./images/solution/longest_self_contained_substring_solution_11.png)
![Solution 12](./images/solution/longest_self_contained_substring_solution_12.png)
![Solution 13](./images/solution/longest_self_contained_substring_solution_13.png)
![Solution 14](./images/solution/longest_self_contained_substring_solution_14.png)
![Solution 15](./images/solution/longest_self_contained_substring_solution_15.png)
![Solution 16](./images/solution/longest_self_contained_substring_solution_16.png)
![Solution 17](./images/solution/longest_self_contained_substring_solution_17.png)
![Solution 18](./images/solution/longest_self_contained_substring_solution_18.png)
![Solution 19](./images/solution/longest_self_contained_substring_solution_19.png)
![Solution 20](./images/solution/longest_self_contained_substring_solution_20.png)
![Solution 21](./images/solution/longest_self_contained_substring_solution_21.png)
![Solution 22](./images/solution/longest_self_contained_substring_solution_22.png)
![Solution 23](./images/solution/longest_self_contained_substring_solution_23.png)
![Solution 24](./images/solution/longest_self_contained_substring_solution_24.png)
![Solution 25](./images/solution/longest_self_contained_substring_solution_25.png)
![Solution 26](./images/solution/longest_self_contained_substring_solution_26.png)
![Solution 27](./images/solution/longest_self_contained_substring_solution_27.png)
![Solution 28](./images/solution/longest_self_contained_substring_solution_28.png)

### Time Complexity

The time complexity of the above solution is O(n), where n is the number of characters in the string.

### Space Complexity

The space complexity of the above solution is O(1) because of the fixed character set size, 26 lowercase English letters.