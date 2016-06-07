line ="+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
"""
In Hong Kong, a valid phone number has the format xxxx xxxx where x is a decimal digit (0-9). For example:

"1234 5678" // is valid
"2359 1478" // is valid
"85748475" // invalid, as there are no spaces separating the first 4 and last 4 digits
"3857  4756" // invalid; there should be exactly 1 whitespace separating the first 4 and last 4 digits respectively
"sklfjsdklfjsf" // clearly invalid
"     1234 5678   " // is NOT a valid phone number but CONTAINS a valid phone number
"skldfjs287389274329dklfj84239029043820942904823480924293042904820482409209438dslfdjs9345 8234sdklfjsdkfjskl28394723987jsfss2343242kldjf23423423SDLKFJSLKsdklf" // also contains a valid HK phone number (9345 8234)
Task

Define two functions, isValidHKPhoneNumber and hasValidHKPhoneNumber, that returns whether a given string is a valid HK phone number and contains a valid HK phone number respectively (i.e. true/false values).

"""
def is_valid_HK_phone_number(number):
    #check if a space is at the end or at the beginning
    if number.startswith(" ") or number.endswith(" "):
        return False
    #if there are spaces in the middle or none at all
    elif number.count(" ") == 2 or number.count(" ") == 0:
        return False
    #check for validity of numbers
    else:
        nList = number.split()
        if nList[0].isdigit() and len(nList[0]) == 4:
            return True
        elif nList[1].isdigit() and len(nList[1]) == 4:
            return True
        else:
            return False

def has_valid_HK_phone_number(number):

    return filter(lambda x:x.isdigit(),number)

print ("Testing for is_valid_HK_phone_number method")
print is_valid_HK_phone_number("1234 5678") # True passed
print is_valid_HK_phone_number("2359 1478") #True passed
print is_valid_HK_phone_number("85748475")  #False passed
print is_valid_HK_phone_number("3857  4756") #False passed
print is_valid_HK_phone_number("sklfjsdklfjsf") #False passed
print is_valid_HK_phone_number("     1234 5678   ") #False passed
print is_valid_HK_phone_number("123456789") #False passed
print is_valid_HK_phone_number(" 987 634 ") #False passed
print is_valid_HK_phone_number("    6    ") #False passed
print is_valid_HK_phone_number("9684 2396") #True passed
print is_valid_HK_phone_number("0000 0000") #True passed
print is_valid_HK_phone_number("abcd efgh") #False passed
print is_valid_HK_phone_number("836g 2986") #False passed
print is_valid_HK_phone_number("8A65 2986") #False passed
print is_valid_HK_phone_number("8c65 2i86") #False passed
print is_valid_HK_phone_number("8368 2aE6") #False passed
print is_valid_HK_phone_number("83680 28968") #False passed
print("-------------------------------------------------")
print ("Testing for has_valid_HK_phone_number method")

print(has_valid_HK_phone_number("Hello, my phone number is 1234 5678")) #True
print(has_valid_HK_phone_number("I wonder if 2359 1478 is a valid phone number?")) #True
print(has_valid_HK_phone_number("85748475 is definitely invalid"))#False
print(has_valid_HK_phone_number("'3857  4756' is so close to a valid phone number!"))#False
print(has_valid_HK_phone_number("sklfjsdklfjsf"))# False
print(has_valid_HK_phone_number("     1234 5678   ")) # True
print(has_valid_HK_phone_number("What about abcd efgh?"))#False
print(has_valid_HK_phone_number("What about 9684 2396?")) #True)
print(has_valid_HK_phone_number("And 836g 2986?")) #False)
print(has_valid_HK_phone_number("skldfjsdklfjs0000 0000skldfjslkdfjs"))#True)
print(has_valid_HK_phone_number("123456789 is invalid")) #False
print(has_valid_HK_phone_number("sdfssdfsdfdf 987 634 sdfsddsds"))#False
print(has_valid_HK_phone_number("\n\n    6    \n\n")) #False
print(has_valid_HK_phone_number("sdfsdsdfdf8A65 2986sdfsddfs"))#False
print(has_valid_HK_phone_number("iwoeurwoeuwo8368 2aE6"))#False
print(has_valid_HK_phone_number("8c65 2i86wioeruwioeruweoi"))#False

print("-------------------------------------------------")
"""
This should be fairly simple. It is more of a puzzle than a programming problem.
There will be a string input in this format: 'a+b' 2 lower case letters (a-z) seperated by a '+'
Return the sum of the two variables.
There is one correct answer for a pair of variables.
I know the answers, it is your task to find out.
Once you crack the code for one or two of the pairs, you will have the answer for the rest.
It is like when you were in school doing math and you saw "11 = c+h" and you needed to find out what c and h were.
However you don't have an 11. You have an unknown there as well. Example:
X = a+b.
You don't know what X is, and you don't know what b is or a, but it is a puzzle and you will find out.
As part of this puzzle, there is three hints or clues on solving this. I won't tell you what the other two are, but one of them is: Don't overthink it. It is a simple solution
Given the input as a string - Return the sum of the two variables as int.
"""

print ord("d")-96
print ord("g")-96
def the_var(var):
    n = [ord(i)-96 for i in var.split("+")]
    return sum(n)

print the_var("d+g")

"""
You'll be given a string, and have to return the total of all the unicode characters as an int. Should be able to handle any characters sent at it.
examples:
uniTotal("a") == 97 uniTotal("aaa") == 291
"""

def uni_total(string):
    return sum([ord(i) for i in string])

print line
print uni_total("a") # 97)
print uni_total("b") # 98)
print uni_total("c") # 99)
print uni_total("") #0)
print uni_total("aaa")#, 291)
print uni_total("abc")# 294)
print uni_total("Mary Had A Little Lamb")#,1873)
print uni_total("Mary had a little lamb")#,2001)
print uni_total("CodeWars rocks")#1370)
print uni_total("And so does Strive")#,1661)
print line

"""
Write a module Converter that can take ASCII text and convert it to hexadecimal. The class should also be able to take hexadecimal and convert it to ASCII text.

Example

Converter.to_hex("Look mom, no hands")
=> "4c6f6f6b206d6f6d2c206e6f2068616e6473"

Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473")
=> "Look mom, no hands"
"""
import binascii
class Converter():
    @staticmethod
    def to_ascii(h):
        return bytearray.fromhex(h).decode()
    @staticmethod
    def to_hex(s):
        return binascii.hexlify(s)


s="Look mom, no hands"
h="4c6f6f6b206d6f6d2c206e6f2068616e6473"

print "Testing for Converter class"
print(Converter.to_hex(s))#,h)
print(Converter.to_ascii(h))#,s)
print(Converter.to_hex(Converter.to_ascii(h)))#,h)
print(Converter.to_ascii(Converter.to_hex(s)))#,s)
print line
"""
Make a program that takes a list of a random amount (but will always have atleast 1 number in) of numbers and returns the average, or mean, of the numbers. Also the program should return "Incorrect" if the value entered is a string.

(Use integer division to divide the numbers, (if you actually use the division method))

Ex: If input is [70, 70, 70, 70, 70] the program should return 70 (for obvious reasons)
"""
def average(x):
    return "Incorrect" if isinstance(x,str) else sum(x)/len(x)

print "Testing for average(x) function"
print(average("Hello please let me break your program") == "Incorrect")
print(average([70, 70])== 70)
print(average([40, 20, 5]) == 21)
print line

"""
Write a function that removes each 9 that it is in between 7s.

seven_ate9('79712312') => '7712312'
seven_ate9('79797') => '777'
Input: String Output: String
"""

import re
def seven_ate9(sevens):
    return re.sub(r"7+9(?=7)","7",sevens)


print "TESTING FOR seven_ate9(sevens) function"
print "Actual: " + seven_ate9('165561786121789797'), "Expected: "+'16556178612178977',seven_ate9('165561786121789797')=='16556178612178977'
print "Actual: " + seven_ate9('797') ,"Expected: " + "77",seven_ate9('797') == "77"
print "Actual: " + seven_ate9('7979797'),"Expected: " + "7777", seven_ate9('7979797')=='7777'
print line



"""
Make a program that will take an int (x) and give you the summation of all numbers from 1 up to x included. If the given input is not an integer, return "Error 404".

Examples:

summation(25)==325
summation(2.56)=="Invalid Value"
"""
def summation(x):
    return sum(range(1,x+1)) if isinstance(x,int) else "Error 404"

print("Actual:",summation(10),"Expected:",55, summation(10) == 55)
print(summation(5) == 15)
print(summation("538") == "Error 404")
print(summation(67.9) == "Error 404")
print line

"""
using n as a parameter in the calling function pattern, where n should be a natural number; complete the codes to get the pattern (take the help of examples). There is no newline in the end (after the pattern ends).

Examples

pattern(3):

1
1*2
1**3
pattern(10):

1
1*2
1**3
1***4
1****5
1*****6
1******7
1*******8
1********9
1*********10
"""
def pattern(n):
    return '\n'.join(['1'] + ['1' + '*' * (i - 1) + str(i) for i in xrange(2, n + 1)])

print("Testing for pattern(n) function")
print("Actual:",pattern(3),"Expected:","1\n1*2\n1**3")
print("Actual:",pattern(7),"Expected:","1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7")
print("Actual:",pattern(20),"Expected:","1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7\n1*******8\n1********9\n1*********10\n1**********11\n1***********12\n1************13\n1*************14\n1**************15\n1***************16\n1****************17\n1*****************18\n1******************19\n1*******************20")

print line

"""
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"

"""
import re
def maskify(cc):
    return cc if len(cc) <=4 else re.sub(r'.',r'#',cc[:-4]) + cc[len(cc) - 4:]


print "Testing for maskify(cc) function"
print "Actual:",maskify("4556364607935616"),"Expected:", "############5616", maskify("4556364607935616") == "############5616"
print maskify("64607935616") ==      "#######5616"
print maskify("1") =="1"
print maskify("") ==  ""
print maskify("Skippy")== "##ippy"
print maskify("Nananananananananananananananana Batman!") == "####################################man!"
print maskify("123")