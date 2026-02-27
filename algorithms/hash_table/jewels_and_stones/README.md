# Jewels and Stones

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case-sensitive, so "a" is considered a different type of stone from "A".

## Examples

Example 1:

```text
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
```

Example 2:

```text
Input: jewels = "z", stones = "ZZ"
Output: 0
```

## Constraints

- 1 <= jewels.length, stones.length <= 50
- jewels and stones consist of only English letters.
- All the characters of jewels are unique.

## Topics

- Hash Table
- String

## Solution

The core intuition behind solving this problem is to treat it as a membership-counting task: we aren’t transforming
either string, we’re simply counting how many characters in stones belong to the set of jewel types in jewels, while
respecting case sensitivity. This maps naturally to a hash-based lookup because it lets us store all jewel types in a
structure that supports fast membership checks. In other words, we treat jewels as an allowlist of valid types and stones
as a stream of items to evaluate. As we scan through stones, we increment a counter whenever the current character appears
in the jewel set. As comparisons are case-sensitive, only exact matches contribute to the final count, which represents
how many of your stones are jewels.

Using the intuition above, we implement the algorithm as follows:

1. Initialize a new set, jewelSet, from the given jewels. 
2. Initialize a variable count to 0. 
3. Iterate through each character ch in the stones:
   - If ch exists in jewelSet:
      - Increment count. 
4. After successfully iterating through the stones array, return count.

### Time complexity

The time complexity of the solution is O(m+n) because it first builds a set from the m characters in jewels, then scans the 
n characters in stones once to count matches.

### Space complexity

The space complexity of the solution is O(m) because it stores up to m unique jewel characters in a set.
