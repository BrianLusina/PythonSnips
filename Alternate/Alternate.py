"""
altERnaTIng cAsE <=> ALTerNAtiNG CaSe

Define String.prototype.toAlternatingCase (StringUtils.toAlternatingCase(String) in Java) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

Note to no Java langs

You must NOT alter the original string.
"""
import random
class Alternate(object):
    def __init__(self,string):
        self.string = string

    @staticmethod
    def to_alternating_case(string):
        return string.swapcase()


"Class to test truths of functions"
class Test(object):
    def __init__(self,n):
        self.n = n

    @staticmethod
    def test_function(actual,expected):
        print "Test for " + str(actual) + " passed " if actual == expected else "Test for " + str(actual) + " failed, expected " + str(expected)


Test.test_function(Alternate.to_alternating_case("hello world"), "HELLO WORLD")
Test.test_function(Alternate.to_alternating_case("HELLO WORLD"), "hello world")
Test.test_function(Alternate.to_alternating_case("hello WORLD"), "HELLO world")
Test.test_function(Alternate.to_alternating_case("HeLLo WoRLD"), "hEllO wOrld")
Test.test_function(Alternate.to_alternating_case("12345"), "12345")
Test.test_function(Alternate.to_alternating_case("1a2b3c4d5e"), "1A2B3C4D5E")
Test.test_function(Alternate.to_alternating_case("String.prototype.toAlternatingCase"), "sTRING.PROTOTYPE.TOaLTERNATINGcASE")
Test.test_function(Alternate.to_alternating_case(Alternate.to_alternating_case("Hello World")), "Hello World")

title = "altERnaTIng cAsE"
title = Alternate.to_alternating_case(title)
Test.test_function(Alternate.to_alternating_case(title), "ALTerNAtiNG CaSe")
title = Alternate.to_alternating_case(title)
Test.test_function(Alternate.to_alternating_case(title), "altERnaTIng cAsE")
title = Alternate.to_alternating_case(title)
Test.test_function(Alternate.to_alternating_case(title), "ALTerNAtiNG CaSe")
title = Alternate.to_alternating_case(title)
Test.test_function(Alternate.to_alternating_case(title), "altERnaTIng cAsE")
title = "altERnaTIng cAsE <=> ALTerNAtiNG CaSe"
title = Alternate.to_alternating_case(title)
Test.test_function(Alternate.to_alternating_case(title), "ALTerNAtiNG CaSe <=> altERnaTIng cAsE")
title = Alternate.to_alternating_case(title)
Test.test_function(Alternate.to_alternating_case(title), "altERnaTIng cAsE <=> ALTerNAtiNG CaSe")
title = Alternate.to_alternating_case(title)
Test.test_function(Alternate.to_alternating_case(title), "ALTerNAtiNG CaSe <=> altERnaTIng cAsE")
title = Alternate.to_alternating_case(title)
Test.test_function(Alternate.to_alternating_case(title), "altERnaTIng cAsE <=> ALTerNAtiNG CaSe")

n = random.randint(1,100)
lst = [1,2,3,4,5]
lst.append(n)
print lst
#print [i for i in [1,2,3,4,5].append(n)]