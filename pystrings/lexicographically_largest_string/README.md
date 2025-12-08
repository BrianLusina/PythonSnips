# Find the Lexicographically Largest String From Box

You are given a string, word, and an integer numFriends, representing the number of friends participating in a game 
organized by Alice.

The game consists of multiple rounds, and in each round:
- The string word is split into exactly numFriends non-empty substrings.
- The split must be unique; no previous round has produced the same sequence of splits.
- All resulting substrings from the split are placed into a box.

When all rounds are over and all possible unique splits have been performed, determine the lexicographically largest 
string among all the substrings in the box.

> A string `a` is considered lexicographically larger than a string `b` if:
> - At the first position where `a` and `b` differ, the character in `a` comes later than the corresponding character in 
`b` in the alphabet.
> - If `a` is a prefix of `b`, the longer string is considered larger.
 
**Constraints**

- 1 ≤ `word.length` ≤ 10^3
- `word` consists only of lowercase English letters.
- 1 ≤ `numFriends` ≤ `word.length`

## Examples

![Example 1](./images/examples/lexicographically_largest_string_from_box_example_1.png)
![Example 2](./images/examples/lexicographically_largest_string_from_box_example_2.png)
![Example 3](./images/examples/lexicographically_largest_string_from_box_example_3.png)
![Example 4](./images/examples/lexicographically_largest_string_from_box_example_4.png)
