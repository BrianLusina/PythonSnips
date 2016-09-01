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

## FizzBuzz

Task
Write a program that prints the integers from   1   to   100   (inclusive).

But:

  for multiples of three,   print   Fizz     (instead of the number)
  for multiples of five,   print   Buzz     (instead of the number)
  for multiples of both three and five,   print   FizzBuzz     (instead of the number)

The   FizzBuzz   problem was presented as the lowest level of comprehension required to illustrate adequacy.

## Divisble by 7, not by 5

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

## Factorial

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

## Q_formula

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. 

## DigitCount
Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer. Square all numbers k (0 <= k <= n) between 0 and n. Count the numbers of digits d used in the writing of all the k**2. Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.

Examples:

n = 10, d = 1, the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in 1, 16, 81, 100. The total count is then 4.

nb_dig(25, 1):
the numbers of interest are
1, 4, 9, 10, 11, 12, 13, 14, 19, 21 which squared are 1, 16, 81, 100, 121, 144, 169, 196, 361, 441
so there are 11 digits `1` for the squares of numbers between 0 and 25.

## Climb Sequence

For every positive integer N, there exists a unique sequence starting with 1 and ending with N and such that every number
in the sequence is either the double of the preceeding number or the double plus 1.

For example, given N = 13, the sequence is [1, 3, 6, 13], because . . . :

 3 =  2*1 +1
 6 =  2*3
 13 = 2*6 +1
Write a function that returns this sequence given a number N. Try generating the elements of the resulting list in ascending order, i.e.,
without resorting to a list reversal or prependig the elements to a list.

## Super Size

Write a function that rearranges an interger into its largest possible value.

``` python
super_size(123456) # 654321
super_size(105)    # 510
super_size(12)     # 21
```

If the argument passed through is single digit or is already the maximum possible integer, your function should simply return it.

## Pernicious

A pernicious number is a positive integer whose binary digit sum (or Hamming weight) is a prime number.

25 = 11010  -->  digit sum = 3 --> 3 is prime --> therefore 25 is a pernicious number 

75 = 1001011  -->  digit sum = 4 --> 4 is not prime --> therefore 75 is not a pernicious number
Task

Your job is to create a function that will list all of the pernicious numbers up to the given value (inclusive). The values given will increase in size, meaning the list will be very large.

For example:
```pernicious
pernicious(5) should return [3, 5]

pernicious(12) should return [3, 5, 6, 7, 9, 10, 11, 12]
```

If there are no pernicious numbers in the given range, your function should return "No pernicious numbers". This means when given a negative value, it should still recieve this output.
```python
pernicious(0) should return "No pernicious numbers"

pernicious(-1) should return "No pernicious numbers"
```

Also, if given a floating point number, return the list of pernicious numbers with the number floored (rounded down).

```python
pernicious(17.546456) should return [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 17]
```

You will only be given integers and floats.

Remember:

1 is not a prime number and 2 is a prime number.


## EvenDigits

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

## Population Growth

In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (number of inhabitants is an integer)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.
More generally given parameters:

p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)

the function nb_year should return n number of entire years needed to get a population greater or equal to p.

aug is an integer (> 0), percent a positive or null floating number, p0 and p are positive integers (> 0)

Examples:
``` python
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
```

Note: Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.

## Largest Pair

Rick wants a faster way to get the product of the largest pair in an array. Your task is to create a performant solution to find the product of the largest two integers in a unique array of positive numbers.
All inputs will be valid.
Passing [2, 6, 3] should return 18, the product of [6, 3].

> Disclaimer: Mr. Roll will only accept solutions that are faster than his, which has a running time O(nlogn).

``` python
maxProduct([2, 1, 5, 0, 4, 3])              // 20
maxProduct([7, 8, 9])                       // 72
maxProduct([33, 231, 454, 11, 9, 99, 57])   // 104874
```

> FUNDAMENTALS ARRAYS ALGORITHMS LOOPS CONTROL FLOW BASIC LANGUAGE FEATURES SORTING

## Triangle Odd

Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:
``` python
row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
```

> FUNDAMENTALS ARRAYS LISTS DATA STRUCTURES NUMBERS ARITHMETIC MATHEMATICS ALGORITHMS

## Make Larger Number

Given a number whose digits are unique, find the next larger number that can be formed with those digits.
For example: 241 will output 421, 27 will output 72 and 68734 will output 87643

## Sum Same Digit

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


## Filter evens
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.



