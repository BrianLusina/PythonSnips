# Word Break

You are given a string, s, and an array of strings, word_dict, representing a dictionary. Your task is to add spaces to 
s to break it up into a sequence of valid words from word_dict. We are required to return an array of all possible 
sequences of words (sentences). The order in which the sentences are listed is not significant.

> Note: The same dictionary word may be reused multiple times in the segmentation.

## Constraints

- 1 <= s.length <= 20
- 1 <= word_dict.length <= 1000
- 1 <= word_dict[i].length <= 10
- s and word_dict[i] consist of only lowercase English letters.
- All the strings in word_dict are unique.

## Topics

- Array
- Hash Table
- String
- Dynamic Programming
- Backtracking
- Trie
- Memoization

## Solutions

### Naive Approach

The naive approach to solve this problem is to use a traditional recursive strategy in which we take each prefix of the 
input string, s, and compare it to each word in the dictionary. If it matches, we take the string’s suffix and repeat 
the process.

Here is how the algorithm works:

1. **Base case**: If the string is empty, there are no characters in the string that are left to process, so there’ll 
   be no sentences that can be formed. Hence, we return an empty array.
2. Otherwise, the string will not be empty, so we’ll iterate every word of the dictionary and check whether or not the 
   string starts with the current dictionary word. This ensures that only valid word combinations are considered:
   - If it doesn’t start with the current dictionary word, no valid combinations can be formed from this word, so we 
     move on to the next dictionary word. 
   - If it does start with the current dictionary word, we have two options:
     - If the length of the current dictionary word is equal to the length of the string, it means the entire string 
       can be formed from the current dictionary word. In this case, the string s is directly added to the result without
       any further processing. 
     - **Recursive case**: Otherwise, the length of the current dictionary word will be less than the length of the 
       string. This means that the string can be broken down further. Therefore, we make a recursive call to evaluate 
       the remaining portion (suffix) of the string.

   - We’ll then concatenate the prefix and the result of the suffix computed by the recursive call above and store it in
     the result.

3. After all possible combinations have been explored, we return the result.

The time complexity of this solution is O(k^n * m), where k is the number of words in the dictionary, `n` is the length
of the string, and `m` is the length of the longest word in the dictionary.

The space complexity is O(k^n * n), where k is the number of words in the dictionary and `n` is the length of the string.

### Optimized approach using dynamic programming - tabulation

Since the recursive solution to this problem is very costly, let’s see if we can reduce this cost in any way. Dynamic 
programming helps us avoid recomputing the same subproblems. Therefore, let’s analyze our recursive solution to see if 
it has the properties needed for conversion to dynamic programming.

- **Optimal substructure**: Given an input string ,s, that we want to break up into dictionary words, we find the first 
    word that matches a word from the dictionary, and then repeat the process for the remaining, shorter input string. 
    This means that, to solve the problem for input `q`, we need to solve the same problem for `p`, where `p` is at 
  least one character shorter than`q`. Therefore, this problem obeys the optimal substructure property.

- **Overlapping subproblems**: The algorithm solves the same subproblems repeatedly. Consider input string “ancookbook” 
  and the dictionary [“an”, “book”, “cook”, “cookbook”]. The following is the partial call tree for the naive recursive 
  solution:
  ```text
          "ancookbook"
         /              \
     "ancookbook"       "cookbook"
     /            \      /         \
  "cookbook"      ... "book"       ...
  ```

From the tree above, it can be seen that the subproblem “cookbook” is evaluated twice. To take advantage of these 
opportunities for optimization, we will use bottom-up dynamic programming, also known as the tabulation approach. This 
is an iterative method of solving dynamic programming problems. The idea is that if a prefix of the input string matches
any word `w` in the dictionary, we can split the string into two parts: the matching word and the suffix of the input 
string. We start from an empty prefix which is the base case. The prefix would eventually develop into the complete 
input string.

> The tabulation approach is often more efficient than backtracking and memoization in terms of time and space complexity 
because it avoids the overhead of recursive calls and stack usage. It also eliminates the need for a separate 
memoization map, as the table itself serves as the storage for the subproblem solutions.

Here’s how the algorithm works:

- We initialize an empty lookup table, dp, of length, n+1, where dp[i] will correspond to the prefix of length i. This 
  table will be used to store the solutions to previously solved subproblems. It will have the following properties:
  - The first entry of the table will represent a prefix of length 0 , i.e., an empty string “”. 
  - The rest of the entries will represent the other prefixes of the string s. For example, the input string “vegan” 
    will have the prefixes “v”, “ve”, “veg”, “vega”, and “vegan”. 
  - Each entry of the table will contain an array containing the sentences that can be formed from the respective prefix. 
    At this point, all the arrays are empty.
- For the base case, we add an empty string to the array corresponding to the first entry of the dp table. This is 
  because the only sentence that can be formed from an empty string is an empty string itself.
- Next, we traverse the input string by breaking it into its prefixes by including a single character, one at a time, 
  in each iteration.
  - For the current prefix, we initialize an array, temp, that will store the valid sentences formed from that prefix. 
    Let’s suppose that the input string is “vegan”, and that the current prefix is “vega”.
  - For all possible suffixes of the current prefix, we check if the suffix exists in the given dictionary. In our 
    example, this would mean checking the dictionary for the suffixes “vega”, “ega”, “ga”, and “a”. For each suffix, it 
    will either match a dictionary word, or not:
    - If it does, we know that the suffix is a valid word from the dictionary and can be used as part of the solution. 
      Therefore, in the dp table, we retrieve all the possible sentences for the prefix to the left of this suffix. 
      Supposing that the current suffix of “vega” is “a”, and that “a” is present in the dictionary, we would retrieve 
      all the sentences already found for “veg”. This means that we reuse the solutions of the subproblem smaller than 
      the current subproblem. Now, we form new sentences for the current prefix by appending a space character and the 
      current suffix (which is a valid dictionary word) to each of the retrieved sentences. Supposing that the valid 
      sentences for the subproblem “veg” are “v eg”, and “ve g”, we will add these new sentences for the current 
      subproblem, “vega”: “veg a”, “v eg a”, and “ve g a”. We add the new sentences to the temp array of this prefix.
    - If the suffix is not present in the dictionary, no sentences can be made from the current prefix, so the temp 
      array of that prefix remains empty.
  - We repeat the above steps for all suffixes of the current prefix.
  - We set the entry corresponding to the current prefix in the dp table equal to the temp array.
- We repeat the steps above for all prefixes of the input string.
- After all the prefixes have been evaluated, the last entry of the dp table will be an array containing all the 
  sentences formed from the largest prefix, i.e., the complete string. Therefore, we return this array.

#### Solution summary

To recap, the solution to this problem can be divided into the following six main steps:

1. We create a 2D table where each entry corresponds to a prefix of the input string. At this point, each entry contains 
   an empty array. 
2. We iterate over all prefixes of the input string. For each prefix, we iterate over all of its suffixes. 
3. For each suffix, we check whether it’s a valid word, i.e., whether it’s present in the provided dictionary. 
4. If the suffix is a valid word, we combine it with all valid sentences from the corresponding entry (in the table) of 
   the prefix to the left of it. 
5. We store the array of all possible sentences that can be formed using the current prefix in the corresponding entry 
   of the table. 
6. After processing all prefixes of the input string, we return the array in the last entry of our table.

![Solution 1](images/solution/word_break_dynamic_programming_tabulation_solution_1.png)
![Solution 2](images/solution/word_break_dynamic_programming_tabulation_solution_2.png)
![Solution 3](images/solution/word_break_dynamic_programming_tabulation_solution_3.png)
![Solution 4](images/solution/word_break_dynamic_programming_tabulation_solution_4.png)
![Solution 5](images/solution/word_break_dynamic_programming_tabulation_solution_5.png)
![Solution 6](images/solution/word_break_dynamic_programming_tabulation_solution_6.png)
![Solution 7](images/solution/word_break_dynamic_programming_tabulation_solution_7.png)
![Solution 8](images/solution/word_break_dynamic_programming_tabulation_solution_8.png)
![Solution 9](images/solution/word_break_dynamic_programming_tabulation_solution_9.png)
![Solution 10](images/solution/word_break_dynamic_programming_tabulation_solution_10.png)
![Solution 11](images/solution/word_break_dynamic_programming_tabulation_solution_11.png)
![Solution 12](images/solution/word_break_dynamic_programming_tabulation_solution_12.png)
![Solution 13](images/solution/word_break_dynamic_programming_tabulation_solution_13.png)

#### Time Complexity

The time complexity of this solution is O(n^2 * v), where n is the length of the string `s` and v is the number of valid
combinations

#### Space Complexity

The space complexity is O(n * v), where n is the length of the string and v is the number of valid combinations stored in
the `dp` array.
