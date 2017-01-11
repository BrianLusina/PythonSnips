## Vampire Numbers

Our loose definition of Vampire Numbers can be described as follows:

6 * 21 = 126

6 and 21 would be valid 'fangs' for a vampire number as the 

digits 6, 1, and 2 are present in both the product and multiplicands

10 * 11 = 110

110 is not a vampire number since there are three 1's in the

multiplicands, but only two 1's in the product
Create a function that can receive two 'fangs' and determine if the product of the two is a valid vampire number.

## More Precise definition

A vampire number is a natural number with an even number of digits, that can be factored into two integers. These two factors are called the fangs, and must have the following properties:

they each contain half the number of the digits of the original number
together they consist of exactly the same digits as the original number
at most one of them has a trailing zero

An example of a Vampire number and its fangs: 1260 : (21, 60)

