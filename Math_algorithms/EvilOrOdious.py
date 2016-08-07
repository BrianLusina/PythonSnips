"""
Instructions
Output
The number n is Evil if it has an even number of 1's in its binary expansion.
First ten: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20

The number n is Odious if it has an odd number of 1's in its binary expansion.
First ten: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19

You have to write a function that determine if a number is Evil of Odious, function should return "It's Evil!" in case of evil number and "It's Odious!" in case of odious number.
"""

class EvilOrOdious(object):
    def __init__(self,n):
        self.n = n

    @staticmethod
    def evil(n):
        return "It's Evil!" if "{0:b}".format(n).count("1")%2 == 0 else "It's Odious!"
        #return "It's %s!" % ["Evil","Odious"][bin(n).count("1")%2]

class Test(object):
    def __init__(self,n):
        self.n = n

    @staticmethod
    def test_function(actual,expected):
        print("Test for " + str(actual) + " passed " if actual == expected else "Test for " + str(actual) + " failed, expected: " + str(expected))


Test.test_function(EvilOrOdious.evil(1),"It's Odious!")
Test.test_function(EvilOrOdious.evil(2),"It's Odious!")
Test.test_function(EvilOrOdious.evil(3),"It's Evil!")

bin(3)
"{0:b}".format(3)
type("{0:b}".format(42))