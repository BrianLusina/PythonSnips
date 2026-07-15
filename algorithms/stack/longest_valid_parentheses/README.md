# Longest Valid Parentheses

You are given a string composed entirely of ‘(’ and ‘)’ characters. Your goal is to identify the longest contiguous segment (substring) within this string that represents a “well-formed” or “valid” sequence of parentheses.

A substring is considered valid if:

1. Every opening parenthesis ‘(’ has a corresponding closing parenthesis ‘)’. 
2. The pairs of parentheses are correctly nested.

Return the length of this longest valid substring.

## Constraints

- 0 <= s.length <= 3 * 10^4
- s[i] is '(', or ')'.

## Examples

Example 1:
```text
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
```

Example 2:
```text
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
```

Example 3:
```text
Input: s = ""
Output: 0
```

## Topics

- String
- Dynamic Programming
- Stack

## Solution

The problem asks for the length of the longest valid (well-formed) parenthesis substring. This type of matching problem,
where you need to pair opening brackets with their corresponding closing brackets, is a classic example of a problem that
lends itself to a stack pattern. The stack’s last in, first out (LIFO) property naturally models the nesting structure of
parentheses: the last opening parenthesis must be the first one to be closed.

The essence of this algorithm is to use the stack to keep track of the indexes of parentheses that have not yet been
matched. Instead of just pushing the characters themselves, pushing their indexes allows us to calculate lengths. The
stack maintains a “base” index at the bottom, which marks the start of a potential valid substring. When a closing
parenthesis, ‘)’, finds a matching opening parenthesis, ‘(’, (by popping its index from the stack), the length of the
newly formed valid substring is calculated as the difference between the current index and the new top of the stack.

The following steps can be performed to implement the algorithm above:

1. Initialize a stack, indexStack, and push an initial index of -1. This value acts as a sentinel or a “base” for the
   first potential valid substring.
2. Next, iterate over the input string from the current index to the right (length of the input string), character by
   character.
   - **Opening parenthesis (**: If we encounter an opening parenthesis, we push its index onto the stack.
   - **Closing parenthesis )**: If we encounter a closing parenthesis:
     - We pop the top element from the indexStack.
     - If the stack becomes empty after popping, it means the current ‘)’ does not have a matching ‘(’. In this case, we
       push the current ‘)’s index onto the stack to serve as the new “base” for any future valid substrings.
     - Otherwise, if the stack is not empty, this means a valid pair has been formed. The length of this valid substring
       is the difference between the currentIndex and the index at the new top of the stack (which is the index right
       before the start of this valid pair). Compare this length with the maximum length, currentLength, found so far,
       and update it if necessary.
3. After the iteration ends, the maximum length, as recorded using max(maxLength, currentLength), is the answer.

### Time Complexity

The solution involves a single pass through the input string s. The loop runs exactly n times, where n is the length of
the string, and inside the loop, all operations (push, pop, top on the stack) take constant time, i.e., O(1). Therefore,
the total time complexity is dominated by the loop, resulting in O(n).

### Space Complexity

In the worst-case scenario, the input string, s, may consist entirely of opening parenthesis (e.g., “((((...”). In this
case, the index of every character will be pushed onto the stack, where the size of the stack can grow up to n, where n
is the length of the string. Therefore, the space complexity is O(n).
