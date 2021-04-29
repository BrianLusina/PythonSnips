A natural number is called k-prime if it has exactly k prime factors, counted with multiplicity. For example:

k = 2  -->  4, 6, 9, 10, 14, 15, 21, 22, ...
k = 3  -->  8, 12, 18, 20, 27, 28, 30, ...
k = 5  -->  32, 48, 72, 80, 108, 112, ...
A natural number is thus prime if and only if it is 1-prime.

Task:
Complete the function find_k_primes,which is given parameters k, start, end (or nd) and returns an array of the k-primes between start (inclusive) and end (inclusive).

Example:
find_k_primes(5, 500, 600) --> [500, 520, 552, 567, 588, 592, 594]