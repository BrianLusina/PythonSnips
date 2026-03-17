# Combination Sum

## II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

```plain

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

### Related Topics

- Array
- Backtracking

## III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the
combinations may be returned in any order.

```plain
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
```

### Related Topics

- Array
- Backtracking

## Combination

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

> Note: Combinations are unordered, i.e., [1, 2] and [2, 1] are considered the same combination.

### Examples

Example 1:
```text
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
```

Example 2:
```text
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
```

### Constraints

- 1 <= n <= 20
- 1 <= k <= n

### Topics

- Backtracking

### Solutions

#### Variation 1

- Create an empty list `result` to store the final combinations and an empty list `stack` to store the current combination being
  formed.
- Define a recursive function `backtrack(start)`, which will generate all possible combinations of size `k` from the
  numbers starting from `start` up to `n`.
- In the backtrack function:
  - If the length of `stack` becomes equal to `k`, it means we have formed a valid combination, so we append a copy of
    the current comb list to the `result` list. We use `stack[:]` to create a copy of the list since lists are mutable
    in Python, and we want to preserve the combination at this point without being modified later.
  - If the length of `stack` is not equal to k, we continue the recursion.
- Within the `backtrack` function, use a loop to iterate over the numbers starting from `start` up to `n`.
  - For each number `num` in the range, add it to the current `stack` list to form the combination.
  - Make a recursive call to `backtrack` with `start` incremented by 1. This ensures that each number can only be used
    once in each combination, avoiding duplicate combinations.
  - After the recursive call, remove the last added number from the `stack` list using stack.pop(). This allows us to
    backtrack and try other numbers for the current position in the combination.
- Start the recursion by calling `backtrack(1)` with start initially set to 1, as we want to start forming combinations
  with the numbers from 1 to n.
- After the recursion is complete, the `result` list will contain all the valid combinations of size `k` formed from the
  numbers 1 to n. Return `result` as the final result.

The code uses a recursive backtracking approach to generate all the combinations efficiently. It explores all possible
combinations, avoiding duplicates and forming valid combinations of size k. The result res will contain all such
combinations at the end.

##### Complexity

###### Time complexity: O(n * k)

`n` is the number of elements and `k` is the size of the subset. The backtrack function is called n times, because there
are n possible starting points for the subset. For each starting point, the backtrack function iterates through all k
elements. This is because the `stack` list must contain all k elements in order for it to be a valid subset.

> The time complexity is T(n,k)=O((n/k) * k), as there are(n/k) possible combinations and each requires O(k) work to build
and copy.

###### Space complexity: O(k)

The `stack` list stores at most k elements. This is because the `backtrack` function only adds elements to the `stack`
list when the subset is not yet complete.

#### Variation 2

The algorithm uses a backtracking strategy to generate all possible combinations of size k from the range [1…n]. It
builds each combination step by step, keeping a temporary list path representing the current sequence of chosen numbers.
At every recursive call, the algorithm selects a new number to add to the path and then continues exploring with the next
larger number. If the length of the path becomes equal to k, the combination is complete and is added to the result list.
After exploring one choice, the algorithm backtracks by removing the last number, allowing it to try different alternatives.

To avoid unnecessary work, the recursion stops early whenever the remaining numbers are too few to complete a valid
combination. This pruning ensures the algorithm explores only those paths that can lead to valid results, making it
efficient and systematic in covering all unique combinations without repetition.

The steps of the algorithm are as follows:

1. Create an empty list, `ans`, to store all valid combinations.
2. Define recursive function, `backtrack(path, start)`, where:
   - `path` stores the current partial combination.
   - `start` is the smallest number that can be chosen next.
3. The base case is a complete combination: when `len(path) == k`, save it to ans and return.
4. Calculate remaining needs:
   - Compute `need = k - len(path)` (how many more numbers are required).
   - Compute `max_start = n - need + 1` (the largest possible starting number that still leaves room to complete the
     combination).
5. Recursive exploration: For each number `num` from `start` to `max_start`:
   - Append `num` to `path` (choose).
   - Call `backtrack(path, num + 1)` (explore further).
   - Remove `num` from `path` (backtrack/undo choice).
6. Start recursion by calling `backtrack([], 1)` with an empty path starting from 1.
7. After recursion finishes, return `ans`, which contains all valid combinations.

##### Complexity

###### Time complexity: O(n * k)

The time complexity is T(n,k)=O((n/k) * k), as there are(n/k) possible combinations and each requires O(k) work to build
and copy.

###### Space complexity: O(k)

The space complexity is O(k), as the recursion depth can reach k and the path itself holds at most k numbers during
recursion.
