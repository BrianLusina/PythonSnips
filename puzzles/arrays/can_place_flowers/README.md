# Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted
in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false
otherwise.

```plain
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false 
```

## Solution(s)

### Approach 1: Single Scan

We can find out the extra maximum number of flowers, `count`, that can be planted
for the given `flowerbed` arrangement. To do so, we can traverse over all the elements of the
`flowerbed` and find out those elements which are 0(implying an empty position). For every such element,
we check if its both adjacent positions are also empty. If so, we can plant a flower at the current position without
violating the no-adjacent-flowers-rule. For the first and last elements, we need not check the previous and the next
adjacent positions respectively.

If the `count` obtained is greater than or equal to nnn, the required number of flowers to be planted, we can
plant nnn flowers in the empty spaces, otherwise not.

#### Complexity Analysis

- Time Complexity: `O(n)`. A single scan of the `flowerbed` array of size `n` is done
- Space Complexity: `O(1)`. Constant extra space is used.

### Approach 2: Single Scan Optimized

Instead of finding the maximum value of `count` that can be obtained, as done in the last approach, we can stop
the process of checking the positions for planting the flowers as soon as `count` becomes equal to nnn. Doing
this leads to an optimization of the first approach. If `count` never becomes equal to `n`, `n` flowers can't be
planted at the empty positions.

#### Complexity Analysis

- Time Complexity: `O(n)`. A single scan of the `flowerbed` array of size `n` is done
- Space Complexity: `O(1)`. Constant extra space is used.

## Related Topics

- Array
- Greedy
