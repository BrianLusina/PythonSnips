# Paint House

You are a renowned painter who is given a task to paint n houses in a row. You can paint each house with one of three colors: Red, Blue, or Green. The cost of painting each house with each color is different and given in a 2D array costs:

- costs[i][0] = cost of painting house `i` Red
- costs[i][1] = cost of painting house `i` Blue
- costs[i][2] = cost of painting house `i` Green

No two neighboring houses can have the same color. Return the minimum cost to paint all houses.

## Constraints

- 1 ≤ n ≤ 100
- costs[i].length == 3
- 1 ≤ costs[i][j] ≤ 1000

## Examples

Example 1

```text
costs = [[8, 4, 15], [10, 7, 3], [6, 9, 12]]
Output: 13

Explanation:

House 0: Blue (cost = 4)
House 1: Green (cost = 3)
House 2: Red (cost = 6)
Total = 4 + 3 + 6 = 13

```

Example 2
```text
Input:

costs = [[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 5, 9]]
Output: 30

Explanation: Red(5) → Green(13) → Red(7) → Blue(5) = 30
```

## Solution

The solution implements a space-optimized dynamic programming approach using three variables to track the minimum costs.

Variable Initialization:

prev_min_cost_red = 0: Minimum cost if the current house is painted red (color 0)
prev_min_cost_blue = 0: Minimum cost if the current house is painted blue (color 1)
prev_min_cost_green = 0: Minimum cost if the current house is painted green (color 2)

These start at 0 because before painting any house, the cost is 0.

Main Loop: The algorithm iterates through each house's costs using tuple unpacking:

```python
for cost_red, cost_blue, cost_green in costs:
    # 
```

Where cost_red, cost_blue, cost_green represent the costs of painting the current house with red, blue, and green
respectively.

State Transition: For each house, we simultaneously update all three variables:

```python
prev_min_cost_red, prev_min_cost_blue, prev_min_cost_green = min(prev_min_cost_blue, prev_min_cost_green) + cost_red, 
min(prev_min_cost_red, prev_min_cost_green) + cost_blue, min(prev_min_cost_red, prev_min_cost_blue) + cost_green
```

Breaking this down:

- New `prev_min_cost_red` (cost if current house is red): `min(prev_min_cost_blue, prev_min_cost_gree) + cost_red` 
  We take the minimum of the previous costs where the house was NOT red (either blue or green)
  Add the cost of painting the current house red

- New `prev_min_cost_blue` (cost if current house is blue): `min(prev_min_cost_red, prev_min_cost_green) + cost_blue`
  We take the minimum of the previous costs where the house was NOT blue (either red or green)
  Add the cost of painting the current house blue

- New `prev_min_cost_green` (cost if current house is green): `min(prev_min_cost_red, prev_min_cost_blue) + cost_blue`
  We take the minimum of the previous costs where the house was NOT green (either red or blue)
  Add the cost of painting the current house green

The simultaneous assignment is crucial here - all three values are calculated using the old values before any updates occur.

Final Result: After processing all houses, `prev_min_cost_red`, `prev_min_cost_blue`, and `prev_min_cost_green` contain
the minimum costs to paint all houses with the last house being red, blue, or green respectively. The answer is the
minimum among these three values:

`return min(prev_mins_cost_red, prev_min_cost_blue, prev_min_cost_green)`

### Complexity Analysis

#### Time Complexity: O(n)

Where n is the number of houses (length of the costs array). The algorithm iterates through the costs array exactly once,
performing constant-time operations (comparisons and additions) for each house.

#### Space Complexity: O(1)

The algorithm uses only three variables (`prev_min_cost_red`, `prev_min_cost_blue`, `prev_min_cost_green`) to track the
minimum costs regardless of the input size. The space usage remains constant as it doesn't create any additional data
structures that scale with the input. The variables are reused and updated in each iteration rather than storing all
intermediate results.
