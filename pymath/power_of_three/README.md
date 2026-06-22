# Power Of Three

Given an integer n, return `true` if it is a power of three. Otherwise, return `false`.

An integer n is a power of three, if there exists an integer x such that `n == 3^x`.

## Examples

Example 1:

```text
Input: n = 27
Output: true
Explanation: 27 = 33
```

Example 2:
```text
Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.`
```

Example 3:
```text
Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
```

## Constraints

- -2^31 <= n <= 2^31 - 1

## Topics

- Math
- Recursion

## Solution

### Using Modulo

The key insight is that since 3 is a prime number, any power of 3 will only have 3 as its prime factor. The largest power
of 3 that fits within a 32-bit signed integer range is `3^19 = 1162261467`. If `n` is a power of 3, then n must be a
divisor of `1162261467`. Because 3 is prime, the only divisors of 3^19 are 3^0, 3^1, 3^2,...3^19, which are exactly all
the powers of 3 in range. Therefore, we simply check whether n is positive and whether `1162261467` is evenly divisible
by `n`. This approach requires no loops or recursion.

Now, let’s look at the solution steps below:

1. Check if n is greater than 0. Any power of 3 must be a positive integer, so if n is 0 or negative, return false
   immediately.
2. Compute 1162261467 % n, where 1162261467 is 3^19, the largest power of three within the 32-bit signed integer range.
   - If the remainder equals 0, then n is a divisor of 3^19, meaning n is itself a power of 3. Return true.
   - If the remainder is not 0, then n is not a power of 3. Return false.

#### Time Complexity

The time complexity of the solution is O(1) because we perform a single comparison and a single modulo operation, both
of which take constant time regardless of the input.

#### Space Complexity

The space complexity of the solution is O(1) because we use only a fixed amount of space (no additional data structures)
and the constant 1162261467 is stored as a single integer.

### Using Loops

To check if a number is a power of three, we need to think about what it means mathematically. If n = 3^x, then we can
keep dividing n by 3 exactly x times until we reach 1. This is the key insight.

Think of it like peeling layers off an onion. If we have 27 = 3^3, we can divide by 3 three times: 27 ÷ 3 = 9, then
9 ÷ 3 = 3, then 3 ÷ 3 = 1. We end up with exactly 1, confirming that 27 is indeed a power of three.

On the other hand, if we try this with a non-power like 45: 45 ÷ 3 = 15, then 15 ÷ 3 = 5. Now 5 is not divisible by 3
(it gives remainder 2), so we know 45 cannot be a power of three.

The pattern becomes clear: a power of three should be repeatedly divisible by 3 until we reach 1, with no remainders
along the way. If at any point during our division we get a remainder (checked using n % 3), we immediately know the
number isn't a power of three.

The algorithm naturally emerges from this observation: keep dividing by 3 while checking for remainders. If we
successfully reduce the number to 1 through repeated division by 3, it's a power of three. If we encounter a remainder
or end up with a number other than 1, it's not.

The solution implements the trial division method to determine if a number is a power of three. Let's walk through the
implementation step by step:

- Main Loop Condition: The algorithm starts with a while loop that continues as long as n > 2. This is because the 
  smallest power of three greater than 2 is 3^1 = 3. Any power of three will be at least 3, so we can stop when n
  becomes 2 or less.
- Divisibility Check: Inside the loop, we check if n % 3 is non-zero. The modulo operation n % 3 returns the remainder
  when n is divided by 3. If there's any remainder (meaning n % 3 evaluates to true), then n is not perfectly divisible
  by 3, which means it cannot be a power of three. We immediately return False.
- Division Step: If n is divisible by 3 (passes the modulo check), we perform integer division: n //= 3. This reduces n
  by a factor of 3 and continues the process. The integer division operator // ensures we're working with whole numbers
  throughout.
- Final Check: After the loop exits (when n <= 2), we check if n == 1. If we've successfully divided a power of three by
  3 repeatedly, we should end up with exactly 1. For example:
  - 27 → 9 → 3 → 1 (returns True)
  - 18 → 6 → 2 (returns False since 2 ≠ 1)

#### Time Complexity 

The algorithm uses a while loop that repeatedly divides n by 3 until n becomes less than or equal to 2. In each iteration,
we perform:

- A modulo operation n % 3 to check divisibility
- An integer division n //= 3 to reduce n

The number of iterations is determined by how many times we can divide n by 3 before it becomes less than or equal to 2.
This is equivalent to finding the largest integer k such that 3^k ≤ n, which gives us k ≤ log₃n. Therefore, the loop
runs at most ⌊log₃n⌋ times, resulting in a time complexity of O(log₃n).

#### Space Complexity

The algorithm only uses a constant amount of extra space:

- The input variable n is modified in place
- No additional data structures are created
- The space used does not depend on the size of the input

Therefore, the space complexity is O(1).

### Using Logarithms

A common loop-free math check (for positive integers n):

- Compute x = log₃n = ln(n)/ln(3)
- Check whether x is an integer: x ≈ k for some integer k (e.g., ∣x−round(x)∣<ε like 10^−10)
- If yes, then n = 3^k; otherwise it isn’t.

Alternative integer-only (no loops) via factorization: compute whether n has any prime factors other than 3, and whether
the exponent of 3 is ≥ 0; but that typically requires some factoring method.
