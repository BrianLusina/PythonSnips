# Frog Jump

A frog is trying to cross a river by jumping on stones placed at various positions along the river. The river is divided
into units, and some units contain stones while others do not. The frog can only land on a stone, but it must not jump
into the water.

You are given an array, stones, that represents the positions of the stones in ascending order (in units). The frog
starts on the first stone, and its first jump must be exactly 1 unit.

If the frog’s last jump was of length k units, its next jump must be either k−1, k, or k+1 units. The frog can only move
forward.

Your task is to determine whether the frog can successfully reach the last stone.

## Constraints

- 2 ≤ `stones.length` ≤ 1000
- 0 ≤ `stones[i]` ≤ 2^20 − 1
- stones[0] == 0
- The stones array is sorted in a strictly increasing order.

## Topics

- Array
- Dynamic Programming

## Solution

The solution’s essence lies in leveraging dynamic programming to track all the jump lengths that can reach each stone.
The frog begins on the first stone with a jump length of zero, and from every reachable stone, it tries jumps of the
same size, one unit longer, or one unit shorter. Each valid move updates the DP table to record new reachable states.
The algorithm stores each stone’s position along with its index in a map, allowing for quick checks to determine if a
stone exists at a given position. Finally, if any jump length reaches the last stone, the frog can successfully cross
the river.

Using the intuition above, we implement the algorithm as follows:
- Store the number of stones in a variable n.
- Create an unordered map, `mapper`, to store each stone’s position as the key and its index as the value for fast
  lookups.
- Populate the `mapper` by mapping every stone position, `stones[i]`, to its index, `i`.
- Initialize a 2D array, `dp`, of size `1001 x 1001` with zeros to track reachable states.
  > Note that this is highly dependable on the constraints, larger sizes of stones will cause an Index out of bounds
  > error. So, ensure to initialize the size correctly
- Set `dp[0][0]` to `1` to indicate that the frog starts on the first stone with a previous jump of 0.
- Iterate over each stone index `i`:
  - For each stone, iterate over all possible previous jump lengths `prevJump`.
  - Check if `dp[i][prevJump]` is 1 to confirm that the frog can reach stone `i` with jump size `prevJump`:
    - If reachable, store the current position as `currPos = stones[i]`.
    - Check if a stone exists at `currPos + prevJump`; if yes, mark `dp[mapper[currPos + prevJump]][prevJump]` as `1`.
    - Check if a stone exists at `currPos + prevJump + 1`; if yes, mark `dp[mapper[currPos + prevJump + 1]][prevJump + 1]` as `1`
    - If `prevJump > 1` and a stone exists at `currPos + prevJump - 1`, mark `dp[mapper[currPos + prevJump - 1]][prevJump - 1]` as `1`.
- After filling the DP table, iterate over all possible jump sizes `jump` for the last stone.
  - If any `dp[n - 1][jump]` equals `1`, return TRUE to indicate that the frog can cross the river.
- If no valid jump leads to the last stone, return FALSE.

![Solution 1](./images/solutions/frog_jump_solution_1.png)
![Solution 2](./images/solutions/frog_jump_solution_2.png)
![Solution 3](./images/solutions/frog_jump_solution_3.png)
![Solution 4](./images/solutions/frog_jump_solution_4.png)
![Solution 5](./images/solutions/frog_jump_solution_5.png)
![Solution 6](./images/solutions/frog_jump_solution_6.png)
![Solution 7](./images/solutions/frog_jump_solution_7.png)
![Solution 8](./images/solutions/frog_jump_solution_8.png)
![Solution 9](./images/solutions/frog_jump_solution_9.png)
![Solution 10](./images/solutions/frog_jump_solution_10.png)
![Solution 11](./images/solutions/frog_jump_solution_11.png)
![Solution 12](./images/solutions/frog_jump_solution_12.png)
![Solution 13](./images/solutions/frog_jump_solution_13.png)
![Solution 14](./images/solutions/frog_jump_solution_14.png)
![Solution 15](./images/solutions/frog_jump_solution_15.png)
![Solution 16](./images/solutions/frog_jump_solution_16.png)
![Solution 17](./images/solutions/frog_jump_solution_17.png)
![Solution 18](./images/solutions/frog_jump_solution_18.png)
![Solution 19](./images/solutions/frog_jump_solution_19.png)
![Solution 20](./images/solutions/frog_jump_solution_20.png)

### Time Complexity

The algorithm’s time complexity is O(n^2), where n is the number of stones. For each stone, it may check all possible
previous jump lengths, and for each valid state, it performs constant-time lookups in the map.

### Space Complexity

The algorithm's space complexity is `O(n)` for the mapper map, plus `O(1)` for the fixed-size 2D DP array (1001 x 1001), assuming the constraints guarantee `n ≤ 1000`.
