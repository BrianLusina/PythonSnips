# Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k
times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed,
etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those
repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

```plain
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Related Topics

- String
- Stack
- Recursion

## Solution

The essence of this approach lies in recognizing that the problem is naturally suited for a stack-based solution. When
decoding a string, we need to handle nested and sequential patterns, and a stack allows us to manage these layers
effectively. By pushing and popping elements on the stack as we encounter brackets, we can keep track of the substrings
and their repeat counts. This method ensures we decode the string from the innermost nested structure outward,
maintaining the correct order and repetition. To achieve this, we process each character in the string in the following
way:

- **Digits**: Represent how many times a substring is repeated.
- **Open bracket ([)**: Marks the start of a new substring and saves the current state by pushing the current substring
  and repeat count onto stacks and then resetting them for a new segment.
- **Close bracket (])**: Ends the current substring, repeats it as specified, and appends it to the previous substring.
- **Letters**: Build the current substring being processed.

This solution handles nested and consecutive encoding strings by utilizing the stack to track previously processed
substrings and their associated repeat counts. The final decoded string is constructed by combining all parts accumulated
in the stacks.

Here’s the step-by-step implementation of the solution:

- Initialize two empty stacks: count_stack for storing repeat counts and string_stack for storing intermediate strings.
- Initialize current as an empty string. This will hold the currently decoded string segment.
- Initialize k as 0: This will store multi-digit numbers representing repeat counts.
- Iterate through each character char in the input string s:
  - If char is a digit:
    - Update k to accumulate the digit into a multi-digit number by performing k = 10 * k + int(char).
  - If char is a '[':
    - Push k onto count_stack to save the current repeat count. 
    - Push current onto string_stack to save the current string segment. 
    - Reset k to 0 for the next repeat count. 
    - Reset current to an empty string to start decoding the new segment.
  - If char is a’]’:
    - Pop the last string segment from string_stack and store it in decoded_string. 
    - Pop the last repeat count from count_stack and store it in num. 
    - Update current by appending current * num to decoded_string, repeating the decoded segment, and combining it with
      the previous string.
  - If char is a regular character:
    - Append char to current, adding it to the currently decoded string segment.
- After processing all characters, current will contain the fully decoded string.

### Time Complexity

The time complexity of this solution is O(n∗m∗k), where n is the length of the input string, m is the length of current,
and k is the maximum multiplier encountered during the decoding.

### Space Complexity

The space complexity of this solution is O(c+d), where c is the number of alphabets and d is the number of digits in the
input string.
