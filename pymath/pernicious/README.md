## Pernicious

A pernicious number is a positive integer whose binary digit sum (or Hamming weight) is a prime number.

25 = 11010 -->  digit sum = 3 --> 3 is prime --> therefore 25 is a pernicious number

75 = 1001011 -->  digit sum = 4 --> 4 is not prime --> therefore 75 is not a pernicious number Task

Your job is to create a function that will list all of the pernicious numbers up to the given value (inclusive). The
values given will increase in size, meaning the list will be very large.

For example:

```pernicious
pernicious(5) should return [3, 5]

pernicious(12) should return [3, 5, 6, 7, 9, 10, 11, 12]
```

If there are no pernicious numbers in the given range, your function should return "No pernicious numbers". This means
when given a negative value, it should still recieve this output.

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
