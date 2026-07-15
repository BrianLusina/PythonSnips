# Word Pattern

Given a `pattern` and a string `s`, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.
Specifically:

- Each letter in `pattern` maps to exactly one unique word in `s`.
- Each unique word in `s` maps to exactly one letter in `pattern`.
- No two letters map to the same word, and no two words map to the same letter.

## Examples

Example 1:

```text
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
```

Example 2:

```text
Input: pattern = "abba", s = "dog cat cat fish"

Output: false
```

Example 3:

```text
Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false
```

## Constraints

- 1 <= `pattern.lengt`h <= 300
- `pattern` contains only lower-case English letters.
- 1 <= `s.length` <= 3000
- `s` contains only lowercase English letters and spaces ' '.
- `s` does not contain any leading or trailing spaces.
- All the words in `s` are separated by a single space.

## Topics

- Hash Table
- String

## Solution(s)

1. [Using two hash maps](#using-two-hash-maps)
2. [Using One hash map](#using-one-hash-map)

### Using two hash maps

The key insight is recognizing that we need to maintain a bidirectional mapping between pattern characters and words.
Think of it like a translation dictionary that works both ways - if we know that 'a' translates to "dog", then "dog"
must always translate back to 'a'.

Why do we need two hash tables instead of just one? Consider this scenario:

- If we only track that 'a' -> "dog" and 'b' -> "dog", we wouldn't catch the error that two different letters map to the
  same word.
- Similarly, if pattern is "aa" and string is "dog cat", using only one mapping wouldn't detect that the same letter 'a'
  is trying to map to two different words.

The bidirectional check ensures both conditions of the bijection are satisfied:

- Forward mapping (d1): Ensures each pattern character consistently maps to the same word
- Reverse mapping (d2): Ensures each word consistently maps to the same pattern character

As we iterate through the pattern and words simultaneously using zip, we check:

- If we've seen this pattern character before (a in d1), does it still map to the same word?
- If we've seen this word before (b in d2), does it still map to the same pattern character?

If either check fails, we know the bijection is broken. If we successfully process all pairs without conflicts, the
pattern matches.

The initial length check (len(pattern) != len(ws)) is a quick optimization - if the pattern has a different number of
characters than we have words, there's no possible valid mapping.

### Time and Space Complexity

#### Time Complexity: O(m + n), where `m` is the length of the pattern string and `n` is the length of string `s`

- Splitting string `s` by spaces takes `O(n)` time as it needs to traverse the entire string.
- The zip operation combined with the loop iterates through `min(pattern length, words length)` elements, which is at
  most `O(m)`iterations after the length check.
- Inside each iteration, dictionary lookups and insertions (in operator and assignment) take `O(1)` average time.

Therefore, the overall time complexity is `O(n)` for splitting + `O(m)` for the loop = `O(m + n)`.

#### Space Complexity: O(m + n), where `m` is the length of the pattern string and `n` is the length of string `s`

- The `words` list stores all words from string `s`, which takes `O(n)` space in the worst case (when `s` contains no
  spaces, the entire string is one word).
- Dictionary `pattern_to_word` stores at most `m` key-value pairs (pattern characters to words), requiring `O(m)` space
  for keys plus the space for word values.
- Dictionary `word_to_pattern` stores at most `m` key-value pairs (words to pattern characters), requiring space for word
  keys plus `O(m)` space for character values.
- The total space used by both dictionaries is proportional to the number of unique pattern characters and unique words,
  bounded by `O(m + n)`. 

Therefore, the overall space complexity is `O(m + n)`.

### Using One Hash Map

The algorithm checks whether a given string of words follows the same pattern as a sequence of characters, ensuring a
one-to-one correspondence (bijection) between pattern characters and words. It begins by splitting the string s into
individual words and verifying that the number of characters in the pattern matches the number of words; if not, it
immediately returns False. Using a hash map, the algorithm records the first index at which each pattern character and
word appear by creating unique keys. As it iterates through the words, it checks that the indices associated with a
character and its corresponding word remain consistent, ensuring that each character maps to exactly one word and each
word maps to exactly one character. If any mismatch occurs in this mapping, return False; otherwise, return True,
confirming that the string follows the specified pattern.

The steps of the algorithm are as follows:

1. Create an empty dictionary map_index to store the mapping indices for pattern characters and words.
2. Use s.split() to divide the string into a list of words.
3. If the number of characters in the pattern does not equal the number of words, return False immediately.
4. Iterate through each character–word pair simultaneously using their indices.
   - For each character c and word w, form two distinct keys:
     - `char_key = 'char_{}'.format(c)`
     - `char_word = 'word_{}'.format(w)`
     - Assign or compare mapping indices:
       - If a key does not exist in map_index, assign its value as the current index i.
       - After the assignment, compare the stored indices for both keys.
       - If the indices do not match, return False (indicating inconsistent mapping).
5. After processing all pairs without inconsistencies, return True, confirming that the pattern matches the word sequence
   correctly.

#### Time and Space Complexity

##### Time Complexity

The time complexity of the above solution is `O(n)` due to splitting the string and iterating through all characters and
words once. Each lookup and insertion in the hash map takes `O(1)` on average, making the total linear in input size.

##### Space Complexity

The space complexity of the above solution is `O(n)` because it stores all unique pattern–word mappings and the list of
words. The hash map and word list grow proportionally to the number of words in the input.
