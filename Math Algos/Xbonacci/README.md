# Xbonacci

JS programs here are about the *xbonacci* sequences. he involve or derive their basic solutions and problems from the fibonacci sequence.
Here is a breakdown of some of the problems and their solutions

## fibonacci

The Fibonacci numbers are the numbers in the following integer sequence (Fn):

 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
 such as

 F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
 Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

 F(n) * F(n+1) = prod.
 Your function productFib takes an integer (prod) and returns an array:

 if F(n) * F(n+1) = prod or returns

 if you don't find two consecutive F(m) verifying F(m) * F(m+1) = prod. F(m) will be the smallest one such as F(m) * F(m+1) > prod.

 Examples

 productFib(714) # should return [21, 34, true],
 # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

 productFib(800) # should return [34, 55, false],
 # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
 Note: Not useful here but we can tell how to choose the number n up to which to go: we can use the "golden ratio" phi which is (1 + sqrt(5))/2 knowing that F(n) is asymptotic to: phi^n / sqrt(5). That gives a possible upper bound to n.

## Tribonacci

Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1,1,1] as a starting input (AKA signature), we have this sequence:

[1,1,1,3,5,9,17,31,...]
But what if we started with [0,0,1] as a signature? As starting with [0,1] instead of [1,1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0,0,1,1,2,4,7,13,24,...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n==0, then return an empty array and be ready for anything else which is not clearly specified ;)

## fibonacci, Tribonacci and Friends

Well, time to expand the family a little more: think of a Quadribonacci starting with a signature of 4 elements and each following element is the sum of the 4 previous, a Pentabonacci (well Cinquebonacci would probably sound a bit more italian, but it would also sound really awful) with a signature of 5 elements and each following element is the sum of the 5 previous, and so on.

Well, guess what? You have to build a Xbonacci function that takes a signature of X elements - and remember each next element is the sum of the last X elements - and returns the first n elements of the so seeded sequence.
```python
Xbonacci([1,1,1,1],10)==[1,1,1,1,4,7,13,25,49,94]
Xbonacci([0,0,0,0,1],10)==[0,0,0,0,1,1,2,4,8,16]
Xbonacci([1,0,0,0,0,0,1],10)==[1,0,0,0,0,0,1,2,3,6]
```
