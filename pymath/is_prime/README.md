## is Prime?

Define a function isPrime that takes one integer argument and returns true or false depending on if the integer is a
prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1
and itself.

Example

isPrime(5)
=> true Assumptions You can assume you will be given an integer input. You can not assume that the integer will be only
positive. You may be given negative numbers.

Find the number of divisors of a positive integer n.

Example:

divisors(4) -> 3 -- 1, 2, 4 divisors(5) -> 2 -- 1, 5 divisors(12) -> 6 -- 1, 2, 3, 4, 6, 12 divisors(30) -> 8 -- 1, 2,
3, 5, 6, 10, 15, 30

from math import sqrt from itertools import count,islice def divisors(n):
is_prime = lambda num: num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))
return len([1, n]) if is_prime(n) else len([x for x in range(1, n+1) if n % x == 0])

## Testing for prime numbers with Regex

Check this [link](http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/) for more
info.



