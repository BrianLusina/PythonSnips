# Palindromic Substring

## Palindromic Substring

Given a string, s, return the number of palindromic substrings contained in it. A substring is a contiguous sequence of
characters in a string. A palindrome is a phrase, word, or sequence that reads the same forward and backward.

### Constraints

- 1 <= `s.length` <= 1000
- `s` consists of lower English characters

### Examples

![Example 1](./images/examples/palindromic_substring_example_1.png)
![Example 2](./images/examples/palindromic_substring_example_2.png)

### Solution

If we look at the example above, we notice that any substring of length 3 contains a substring of length 1 at the center.
Although we had already checked all substrings of length 1, our algorithm rechecked them for substrings of longer lengths.
This rechecking consumes a lot of time, which can be avoided by storing and reusing the results of the earlier computations.
To do this, we can create a lookup table, dp, of size n×n, where n is the length of the input string. Each cell dp[i][j]
will store whether the string s[i..j] is a palindromic substring. If the cell dp[i][j] holds the result of the earlier
computation, we will utilize it in O(1) lookup time instead of making a recursive call again.

1. First, we initialize a count variable with 0, which will count the number of palindromic substrings in s.
2. A lookup table is initialized with FALSE.
3. Base case 1: The diagonal in the lookup table is populated with TRUE because any cell in the diagonal corresponds to
   a substring of length one, and any string of length one is always a palindrome. The number of one-letter palindromic 
   strings (i.e., the number of elements in the diagonal) is also added to the count.
4. Base case 2: We check whether all two-letter substrings are palindromes and update the count and dp accordingly. We
   do this by iterating over the string, comparing s[i] and s[i+1], and storing the result at dp[i][i+1]. After that, we
   also increment the count if the value of dp[i][i+1] is TRUE, which tells us that the two-letter substring was a
   palindrome.
5. After these base cases, we check all substrings of lengths greater than two. However, we only compare the first and
   the last characters. The rest of the string is checked using the lookup table. For example, for a given string “zing”,
   we want to check whether “zin” is a palindrome. We’ll only compare ‘z’ and ‘n’ and check the value of dp[1][1], which
   will tell whether the remaining string “i”, represented by s[1..1], is a palindrome. We’ll take the logical AND of
   these two results and store it at dp[0][2] because “zin” is represented by the substring s[0..2]. This way, we’ll
   avoid redundant computations and check all possible substrings using the lookup table.

![Solution 1](./images/solutions/palindromic_substring_solution_1.png)
![Solution 2](./images/solutions/palindromic_substring_solution_2.png)
![Solution 3](./images/solutions/palindromic_substring_solution_3.png)
![Solution 4](./images/solutions/palindromic_substring_solution_4.png)
![Solution 5](./images/solutions/palindromic_substring_solution_5.png)
![Solution 6](./images/solutions/palindromic_substring_solution_6.png)
![Solution 7](./images/solutions/palindromic_substring_solution_7.png)
![Solution 8](./images/solutions/palindromic_substring_solution_8.png)
![Solution 9](./images/solutions/palindromic_substring_solution_9.png)
![Solution 10](./images/solutions/palindromic_substring_solution_10.png)
![Solution 11](./images/solutions/palindromic_substring_solution_11.png)
![Solution 12](./images/solutions/palindromic_substring_solution_12.png)
![Solution 13](./images/solutions/palindromic_substring_solution_13.png)
![Solution 14](./images/solutions/palindromic_substring_solution_14.png)
![Solution 15](./images/solutions/palindromic_substring_solution_15.png)
![Solution 16](./images/solutions/palindromic_substring_solution_16.png)
![Solution 17](./images/solutions/palindromic_substring_solution_17.png)

#### Solution Summary

To recap, the solution to this problem can be divided into the following five main parts:

1. We count all one-letter substrings since any one-letter string is always a palindrome. These results are also stored
   in a lookup table to be used later.
2. Next, the algorithm checks all two-letter substrings and updates the count and the lookup table accordingly.
3. After these base cases, the algorithm checks all possible substrings of lengths greater than three. However, it only
   compares the first and last characters, and the rest of the substring is checked using the lookup table.
4. Whenever a palindromic substring is found, the count and the lookup table are updated accordingly.
5. After checking all possible substrings, the algorithm terminates and returns the count of the palindromic substrings.

#### Complexity Analysis

##### Time Complexity

The time complexity of this algorithm is O(n^2), where n is the length of the input string. This is the time required to
populate the lookup table.

##### Space Complexity

The space complexity of this algorithm is O(n^2), where n is the length of the input string. This is the space occupied
by the lookup table.

---

## Longest Palindromic Substring

Problem Description

Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:

A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).

Input Format
First and only argument is a string A.

Output Format
Return a string denoting the longest palindromic substring of string A.

Example Input
A = "aaaabaaa"

Example Output
"aaabaaa"

Example Explanation
We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".
