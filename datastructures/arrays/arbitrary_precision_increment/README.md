# Arbitrary Precision Increment

Given: An array of non-negative digits that represent a decimal integer.

Problem: Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision
arithmetic.

```text
Array A
[1, 4, 9]
|
Adding 1
|
Array A
[1, 5, 0]
```
> Example 1

```text
Array A
[9, 9, 9]
|
Adding 1
|
Array A
[1, 0, 0, 0]
```
> Example 2