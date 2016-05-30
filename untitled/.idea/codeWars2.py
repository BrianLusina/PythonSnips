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
Instructions
A string is considered to be in title case if each word in the string is either
(a) capitalised (that is, only the first letter of the word is in upper case) or
(b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

Arguments (Other languages)

First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word
in the string.
Example

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
"""

def title_case(title, minor_words=None):
    t =title.title()
    if minor_words == None:
        return t
    else:
        c = 0
        while c < len(t.split()[1:]):
            e = [i.title() for i in minor_words.split()]
            m = [t.replace(i.title(), i.lower()) for i in e if i in t.split()[1:]]
            c+=1
        return "".join(m)


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