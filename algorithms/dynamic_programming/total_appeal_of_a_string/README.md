# Total Appeal of A String

The appeal of a string is the number of distinct characters found in the string.

- For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.

Given a string s, return the total appeal of all of its substrings.

A substring is a contiguous sequence of characters within a string.

## Examples

Example 1:
```text
Input: s = "abbca"
Output: 28
Explanation: The following are the substrings of "abbca":
- Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively. The sum is 5.
- Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively. The sum is 7.
- Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively. The sum is 7.
- Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 5: "abbca" has an appeal of 3. The sum is 3.
The total sum is 5 + 7 + 7 + 6 + 3 = 28.
```

Example 2:
```text
Input: s = "code"
Output: 20
Explanation: The following are the substrings of "code":
- Substrings of length 1: "c", "o", "d", "e" have an appeal of 1, 1, 1, and 1 respectively. The sum is 4.
- Substrings of length 2: "co", "od", "de" have an appeal of 2, 2, and 2 respectively. The sum is 6.
- Substrings of length 3: "cod", "ode" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 4: "code" has an appeal of 4. The sum is 4.
The total sum is 4 + 6 + 6 + 4 = 20.
```

## Constraints

- 1 <= s.length <= 10^5
- s consists of lowercase English letters.

## Topics

- Hash Table
- String
- Dynamic Programming

## Hints

- Consider the set of substrings that end at a certain index i. Then, consider a specific alphabetic character. How do
  you count the number of substrings ending at index i that contain that character?
- The number of substrings that contain the alphabetic character is equivalent to 1 plus the index of the last occurrence
  of the character before index i + 1.
- The total appeal of all substrings ending at index i is the total sum of the number of substrings that contain each
  alphabetic character.
- To find the total appeal of all substrings, we simply sum up the total appeal for each index.

## Solution

The key intuition for solving this problem efficiently is to focus on the contribution of each character to the total
appeal, rather than processing all possible substrings. In any substring, each character contributes only once to the
total appeal, regardless of how many times it appears. Therefore, we can consider only the first occurrence of each
character in any substring as contributing to the total appeal. To achieve this, we keep track of the last index of each
character, which helps us identify when a character appears again, allowing us to avoid counting it multiple times.

To implement this, we calculate the following two values for each character c in the string:

- The number of substrings that end at c. This is calculated by finding the distance from the current index to the last
  occurrence of c.
- The number of substrings that start from c and extend to the end of the string. This is simply the total length of the
  string minus the current index.

The product of these two values gives us the contribution of c to the total appeal. The first value counts the substrings
containing an occurrence of c, and each of these substrings can be concatenated with the substrings formed using the rest
of the characters to create new substrings.

Using the above intuition, the solution can be implemented as follows:
1. Create a hash map, track, to store the last index where each character appeared in the string. It's initialized to −1
   for characters that haven't been seen yet. The maximum number of values that this hash map will store is 26.
2. Create a variable, appeal, to accumulate the total appeal sum.
3. For each character c at index i in the string, calculate the contribution of c to the total appeal.
   - Determine how many new substrings can be formed that end with the current character c. We do this using i - track[c].
     - If track[c] is −1 (meaning c hasn't appeared before), then i - track[c] is simply i+1 (all substrings from the
       start up to index i).
     - If track[c] is a valid index, this expression gives the count of substrings that include the current position but
       exclude previous occurrences of c.
   - Calculate how many substrings can start from the current index i to the end of the string, which can be calculated
     using n - i.
   - The product of these two values gives the total number of substrings contributed by the current character c. Add
     the result of this product to appeal.
4. After calculating the contribution, update the track dictionary to record that the last occurrence of character c is
   now at index i.
5. After processing all characters, return the accumulated result appeal, which is the total appeal sum.

### Time Complexity

The algorithm’s time complexity is O(n), where n is the length of the input string s.

### Space Complexity

The algorithm’s space complexity is O(1), because the maximum number of values that can be stored in the hash map is 26
equivalent to the lowercase English letters.

