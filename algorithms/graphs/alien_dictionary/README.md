# Alien Dictionary

You are given a list of words written in an alien language, where the words are sorted lexicographically by the rules of
this language. Surprisingly, the aliens also use English lowercase letters, but possibly in a different order.

Given a list of words written in the alien language, return a string of unique letters sorted in the lexicographical
order of the alien language as derived from the list of words.

If there’s no solution, that is, no valid lexicographical ordering, you can return an empty string "".

If multiple valid orderings exist, you may return any of them.

> Note: A string, a, is considered lexicographically smaller than string b if:
> 1. At the first position where they differ, the character in a comes before the character in b in the alien alphabet.
> 2. If one string is a prefix of the other, the shorter string is considered smaller.

## Constraints

- 1 <= `words.length` <= 10^3
- 1 <= `words[i].length` <= 20
- All characters in `words[i]` are English lowercase letters

## Examples

![Example 1](./images/examples/alien_dictionary_example_1.png)
![Example 2](./images/examples/alien_dictionary_example_2.png)
![Example 3](./images/examples/alien_dictionary_example_3.png)
![Example 4](./images/examples/alien_dictionary_example_4.png)
![Example 5](./images/examples/alien_dictionary_example_5.png)
