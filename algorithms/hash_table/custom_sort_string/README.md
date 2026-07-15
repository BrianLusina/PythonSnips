# Custom Sort String

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order
previously.

Permute the characters of `s` so that they match the order that `order` was sorted. More specifically, if a character `x`
occurs before a character `y` in `order`, then `x` should occur before `y` in the permuted string.

Return any permutation of `s` that satisfies this property.

## Examples

Example 1:

```text
Input: order = "cba", s = "abcd"
Output: "cbad"

Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".

Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also
valid outputs.
```

Example 2:

```text
Input: order = "bcafg", s = "abcd"

Output: "bcad"

Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in
s does not appear in order, so its position is flexible.

Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be
placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like
"dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.
```

## Constraints

- 1 <= order.length <= 26
- 1 <= s.length <= 200
- order and s consist of lowercase English letters.
- All the characters of order are unique.

## Topics

- Hash Table
- String
- Sorting

## Solution

### Custom Comparator

A comparator is a tool used to define (or redefine) an order between two items of the same class or data type. Most
languages allow for the use of a custom comparator. This means that we can define a rule that determines how an array
is sorted, and leverage built-in sort functions for custom sort.

Recall that a comparator takes two values c1 and c2 as parameters and returns the following:

1. If c1 comes before c2, return a negative integer.
2. If c1 comes after c2, return a positive integer.
3. If c1 and c2 are equal, return 0.

Letter c1 should come before c2 in the sorted order of s if and only if the index of c1 in the order string is less than
the index of c2. By evaluating c1 and c2 as integer indices, we can use subtraction to achieve a return value that abides
by the three rules described above.

Let's consider the following example: let s = "bdadeec" and order = "edcba". Letter "e" is at index 0 in order, whereas
letter "b" is at index 3. Because 0<3, "e" should come before "b" in the result string. Therefore, the return result is
0−3=−3, a negative number that adheres to the first rule listed above.

Taking into account all possible relationships between pairs of letters, the result string is "eeddcba".

Algorithm

- Create a character array of input string s to allow modification. (In languages like C++ where strings are mutable,
  we can sort s in-place without this step.)
- Use the built-in sort method and define the comparator function as the difference between the index of c1 and the
  index of c2 in order. 
- Concatenate the character array into a string. (Skip if sorting was done in-place.)
- Return this resulting string.

#### Complexity Analysis

Here, we define N as the length of string s, and K as the length of string order.

- Time Complexity: `O(NlogN)`
  Sorting an array of length N requires O(NlogN) time, and the indices of order have to be retrieved for each distinct
  letter, which results in an O(NlogN+K) complexity. K is at most 26, the number of unique English letters, so we can 
  simplify the time complexity to O(NlogN).

- Space Complexity: `O(N) or O(logN)`
  Note that some extra space is used when we sort arrays in place. The space complexity of the sorting algorithm
  depends on the programming language.
  - In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm, which has a space complexity of
    O(logN) for sorting two arrays. The Java solution also uses an auxiliary array of length N. This is the dominating
    term for the Java solution.
  - In C++, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worse-case
    space complexity of O(log⁡N). This is the main space used by the C++ solution.
  - In Python, the sorted() function uses Timsort, which has a space complexity of O(N). The Python solution also creates
    a list of length N from the input string.

### Frequency Table and Counting

Because the order string already gives us the explicit ordering to sort all the letters, we can generate a sorted
version of s without calling upon an O(NlogN) algorithm. Let's create a frequency table where the key equals a character
c, and the value equals how many times c appears in the string s. Then, for each character in order, append the number
of occurrences of that character in s to the resulting string. After iterating through order, any remaining characters
in s can be appended to the end without disrupting the defined sorting order.

Let's look at an example: consider s = "leetcoded" and order = "ecolt", and result is initially an empty string.

Frequency Table:

character	l	e	t	c	o	d
frequency	1	3	1	1	1	2

- The first letter in order is "e", which appears 3 times in s, so result = "eee".
- The second letter in order is "c", which appears 1 times in s, so result = "eeec".
- The third letter in order is "o", which appears 1 times in s, so result = "eeeco".
- The fourth letter in order is "l", which appears 1 times in s, so result = "eeecol".
- The fifth letter in order is "t", which appears 1 times in s, so result = "eeecolt".

Finally, note that some letters in s could be missing in order, so we need to append any remaining letters to result.
In this case, two occurrences of "d" need to be appended, so result = "eeecoltdd" is the final result.

**Algorithm**

- Initialize a frequency table (here we use a Hashmap, but a frequency array works too).
- Populate the frequency table by incrementing freq[letter] for each letter in s.
- For each character of order, append to result the same frequency it appears in s.
- Iterate through the frequency table to find any remaining letters of s not in order, and append these letters to result.
- Return the resulting string.

#### Complexity Analysis

Here, we define N as the length of string s, and K as the length of string order.

##### Time Complexity: O(N)

It takes O(N) time to populate the frequency table, and all other hashmap operations performed take O(1) time in the
average case. Building the result string also takes O(N) time because each letter from s is appended to the result in
the custom order, making the overall time complexity O(N).

##### Space Complexity: O(N)

A hash map and a result string are created, which results in an additional space complexity of O(N).
