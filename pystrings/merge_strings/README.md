# Merge Strings Alternatively

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with
word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

```plain
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
```

## Solution

### Approach 1: Two Pointers

#### Intuition

An intuitive method is to use two pointers to iterate over both strings. Assume we have two pointers, `first_pointer`
and `second_pointer`, with `first_pointer` pointing to the first letter of `word1` and `second_pointer` pointing to the
first letter of `word2`. We also create an empty string `merged_word` to store the outcome.

We append the letter pointed to by pointer `first_pointer` i.e., `word1[first_pointer]`, and increment `first_pointer`
by 1 to point to the next letter of `word1`.

Because we need to add the letters in alternating order, next we append `word2[second_pointer]` to `merged_word`. We
also increase `second_pointer` by 1.

We continue iterating over the given strings until both are exhausted. We stop appending letters from `word1`
when `first_pointer` reaches the end of `word1`, and we stop appending letters from `word2` when `second_pointer`
reaches the end of `word2`.

#### Complexity Analysis

Here, `m` is the length of `word1` and `n` is the length of `word2`.

- Time complexity: `O(m+n)`:

  We iterate over `word1` and `word2` once and add their letters into `merged_word`. It would take `O(m+n)` time.

- Space complexity: `O(1)`:

  Without considering the space consumed by the input strings (`word1` and `word2`) and the output
  string (`merged_word`), we do not use more than constant space.

### Approach 2: One Pointer

#### Intuition

To merge the given words, we can also use a single pointer.

Let i be the pointer that we'll use. We begin with i = 0 and progress to the size of the longer word between word1 and
word2, i.e., till i = max(word1.length(), word2.length()).

As we progress to the size of a longer word, we check each time if i points to an index that is in bounds of the words
or not. If i < word1.length(), we append word1[i] to results. Similarly if i < word2.length(), we append word2[i] to
results.

However, if i exceeds the length of any word, we don't have any letters to add from that word, so we ignore it and
continue adding the letter from the longer word.

#### Complexity Analysis

Here, mmm is the length of word1 and nnn is the length of word2.

- Time complexity: `O(m+n)`

  We iterate over word1 and word2 once pushing their letters into result. It would take `O(m+n)` time.

- Space complexity: `O(1)`

  Without considering the space consumed by the input strings (word1 and word2) and the output string (result), we do
  not use more than constant space.
