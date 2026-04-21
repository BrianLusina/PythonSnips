# Powerful Integers

Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to
bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.

## Examples

Example 1:

```text
Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 20 + 30
3 = 21 + 30
4 = 20 + 31
5 = 21 + 31
7 = 22 + 31
9 = 23 + 30
10 = 20 + 32
```

Example 2:
```text
Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]
```

## Constraints

- 1 <= x, y <= 100
- 0 <= bound <= 10^6

## Topics

- Hash Table
- Math
- Enumeration

## Solution(s)

1. [Logarithmic Bounds](#logarithmic-bounds)
2. [Logarithmic Bound 2](#logarithmic-bound-2)

### Logarithmic Bounds

Our approach here will only focus on finding the bounds for numbers x and y. One way to get the bounds on the powers is
to have nested loops that iterate from [0⋯bound]. However, this is very inefficient because the bound can be an extremely
large value and a nested-loop over this bound will take forever to finish. Also, we don't need to iterate over all of the
values and combinations. There is a way to find a much smaller bound for the powers.

m^n <= bound

This formula implies that

n<=log(m) bound

> We can use the log function to determine the bounds for the powers of "x" and "y".

#### Algorithm

1. Let's define `a` as the power bound for the number `x`. Thus `a=log(x)bound`.
2. Similarly, let's define `b` as the power bound for the number `y`. Thus `b=log(y)bound`.
3. Now we will have our nested for-loop structure where the outer loop will iterate from [0⋯a] and the inner loop will
   iterate from [0⋯b].
4. We will use a set to store our results. This is because we might generate the same value multiple times. E.g. 
   `2^1 + 3^2 = 11` and `2^3 + 3^1 = 11`. We only need to include the value 11 once and hence, we will use a set called
   `resultSet` to store our answers.
5. At each step, we calculate `x^a + y^b` and check if this value is less than or equal to bound. If it is, then this is
   a powerful integer and we add it to our set of answers.
6. We need special break conditions to handle the scenario when x or y is 1. This is because if the number x or y is 1,
   then their power-bound will be equal to bound itself. Also, it doesn't matter what their power-bound is because 1^N
   is always 1. Thus, when the number is 1, we don't need to loop from [0⋯N] and we can break early.
7. Finally, convert the set to a list and return.

#### Time Complexity

Time Complexity: Let `N` be `log(x)bound` and `M` be `log(y)bound`. Then the overall time complexity is `O(N×M)` because
we used a nested loop structure to calculate all of the powerful integers.

#### Space Complexity

`O(N×M)` because we use a set to omit duplicates. We could just use our result list to check membership before adding
values. However, that would be costly in terms of time complexity because it would require a full scan of the result list
to see if the value already exists.

### Logarithmic Bound 2

The key insight is that since x^i and y^j grow exponentially, the number of distinct powers of x and y that remain within
bound is at most O(log(bound) each. We can enumerate all pairs (i,j) by iterating through powers of x in an outer loop
and powers of y in an inner loop, adding each sum x^i + y^j that is less than or equal to bound into a hash set called
`resultSet`. The set automatically handles deduplication, ensuring each powerful integer appears at most once. A special
case arises when x or y equals 1, because 1^i is always 1 regardless of the exponent, which would cause an infinite loop.
We handle this by breaking out of the respective loop after the first iteration when x or y is 1.

Solution steps:

1. Initialize an empty set resultSet to store unique powerful integers.
2. Initialize `powX` to 1, representing x^0
3. Start an outer while loop that continues as long as `powX ≤ bound`.
   - Inside the outer loop, initialize `powY` to 1, representing y^0
   - Start an inner while loop that continues as long as `powX + powY ≤ bound`.
     - Add the value `powX` + `powY` to `resultSet`.
     - If y equals 1, break out of the inner loop immediately, since y^j will always be 1 and further iterations would
       not produce new values.
     - Otherwise, multiply `powY` by y to advance to the next power of y.
   - After the inner loop, if x equals 1, break out of the outer loop immediately, since x^i will always be 1 and further
     iterations would not produce new values.
   - Otherwise, multiply `powX` by x to advance to the next power of x.
4. Convert resultSet to a list and return it.

#### Time Complexity

The time complexity of the solution is O(logx(bound)) * logy(bound) because the outer loop runs at most O(logx(bound))
times and the inner loop runs at most O(logy(bound)) times for each iteration of the outer loop. Since bound ≤10^6 and
the minimum base greater than 1 is 2, each loop runs at most about log2(10^6)≈20 iterations, making this very efficient.
When x or y is 1, the corresponding loop runs only once.

#### Space Complexity

The space complexity is `O(logx(bound)) * logy(bound)`  because in the worst case, every combination of powers produces
a unique sum, and all of these are stored in the resultSet. This is bounded by the total number of pairs enumerated,
which is at most `O(logx(bound)) * logy(bound)`.
