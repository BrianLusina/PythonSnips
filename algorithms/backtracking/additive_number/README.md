# Additive Number

An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent
number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

> Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

## Examples

Example 1:
```text
Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
```

Example 2:
```text
Input: "199100199"
Output: true
Explanation: 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199
```

## Constraints

- 1 <= num.length <= 35
- num consists only of digits.

## Topics

- String
- Backtracking

## Solution

The key intuition behind this problem is that once we fix the first two numbers in the sequence, the entire rest of the
sequence is completely determined, each subsequent number must equal the sum of the two preceding ones. Therefore, we
use backtracking to try all possible ways to choose the first and second numbers by varying their lengths, and for each
choice, we greedily verify whether the remaining digits of the string can be partitioned to satisfy the additive property.
The backtrack function processes the string from left to right, extracting candidate numbers of increasing length. For
the first two numbers (count < 2), we freely explore all possible lengths. Once we have at least two numbers, we compute
the `expectedSum` and prune: if `currentNum` exceeds `expectedSum`, we break (longer substrings will only be larger); if
`currentNum` is less, we continue to try a longer substring. If `currentNum` matches, we recurse deeper. The recursion
succeeds when we consume the entire string with at least 3 numbers in the sequence.

Now, let's look at the solution steps below:

1. Initialize n as the length of the input string num.
2. Define a recursive helper function `backtrack(start, prev1, prev2, count)` where `start` is the current index in `num`,
   `prev1` is the second-to-last number, `prev2` is the last number, and count tracks how many numbers have been placed
   so far.
3. **Base case**: If `start` equals `n` (the entire string has been consumed), return true if count ≥ 3, otherwise return
   false.
4. Iterate over all possible end positions `end` from `start + 1` to `n` (inclusive) to form candidate substrings
   `num[start:end]`.
   - If the substring has length greater than 1 and starts with '0', break out of the loop — this handles the leading-zero
     constraint, since any longer substring starting from the same position will also have a leading zero.
   - Convert the `substring` to an integer `currentNum`.
   - If `count ≥ 2` (meaning we already have at least two numbers), compute `expectedSum` as `prev1 + prev2`.
     - If `currentNum` > `expectedSum`, break as no need to try longer substrings since they will only yield larger values.
     - If `currentNum` < `expectedSum`, continue and try a longer substring that might match the expected sum.
     - If `currentNum` = `expectedSum`, proceed to recurse.
   - Recursively call `backtrack(end, prev2, currentNum, count + 1)`. If it returns true, propagate true upward immediately.
5. If no valid partition is found after exhausting all candidates, return false.
6. Invoke backtrack(0, 0, 0, 0) and return its result.

### Time Complexity

The time complexity is commonly described as O(n^3): O(n^2) choices for the first two numbers, and O(n) to validate the
+rest for each choice. If you also account for substring-to-integer parsing cost, the practical bound can be higher.

> Note that Python natively handles arbitrarily large integers, which addresses the follow-up question about overflow
> for very large inputs, no special handling is needed.

### Space Complexity

The space complexity of the solution is O(n) because the recursion depth is at most O(n) (in the case where each number
is a single digit), and each recursive call uses a constant amount of additional space aside from the call stack.
Substring creation also uses up to O(n) space.
