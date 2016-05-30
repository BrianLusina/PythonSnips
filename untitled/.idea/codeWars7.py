line = "========================================================================"
"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""
from itertools import groupby
def unique_in_order(lst):
    return [k for k, g in groupby(lst)]

"""
 Alternatively
 prev = object()
    for item in lst:
        if item != prev:
            prev = item
            yield item
"""

print "Testing for unique_in_order(iterable)"
print unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
print unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
print unique_in_order([1,2,2,3,3]) == [1,2,3]
print line


"""
Calculate the sum of all the arguments passed to a function.

Note: If any of the arguments is not a finite number the function should return false/False instead of the sum of the arguments.

For example:

sum(1,2,3,4)         should return 10
sum(1, "two", 3)     should return false
sum(1, 2, [3], NaN)  should return false
"""
def sum_all(*args):
    total = 0
    for i in args:
        if isinstance(i,int):
            total+=i
        else:
            return False
    return total

print("Testing for sum_all() function")
print (sum_all(6,2,3) == 11)
print (sum_all(756,2,1,10) == 769)
print (sum_all(76856,-32,1981,1076) ==79881)
print (sum_all(1,-32,"codewars",1076) == False)
print (sum_all(7,-3452,1981,1076) == -388)
print line
"""
Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".
"""
def problem(a):
    return "Error" if isinstance(a,str) else (a*50)+6

print(problem("hello")== "Error")
print(problem(1) == 56)
print line

"""
Terminal game turn function

You are creating a text-based terminal version of your favorite board game. In the board game, each turn has six steps that must happen in this order: roll the dice, move, combat, get coins, buy more health, and print status.

You are using a library that already has the functions below. Create a function named doTurn/do_turn that calls the functions in the proper order as described in the paragraph above.

- `combat`
- `buy_health`
- `get_coins`
- `print_status`
- `roll_dice`
- `move`
"""
def do_turn():
    m= ["combat","buy_health","get_coins","print_status","roll_dice","move"]
    for i in m:
        print i

