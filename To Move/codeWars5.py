# -*- coding: utf-8 -*-

line = "************************************************************************************************"
"""
wallpaper(4, 3.5, 3) should return "ten"

Notes:

all rolls (even with incomplete width) are put edge to edge
0 <= l, w, h (floating numbers), it can happens that w x h x l is zero
the integer r (number of rolls) will always be less or equal to 20
"""
def wallpaper(l, w, h):
    wallArea = 2*((l*h)+(w*h))
    wallPaperArea = .52*(10*1.15)
    papers = wallArea/wallPaperArea
    return papers

print wallpaper(6.3, 4.5, 3.29) #"sixteen"
print wallpaper(7.8, 2.9, 3.29) #"sixteen"
print wallpaper(6.3, 5.8, 3.13) #"seventeen"
print wallpaper(6.1, 6.7, 2.81) #"sixteen"
print line

"""
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
Detective, we're hot on their trail! We have a big pile of encoded messages here to use as evidence, but it would take way too long to decode by hand. Could you write a program to do this for us?

Write a funciton called decode(). Given an encoded string, return the actual phone number in string form. Don't worry about input validation, parenthesies, or hyphens.
"""
def decode(string):
    d = {1:9, 2:8, 3:7, 4:6, 5:0,9:1, 8:2, 7:3, 6:4, 0:5}
    m = [str(d.get(int(i))) for i in string]
    return "".join(m)


print decode("4103432323")# "6957678787")
print decode("4103438970")# "6957672135")
print decode("4104305768")# "6956750342")
print decode("4102204351")# "6958856709")
print decode("4107056043")# "6953504567")
print line

"""
In some scripting languages like PHP, there exists a logical operator (e.g. &&, ||, and, or, etc.) called the "Exclusive Or" (hence the name of this Kata). The exclusive or evaluates two booleans. It then returns true if exactly one of the two expressions are true, false otherwise. For example:

false xor false == false // since both are false
true xor false == true // exactly one of the two expressions are true
false xor true == true // exactly one of the two expressions are true
true xor true == false // Both are true.  "xor" only returns true if EXACTLY one of the two expressions evaluate to true.
Task

Since we cannot define keywords in Javascript (well, at least I don't know how to do it), your task is to define a function xor(a, b) where a and b are the two expressions to be evaluated. Your xor function should have the behaviour described above, returning true if exactly one of the two expressions evaluate to true, false otherwise.
"""

def xor(a,b):
    return a!=b
print xor(False, False) #False, "False xor False == False")
print xor(True, False) #, True, "True xor False == True")
print xor(False, True) #, True, "False xor True == True")
print xor(False, xor(False, False)) # False)
print xor(xor(True, False), False) # True)
print xor(True, True) # False, "True xor True == False")
print xor(xor(True, True), False) #False)
print xor(True, xor(True, True)) # True)
print xor(xor(False, False), xor(False, False)) #False)
print xor(xor(False, False), xor(False, True)) #True)
print xor(xor(True, False), xor(False, False)) #True)
print xor(xor(True, False), xor(True, False)) #False)
print xor(xor(True, True), xor(True, False)) #True)
print xor(xor(True, xor(True, True)), xor(xor(True, True), False)) #True)
print line


"""
For a given positive integer convert it into its English representation. All words are lower case and are separated with one space. No trailing spaces are allowed.

To keep it simple, hyphens and the writing of the word 'and' both aren't enforced. (But if you are looking for some extra challenge, fch an output will pass the tests.)

Large number reference: http://en.wikipedia.org/wiki/Names_of_large_numbers (U.S., Canada and modern British)

Input range: 1 -> 10**26 (10**16 for JS)

Examples:

intToEnglish(1) == 'one'

intToEnglish(10) == 'ten'

intToEnglish(25161045656) == 'twenty five billion one hundred sixty one million forty five thousand six hundred fifty six'
or

intToEnglish(25161045656) == 'twenty five billion one hundred
"""

def int_to_english(num,join=True):
    '''words = {} convert an integer number into words'''
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', \
             'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', \
            'eighty', 'ninety']
    thousands = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', \
                 'quintillion', 'sextillion', 'septillion', 'octillion', \
                 'nonillion', 'decillion', 'undecillion', 'duodecillion', \
                 'tredecillion', 'quattuordecillion', 'sexdecillion', \
                 'septendecillion', 'octodecillion', 'novemdecillion', \
                 'vigintillion']
    words = []
    if num == 0:
        words.append('zero')
    else:
        numStr = '%d' % num
        numStrLen = len(numStr)
        groups = (numStrLen + 2) / 3
        numStr = numStr.zfill(groups * 3)
        for i in range(0, groups * 3, 3):
            h, t, u = int(numStr[i]), int(numStr[i + 1]), int(numStr[i + 2])
            g = groups - (i / 3 + 1)
            if h >= 1:
                words.append(units[h])
                words.append('hundred')
            if t > 1:
                words.append(tens[t])
                if u >= 1: words.append(units[u])
            elif t == 1:
                if u >= 1:
                    words.append(teens[u])
                else:
                    words.append(tens[t])
            else:
                if u >= 1: words.append(units[u])
            if (g >= 1) and ((h + t + u) > 0): words.append(thousands[g])
    if join: return ' '.join(words)
    return words


print int_to_english(15) #'fifteen', "'fifteen' expected")
print int_to_english(47) #'forty seven' or int_to_english(47) == 'forty-seven', "'forty seven' or 'forty-seven' expected")
print int_to_english(536) #== 'five hundred thirty six' or int_to_english(536) == 'five hundred and thirty-six', "'five hundred thirty six' or 'five hundred and thirty-six' expected")
print int_to_english(12356) #== 'twelve thousand three hundred fifty six' or int_to_english(12356) == 'twelve thousand three hundred and fifty-six', "'twelve thousand three hundred fifty six' or 'twelve thousand three hundred and fifty-six' expected")
print line

"""
Write a function that verifies provided argument is either an integer or a floating-point number, returning true if it is or false otherwise.

Pointers

Numeric quantities are signed (optionally when positive, e.g. "+5" is valid notation)
Floats less than 1 (not considering possible exponent!) can be written without a leading "0" (e.g. ".00001")
Order-of-magnitude (i.e. 10, 100, 1000, etc.) can be written in E notation (the exponent is also signed, optionally so if positive, e.g. all the following are valid 1e2, 1E2, 1e-2, 1E-2, 1e+2)
Probably obvious, but no spaces are allowed anywhere (we aim to represent a real-life number)
You can mix-n'-match any or all above pointers in any single numeric quantity
"""
def i_or_f(arr):
    if isinstance(int(arr),int) or isinstance(float(arr),float):
        return True
    else:
        return False

"""
print i_or_f('1')#, True)
print i_or_f('1.0')#, True)
print i_or_f('1e1')#, True)
print i_or_f('1E-1')#, True)
print i_or_f('1e+1')#, True)
"""
print line

"""
Sum of 'n' Numbers

sum_of_n (or SequenceSum.sumOfN in Java, SequenceSum.SumOfN in C#) takes an integer n and returns a List (an Array in Java/C#) of length abs(n) + 1. The List/Array contains the numbers in the arithmetic series produced by taking the sum of the consecutive integer numbers from 0 to n inclusive.

n can also be 0 or a negative value.
Wikipedia reference for abs value is available here.

Example:

5 -> [0, 1, 3, 6, 10, 15]

-5 -> [0, -1, -3, -6, -10, -15]

7 -> [0, 1, 3, 6, 10, 15, 21, 28]
"""
class Test(object):
    def __init__(self, n):
        self.n = n

    @staticmethod
    def test_function(actual, expected):
        print "Test for " + str(actual) + " passed " if actual == expected else "Test for " + str(actual) + " failed, expected " + str(expected)


def sum_of_n(n):
    count, result = 0, []
    while count < abs(n) + 1:
        result.append(sum(range(count+1)))
        count+=1
    if n<0:
        result = [-i for i in result]
    return result

print "Testing for sum_of_n(n) function"
Test.test_function(sum_of_n(3), [0, 1, 3, 6])
Test.test_function(sum_of_n(1), [0, 1])
Test.test_function(sum_of_n(0), [0])
Test.test_function(sum_of_n(-4), [0, -1, -3, -6, -10])
print line
"""
Description:

Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:

toWeirdCase( "String" );//=> returns "StRiNg"
toWeirdCase( "Weird string case" );//=> returns "WeIrD StRiNg CaSe"
"""
def caser(s):
    res = ""
    for i in list(enumerate(s)):
        if i[0] % 2 == 0:
            res += i[1].upper()
        else:res+=i[1].lower()
    return res

def to_weird_case(strng):
    res, lst = [],strng.split(" ")
    for x in lst:
        res.append(caser(x))
    return " ".join(res)

Test.test_function(to_weird_case('This'), 'ThIs')
Test.test_function(to_weird_case('is'), 'Is')
Test.test_function(to_weird_case('test'), 'TeSt')
Test.test_function(to_weird_case("This is a test"),"ThIs Is A TeSt")
print line
