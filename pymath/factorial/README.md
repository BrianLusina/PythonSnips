## Factorial

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,

Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated
sequence on a single line. Suppose the following input is supplied to the program:
8 Then, the output should be:
40320

Also:
Find the sum of the digits in the number n!

---

# Trailing Zeros

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples zeros(6) = 1

# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2

# 12! = 479001600 --> 2 trailing zeros

Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.