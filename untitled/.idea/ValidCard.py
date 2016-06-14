# -*- coding: utf-8 -*-

"""
Write a function that checks whether a credit card number is correct or not, using the Luhn algorithm.

The algorithm is as follows:

From the rightmost digit, which is the check digit, moving left, double the value of every second digit;
if the product of this doubling operation is greater than 9 (e.g., 8 × 2 = 16), then sum the digits of the products (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or alternatively subtract 9 from the product (e.g., 16: 16 - 9 = 7, 18: 18 - 9 = 9).
Take the sum of all the digits.
If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula; else it is not valid.
The input is a string with the full credit card number, in groups of 4 digits separated by spaces, i.e. "1234 5678 9012 3456"
Don´t worry about wrong inputs, they will always be a string with 4 groups of 4 digits each separated by space.

Examples

         ValidCard.valid_card?("5457 6238 9823 4311") # -> true
         ValidCard.valid_card?("5457 6238 9323 4311") # -> false

for reference check: https://en.wikipedia.org/wiki/Luhn_algorithm
"""
class Test(object):
    def __init__(self,n):
        self.n = n

    @staticmethod
    def test_function(actual, expected):
        print "Test for " + str(actual) + " passed " if actual == expected else "Test for " + str(actual) + " failed, expected " + str(expected)


class ValidCard(object):
    def __init__(self, card):
        self.card = card


    @staticmethod
    def valid_card(card):
        newC = card.replace(' ', '') #replace all whitespace and convert to string
        li = [int(y) for y in newC] #sum of all the digits

        for i in newC[::-2]:
            x = int(i)
            if x * 2 > 9:
                (x * 2) - 9
                if sum(li) % 10 == 0:
                    return True
                else:
                    return False


Test.test_function(ValidCard.valid_card("5457 6238 9823 4311"), True)
Test.test_function(ValidCard.valid_card("8895 6238 9323 4311"), False)
Test.test_function(ValidCard.valid_card("5457 6238 5568 4311"), False)
Test.test_function(ValidCard.valid_card("5457 6238 9323 4311"), False)
Test.test_function(ValidCard.valid_card("2222 2222 2222 2224"), True)
Test.test_function(ValidCard.valid_card("5457 1125 9323 4311"), False)
Test.test_function(ValidCard.valid_card("1252 6238 9323 4311"), False)
Test.test_function(ValidCard.valid_card("9999 9999 9999 9995"), True)
Test.test_function(ValidCard.valid_card("0000 0300 0000 0000"), False)
Test.test_function(ValidCard.valid_card("4444 4444 4444 4448"), True)
Test.test_function(ValidCard.valid_card("5457 6238 9323 1252"), False)
Test.test_function(ValidCard.valid_card("5457 6238 1251 4311"), False)
Test.test_function(ValidCard.valid_card("3333 3333 3333 3331"), True)
Test.test_function(ValidCard.valid_card("6666 6666 6666 6664"), True)
Test.test_function(ValidCard.valid_card("5457 6238 0254 4311"), False)
Test.test_function(ValidCard.valid_card("0000 0000 0000 0000"), True)
Test.test_function(ValidCard.valid_card("5457 1111 9323 4311"), False)
Test.test_function(ValidCard.valid_card("5457 6238 9823 4311"), True)
Test.test_function(ValidCard.valid_card("1145 6238 9323 4311"), False)
Test.test_function(ValidCard.valid_card("8888 8888 8888 8888"), True)
Test.test_function(ValidCard.valid_card("0025 2521 9323 4311"), False)
Test.test_function(ValidCard.valid_card("5457 6238 9323 4311"), False)
Test.test_function(ValidCard.valid_card("1111 1111 1111 1117"), True)
Test.test_function(ValidCard.valid_card("1234 5678 9012 3452"), True)
Test.test_function(ValidCard.valid_card("5458 4444 9323 4311"), False)
Test.test_function(ValidCard.valid_card("5457 6238 3333 4311"), False)
Test.test_function(ValidCard.valid_card("0123 4567 8901 2345"), False)
Test.test_function(ValidCard.valid_card("5555 5555 5555 5557"), True)

card = "5457 6238 9823 4311"
mCard = card.replace(" ", "")
intCard = [int(y) for y in mCard]

print "New Card",mCard, "Digits sum",sum(intCard)
print "Every 2nd Digit", intCard[::-2]

doubler = (2).__mul__
sub9 = (9).__sub__
sumDig = lambda x:x-9

intCard[::-2] = map(doubler,intCard[::-2])
print intCard
intCard[::-2] = map(sumDig,intCard[::-2])

print intCard
