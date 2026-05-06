# Russian Doll Envelopes

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an
envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other
envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

## Examples

```text
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
```

Example 2:

```text
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
```

## Constraints

- 1 <= envelopes.length <= 10^5
- envelopes[i].length == 2
- 1 <= wi, hi <= 10^5

## Topics

- Array
- Binary Search
- Dynamic Programming
- Sorting

## Solution

You need to determine the longest chain of envelopes where each envelope in the sequence can fit inside the next one.
Envelopes cannot be rotated.

For example, if you have envelopes [[5,4], [6,4], [6,7], [2,3]], the maximum number you can nest is 3: [2,3] → [5,4] → [6,7].

The solution uses a clever approach by:

- Sorting envelopes by width (ascending) and height (descending for same width)
- Finding the longest increasing subsequence (LIS) based on heights only

The sorting strategy ensures that envelopes with the same width cannot be nested (due to descending height order), while
the LIS on heights gives us the maximum nesting sequence. The algorithm uses binary search (bisect_left) to efficiently
maintain the LIS, achieving O(n log n) time complexity.

The key insight is recognizing this problem as a 2D version of the Longest Increasing Subsequence (LIS) problem. In
standard LIS, we find the longest sequence where each element is greater than the previous one. Here, we need both
dimensions (width and height) to be increasing.

The challenge is handling two dimensions simultaneously. We can't simply apply LIS on pairs because we need both width
AND height to increase together. This is where the sorting strategy becomes crucial.

By sorting envelopes by width first, we ensure that as we traverse the array, we only need to worry about one dimension
- the height. Once sorted by width, any valid nesting sequence must have increasing heights as well.

But there's a subtle issue: what if multiple envelopes have the same width? For example, [3,4] and [3,5]. They can't nest
inside each other since their widths are equal, but if we only consider heights after sorting, we might incorrectly count
both in our sequence.

The clever trick is to sort envelopes with the same width in descending order by height. Why? This prevents us from
selecting multiple envelopes with the same width in our LIS. Since we're looking for an increasing sequence of heights,
and envelopes with the same width are arranged in decreasing height order, we can only pick at most one envelope from
each width group.

After this special sorting (x[0], -x[1]), the problem reduces to finding LIS on the heights alone. The binary search
optimization using bisect_left maintains a list d where d[i] represents the smallest ending height of all increasing
subsequences of length i+1, allowing us to efficiently build the longest sequence.

### Time and Space Complexity

#### Time Complexity O(n log(n))

The time complexity breaks down as follows:

- Sorting the envelopes takes `O(n log n)` where n is the number of envelopes
- Iterating through the sorted envelopes takes `O(n)` time
- For each envelope, we either:
  - Append to the end of array d in `O(1)` time, or
  - Perform binary search using `bisect_left` in `O(log k)` time where k is the current size of array d, and update the
    element at that index in O(1) time
- Since k ≤ n, each binary search operation is at most `O(log n)`
- Overall: `O(n log n) + O(n) * O(log n) = O(n log n)`

#### Space Complexity: O(n)

The space complexity analysis:

- The sorting operation may use `O(log n)` space for the recursion stack (depending on the sorting algorithm
  implementation)
- Array d stores at most n elements in the worst case, requiring O(n) space
- No other significant auxiliary space is used
- Overall: `O(n)` space complexity
