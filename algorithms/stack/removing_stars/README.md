# Removing Starts From a String

You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

```plain
Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:

- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
  There are no more stars, so we return "lecoe".
  Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
```

## Solutions

### Approach 1: Stack

To solve the problem, we must keep track of the most recently seen non-star character while iterating from the beginning
to the end of the string. Our task should be easy if we are able to use a data structure or write an algorithm that
keeps track of the most recent non-star character, which when removed gives the second most recent non-star character,
which when removed gives the third most recent non-star character, and so on.

There are several approaches to solving such a problem, one of which is to use a stack data structure.

We iterate through the given string s from the start. We check the character at every index i of s. If s[i] is a
non-star character, we push it into the stack. Otherwise, if s[i] is a star character, we pop the character from the
stack because the character at the top of the stack is the most recently seen non-star character from the characters
that have been seen up to this point and are not removed.

When we've finished iterating over the string, the stack will contain the required string in reverse order. We pop all
of the characters from the stack to form a string and then return the reverse of that string as our answer.

### Algorithm

1. Initialize a stack of characters `stack`.
2. Iterate over the string s from the start and for each index i of the string:
    1. If s[i] == '*', we perform the pop operation to remove the top character from the stack.
    2. Otherwise, we have a non-star character, so we push it into the stack.
3. Create an empty string variable answer.
4. While the stack is not empty:
    - Append the top character of the stack to answer and remove it from the stack.
5. Return the reverse of answer.

### Complexity Analysis:

Here,`n` is the length of `s`

- Time complexity: `O(n)`
    - We iterate over `s` and for every character we either push it in the stack or pop the top character from the stack
      which takes `O(1)` time per character. It takes `O(n)` time for `n` characters.
    - To form the answer string, we remove all the characters from the stack. Because a stack can have maximum of `n`
      characters, it would also take `O(n)` time in that case.
    - We also require `O(n)` time to reverse answer which can have `n` characters.
- Space complexity: `O(n)`
    - The stack used in the solution can grow to a maximum size of `n`. We would need `O(n)` space for that case.

## Related Topics

- String
- Stack
- Simulation
