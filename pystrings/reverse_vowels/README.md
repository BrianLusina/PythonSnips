# Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

```plain
Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede" 
```

## Solution

### Approach 1: Two Pointers

#### Intuition

We will initialize two pointers, one pointer (referred as `left_pointer`) pointing to the left end of the input string
and the
other pointer (named as `right_pointer`) pointing to the right end of the string.

To achieve this, we would initialize a `left pointer` to 0 and keep incrementing it until we get a vowel. Similarly, we
initialize the `right pointer` to the last index and keep decrementing it until it points to a vowel. At each such
iteration where both the pointers are pointing to the vowel, we would swap the characters at these pointers.

#### Algorithm

1. Initialize the left pointer start to 0, and the right pointer end to s.size() - 1.
2. Keep iterating until the left pointer catches up with the right pointer:
    - Keep incrementing the left pointer start until it's pointing to a vowel character.
    - Keep decrementing the right pointer end until it's pointing to a vowel character.
    - Swap the characters at the start and end.
    - Increment the start pointer and decrement the end pointer.
3. Return the string s.

#### Complexity Analysis

Here, `N` is the length of the string `s`.

##### Time complexity: `O(N)`

It might be tempting to say that there are two nested loops and hence the complexity would be `O(N^2)`. However, if we
observe closely the pointers start and end will only traverse the index once. Each element of the
string `s` will be iterated only once either by the left or right pointer and not both. We swap characters when both
pointers point to vowels which are `O(1)` operation. Hence the total time complexity will be `O(N)`.

Note that in we need to convert the string to a list as strings are immutable and hence it would take `O(N)` time.

##### Space complexity: `O(N)`

Since we need to convert the string to a list that would take `O(N)` space, and therefore the space complexity is `O(N)`.

## Related Topics

- Two Pointers
- String
