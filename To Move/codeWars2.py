line = "================================================================================================================"
"""
Input: Array of elements
["h","o","l","a"]
Output: String with comma delimited elements of the array in th same order.
"h,o,l,a"
"""
def print_array(arr):
    return ",".join([str(i) for i in arr])

"""
Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised
to the number of digits of each numbers, so, for example:

multiply(3)==15
multiply(10)==250
multiply(200)==25000
multiply(0)==0
multiply(-3)==-15
"""
def multiply(n):
    return 5**len(str(n))*n if n>1 else (5**(len(str(n))-1))*n


"""
Write a function that takes a negative or positive integer,
which represents the number of minutes before (-) or after (+) Sunday midnight,
and returns the current day of the week and the current time in 24hr format ('hh:mm') as a string.

day_and_time(0)       should return 'Sunday 00:00'
day_and_time(-3)      should return 'Saturday 23:57'
day_and_time(45)      should return 'Sunday 00:45'
day_and_time(759)     should return 'Sunday 12:39'
day_and_time(1236)    should return 'Sunday 20:36'
day_and_time(1447)    should return 'Monday 00:07'
day_and_time(7832)    should return 'Friday 10:32'
day_and_time(18876)   should return 'Saturday 02:36'
day_and_time(259180)  should return 'Thursday 23:40'
day_and_time(-349000) should return 'Tuesday 15:20'
"""
from datetime import datetime
now= datetime.now()
#returns current date in the calender as an integer
print now.day
#returns the current day of the week as an integer e.g Monday is 0
print now.weekday()
print line

"""
There is a bus moving in the city, and it takes and drop some people in each bus stop.

You are provided a list (or array in JS) of integer array. Each integer array has two items which represent number of people get into bus (The first item) and number of people get off the bus (The second item).

The first integer array has 0 number in the second item, since the bus is empty in the first bus stop.

Your task is to return number of people in the bus after the last bus station. Take a look on the test cases :)

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.
"""
def number(bus_stops):
    return sum([i[0]-i[1] for i in bus_stops])

print("Testing for number(n) function")
print(number([[10,0],[3,5],[5,8]]) == 5)
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) ==17)
print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) ==21)
print line


"""
A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits.

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1634 (4 digits):
    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
The Challenge:
Your code must return true or false depending upon whether the given number is a Narcissistic number.
Error checking for text strings or other invalid inputs is not required, only valid integers will be passed into the function.
"""
def narcissistic(value):
    l = len(str(value)) #length of number
    return sum([pow(int(i), l) for i in str(value)]) == value


print "Testing for narcissistic(v) function"
print (narcissistic(7)== True) # '7 is narcissistic');
print(narcissistic(371)== True) #'371 is narcissistic');
print(narcissistic(122)== False) #'122 is not narcissistic')
print(narcissistic(4887)== False) #'4887 is not narcissistic')
print line


"""
Your goal in this kata is to implement an difference function, which subtracts one list from another.
It should remove all values from list a, which are present in list b.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]
"""
def array_diff(a, b):
    return [x for x in a if x not in b]

print(array_diff([1,2], [1])== [2])#, "a was [1,2], b was [1], expected [2]")
print(array_diff([1,2,2], [2])== [1])#, "a was [1,2,2], b was [2], expected [1]")
print(array_diff([], [1,2])== [])#, "a was [], b was [1,2], expected []")

print(array_diff([1,2,2], [1])== [2,2])#, "a was [1,2,2], b was [1], expected [2,2]")
print(array_diff([1,2,2], [])== [1,2,2])#, "a was [1,2,2], b was [], expected [1,2,2]")
print line

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
print "Actual:",group_check("()"),"Expected:",True, "Test Passed:",group_check("()") == True
print "Actual:",group_check("({"),"Expected:",False, "Test Passed:",group_check("({") == False
print line

d={"(":")","{":"}","[":"]","\"":"\""}
test = "()"
count = Counter(test)
print count
m =count.items()
print line
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

print year_days(0),year_days(0) == '0 has 366 days'
print year_days(-64),year_days(-64) == '-64 has 366 days'
print year_days(2016),year_days(2016)=='2016 has 366 days'
print year_days(1974),year_days(1974)=='1974 has 365 days'
print year_days(-10),year_days(-10)== '-10 has 365 days'
print year_days(666),year_days(666)== '666 has 365 days'
print year_days(1857),year_days(1857)== '1857 has 365 days'
print year_days(2000),year_days(2000)== '2000 has 366 days'
print year_days(-300),year_days(-300)== '-300 has 365 days'
print year_days(-1),year_days(-1)== '-1 has 365 days'
print line

"""
Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
c# Ghost ghost = new Gost(); ghost.GetColor(); // => "white" or "yellow" or "purple" or "red"
"""
import random,math
class Ghost(object):
    @classmethod
    def color(self):
        colors = ["red", "purple", "white", "yellow"]
        return colors[random.randint(0,3)]


ghost = Ghost
print ghost.color()
print line
