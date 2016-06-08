line = "----------------------------------------------------------------------------------------------------------------"
"""
Description:

Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need.

Example:
paperwork(5, 5) == 25
Note! if n or m < 0 return 0!
"""
def paperwork(n, m):
    return 0 if (n<0 or m<0) else n*m

"""
You must create a function, spread, that takes a function and a list of arguments to be applied to that function. You must make this function return the result of calling the given function/lambda with the given arguments.

eg:

spread(someFunction, [1, true, "Foo", "bar"] )
# is the same as...
someFunction(1, true, "Foo", "bar")
"""
def spread(func, args):
    return func(*args)
#alternatively
#spread=apply

print spread(lambda x,y:x*y,[2,2])
print line

"""
Description:

Python dictionaries are inherently unsorted. So what do you do if you need to sort the contents of a dictionary.

In this kata you will create a function that returns a sorted list of (key, value) tuples (Javascript: arrays of 2 items).

The list must be sorted by the value and be sorted largest to smallest.

Examples

sortDict({3:1,2:2,1:3}) == [[1,3],[2,2],[3,1]]
sortDict({1:2,2:4,3:6}) == [[3,6],[2,4],[1,2]]
"""
import operator
def sort_dict(d):
    return sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print "Testing for sort_dict(d) function"
print sort_dict({3:1,2:2,1:3}) == [(1,3),(2,2),(3,1)]
print sort_dict({1:2,2:4,3:6}) == [(3,6),(2,4),(1,2)]
print line

"""
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"
"""
import re

def order(sent):
    digits = lambda sent:int(sent) if sent.isdigit() else sent
    natural_keys = lambda x:[digits(x) for x in re.split('(\d+)', sent)]

    m = sent.split()
    m.sort(key = natural_keys)
    return " ".join(m)

print "Testing for order() function"
print order("is2 Thi1s T4est 3a") #== "Thi1s is2 3a T4est"
print line

"""
While developing a website, you detect that some of the members have troubles logging in. Searching through the code you find that all logins ending with a "_" make problems. So you want to write a function that takes an array of pairs of login-names and e-mails, and outputs an array of all login-name, e-mails-pairs from the login-names that end with "_".

If you have the input-array:

[ [ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
it should output

[ [ "bar_", "bar@bar.com" ] ]
You have to use the filter-method of Python, which returns each element of the array for which the filter-method returns true.
"""
def filterFnc(logins):
    res = []
    for x in logins:
        for i in x:
            if i[0].endswith("_"):
                res.append(i)
    return res

def search_names(logins):
    return filter(filterFnc,logins)

print("Testing for search_names(logins) function")
print(search_names([[ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]) == [ [ "bar_", "bar@bar.com" ] ])
print(search_names([[ "foobar_", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]) == [[ "foobar_", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ])
print (search_names([[ "foo", "foo@foo.com" ], [ "bar", "bar@bar.com" ] ]) == [])
print line



"""
Task:

You have to write a function pattern which returns the following Pattern(See Pattern & Examples) upto n number of rows.

Note:Returning the pattern is not the same as Printing the pattern.
Rules/Note:

If n < 1 then it should return "" i.e. empty string.
There are no whitespaces in the pattern.
Pattern:

(n)(n-1)(n-2)...4321
(n)(n-1)(n-2)...432
(n)(n-1)(n-2)...43
(n)(n-1)(n-2)...4
...............
..............
(n)(n-1)(n-2)
(n)(n-1)
(n)
Examples:

pattern(4):

4321
432
43
4
pattern(11):

1110987654321
111098765432
11109876543
1110987654
111098765
11109876
1110987
111098
11109
1110
11
Hint: Use \n in string to jump to next line
"""
def pattern(n):
    if n < 1:
        return ""
    else:
        m = [i for i in range(1, n + 1)]


print("Testing pattern(n) function")
print(pattern(1) == "1")
print(pattern(2) == "21\n2")
print(pattern(5) == "54321\n5432\n543\n54\n5")
print(line)

n=[range(1,i+1) for i in range(1, 5 + 1)]
print(n)

"""
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, and u as vowels for this Kata.
"""
def getCount(inputStr):
    v = ["a","e","i","o","u"]
    c = [inputStr.count(i) for i in v if i in inputStr.lower()]
    return sum(c)
print("Test for getCount() function")
print (getCount("abracadabra")==5)
print line

"""
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works (Ruby example given):

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
"""

def digital_root(num):
    return num if num<10 else digital_root(sum(map(int, str(num))))

print digital_root(493193) #2
print digital_root(132189) #6
print digital_root(942) #6
print digital_root(16) #7
print digital_root(123456789) #9
print digital_root(12345678910111223141516171819) #2

print line

"""
Description:

Write a function that accepts a string, and returns true if it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)

Examples:

validPhoneNumber("(123) 456-7890")  =>  returns true
validPhoneNumber("(1111)555 2345")  => returns false
validPhoneNumber("(098) 123 4567")  => returns false
"""
import re
def validPhoneNumber(phoneNum):
    expr = r"^\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4}$"
    return bool(re.match(expr,phoneNum))

print (validPhoneNumber("(123) 456-7890") == True)
print (validPhoneNumber("(1111)555 2345") == False)
print (validPhoneNumber("(098) 123 4567") == False)
print(validPhoneNumber("(1a3) 456-7890")== False)
print(validPhoneNumber("(123) 456-7fg0")==False)
print(validPhoneNumber("(12c) 4th6-7890")== False)
print line

