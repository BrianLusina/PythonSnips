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
