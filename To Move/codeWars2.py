"""
Your goal in this kata is to implement an difference function, which subtracts one list from another.
It should remove all values from list a, which are present in list b.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]
"""


def array_diff(a, b):
    return [x for x in a if x not in b]


print(array_diff([1, 2], [1]) == [2])  # , "a was [1,2], b was [1], expected [2]")
print(array_diff([1, 2, 2], [2]) == [1])  # , "a was [1,2,2], b was [2], expected [1]")
print(array_diff([], [1, 2]) == [])  # , "a was [], b was [1,2], expected []")

print(array_diff([1, 2, 2], [1]) == [2, 2])  # , "a was [1,2,2], b was [1], expected [2,2]")
print(array_diff([1, 2, 2], []) == [1, 2, 2])  # , "a was [1,2,2], b was [], expected [1,2,2]")


"""
In English and programming, groups can be made using symbols such as "()" and "{}" that change meaning. However, these groups must be closed in the correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for correct grouping. For instance, the following groups are done correctly:

({})
[[]()]
[{()}]
The next are done incorrectly
{(})
([]
[])
A correct string cannot close groups in the wrong order, open a group but fail to close it, or close a group before it is opened.
Your function will take an input string that may contain any of the symbols "()" "{}" or "[]" to create groups.
It should return True if the string is empty or otherwise grouped correctly, or False if it is grouped incorrectly.
"""
from collections import Counter
import re


def group_check(s):
    pass


print "Testing for group_check(s) function"
print "Actual:", group_check("()"), "Expected:", True, "Test Passed:", group_check("()") == True
print "Actual:", group_check("({"), "Expected:", False, "Test Passed:", group_check("({") == False


d = {"(": ")", "{": "}", "[": "]", "\"": "\""}
test = "()"
count = Counter(test)
print count
m = count.items()

"""
A variation of determining leap years, assuming only integers are used and years can be negative and positive.

Write a function which will return the days in the year and the year entered in a string. For example 2000, entered as an integer, will return as a string 2000 has 366 days

There are a few assumptions we will accept the year 0, even though there is no year 0 in the Gregorian Calendar.

Also the basic rule for validating a leap year are as follows

Most years that can be divided evenly by 4 are leap years.

Exception: Century years are NOT leap years UNLESS they can be evenly divided by 400.

So the years 0, -64 and 2016 will return 366 days. Whilst 1974, -10 and 666 will return 365 days.
"""


def year_days(year):
    days = 365
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days += 1
    return "%d has %d days" % (year, days)


print year_days(0), year_days(0) == '0 has 366 days'
print year_days(-64), year_days(-64) == '-64 has 366 days'
print year_days(2016), year_days(2016) == '2016 has 366 days'
print year_days(1974), year_days(1974) == '1974 has 365 days'
print year_days(-10), year_days(-10) == '-10 has 365 days'
print year_days(666), year_days(666) == '666 has 365 days'
print year_days(1857), year_days(1857) == '1857 has 365 days'
print year_days(2000), year_days(2000) == '2000 has 366 days'
print year_days(-300), year_days(-300) == '-300 has 365 days'
print year_days(-1), year_days(-1) == '-1 has 365 days'


"""
Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
c# Ghost ghost = new Gost(); ghost.GetColor(); // => "white" or "yellow" or "purple" or "red"
"""
import random, math


class Ghost(object):
    @classmethod
    def color(self):
        colors = ["red", "purple", "white", "yellow"]
        return colors[random.randint(0, 3)]


ghost = Ghost
print ghost.color()

