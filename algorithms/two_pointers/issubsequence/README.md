# Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "
abcde" while "aec" is not).

``` plain
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
```

## Related Topics

- Two Pointers
- String
- Dynamic Programming


### Solution

The key intuition behind this problem is that we can use two pointers to match characters of s in t from left to right.
We maintain a first pointer for string s and a second pointer for string t. As we scan through t, whenever the current
character in t matches the current character we're looking for in s, we advance the first pointer to look for the next
character. We always advance the second pointer regardless of a match. If by the end of the traversal the first pointer
has reached the end of s, it means every character in s was found in t in the correct relative order, so s is a
subsequence of t.

Now, let’s look at the solution steps below:

1. Initialize a pointer sPointer (pointing to the start of s) to 0
2. Initialize a pointer tPointer (pointing to the start of t) to 0
3. Iterate using a while loop as long as `pointer_s` is less than the length of s and `pointer_t` is less than the length
   of t.
   - If the character at `s[pointer_s]` equals the character at `t[pointer_t]`,
     - Increment `pointer_s` by 1
   - Regardless of whether there was a match, increment `pointer_t` by 1 to continue scanning through t.
4. After the loop terminates, check if sPointer equals the length of s. If it does, all characters of s have been
   matched in order within t, so return TRUE. Otherwise, return FALSE.

#### Complexity analysis

##### Time complexity

The time complexity of the solution is O(n) where n is the length of t. In the worst case, we traverse the entire string
t once with tPointer, performing a constant-time character comparison at each step.

##### Space complexity

The space complexity of the solution is O(1) because we only use two integer pointer variables (sPointer and tPointer)
regardless of the input size. No additional data structures are allocated.
