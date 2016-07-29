# Math Algorithms

Series of Python snippets on Math Algorithms

## is Prime?

Define a function isPrime that takes one integer argument and returns true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Example

isPrime(5)
=> true
Assumptions
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers.


Find the number of divisors of a positive integer n.

Example:

divisors(4) -> 3 -- 1, 2, 4
divisors(5) -> 2 -- 1, 5
divisors(12) -> 6 -- 1, 2, 3, 4, 6, 12
divisors(30) -> 8 -- 1, 2, 3, 5, 6, 10, 15, 30

from math import sqrt
from itertools import count,islice
def divisors(n):
    is_prime =  lambda num: num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))
    return len([1, n]) if is_prime(n) else len([x for x in range(1, n+1) if n % x == 0])


## Reduce Fraction

Write a function which reduces fractions to their simplest form! Fractions will be presented as an array, and the reduced fraction must be returned as an array:

input: [numerator, denominator]   output: [newNumerator, newDenominator]
                    Eg: [45, 120] --> [3, 8]
All numerators and denominators will be positive integers.

Note: This is an introductory Kata for a series... coming soon!


## Convert Improper Fraction

In Math, an improper fraction is a fraction where the numerator (the top number) is greater than or equal to the denominator (the bottom number) For example: 5/3 (five third).

A mixed numeral is a whole number and a fraction combined into one "mixed" number. For example: 1 1/2 (one and a half) is a mixed numeral.

Write a function convertToMixedNumeral to convert the improper fraction into a mixed numeral.

The input will be given as a string (e.g. '4/3').

The output should be a string, with a space in between the whole number and the fraction (e.g. '1 1/3'). You do not need to reduce the result to its simplest form.

For the purpose of this exercise, there will be no 0, empty string or null input value. However, the input can be:

a negative fraction
a fraction that does not require conversion
a fraction that can be converted into a whole number
Example

```Python
convertToMixedNumeral('6/2') // '3'
convertToMixedNumeral('74/3') // '24 2/3'
convertToMixedNumeral('-504/26') // '-19 10/26'
convertToMixedNumeral('9/18') // '9/18'
```

## Vampire Numbers

Vampire Numbers

Our loose definition of Vampire Numbers can be described as follows:

6 * 21 = 126
6 and 21 would be valid 'fangs' for a vampire number as the 
digits 6, 1, and 2 are present in both the product and multiplicands

10 * 11 = 110
110 is not a vampire number since there are three 1's in the
multiplicands, but only two 1's in the product
Create a function that can receive two 'fangs' and determine if the product of the two is a valid vampire number.
