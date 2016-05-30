line = "----------------------------------------------------------------------------------------------------------------"
"""
For a variable, x, that may have different values, the geometric mean is defined as:
gm = nthRoot(x1x2x3....xn)
Suposse that you have to calculate the geometric mean for a research where the amount of values of x is rather small.

Implement the function geometric_meanI(), (geometricMeanI javascript)that receives an array with the different values of the variable and outputs the geometric mean value.

The negative values and strings will be discarded for the calculations.

Nevertheless if the amount of total invalid values is too high, the function will return 0. The tolerance for invalid values of the variable will be as follows:

amount of entries      maximum invalid entries
  2 - 10                       1
  From 11 and above      10 % of total of entries
You do not have to round the results.

"""
def geometric_meanI(arr):
    # find the strings and negative values and count them
    strNeg = [x for x in arr if isinstance(x,str) or x < 0]
    strNegCount = len(strNeg)
    if len(arr)<=10:
        #check count for invalid entries, only perform calculation if they are less than or equal to one
        if strNegCount <= 1:
            n = [int(i) for i in arr if isinstance(i,int) and i>=0]
            l = len(n)
            m = reduce(lambda x,y:x*y,n)
            gm = pow(m,1/float(l))
            return gm
        else:
            return 0
    else:
        if strNegCount <= int(0.1*len(arr)):
            n = [i for i in arr if isinstance(i,int) and i >= 0]
            l = len(n)
            m = reduce(lambda x, y: x * y, n)
            gm = pow(m, 1 / float(l))
            return gm
        else:
            return 0

print "Test cases for geometric_meanI(arr) function"
print geometric_meanI([2, 3, 4, 6])# 3.46410161514)
print geometric_meanI([2, 3, 4, 6, -5])#3.46410161514)
print geometric_meanI([2, 3, 4, 6, '5'])# 3.46410161514)
print geometric_meanI([2, 2, 3, 4, 10, 8, 1, 4, 6, 7, 2])# 3.59348221822)
print geometric_meanI([2, 2, 3, 4, 10, -4, 8, 1, 4, 6, 7, 2])#3.59348221822)
print geometric_meanI([2, 2, 3, 0, 4, 10, -4, 8, 1, 4, 6, 7, 2])# 0.0)
print geometric_meanI([2, 3, 4, 6, - 5, '5'])# 0)
print geometric_meanI([2, 2, 3, 4, 10, -4, 8, 1, 4, 6, 7, 2, ''])# 0)
print geometric_meanI([1, 13, 9, 11, 36, 37, 41, 33, 18, 17, 15, 37, 32, -3, 1, 3, 5, 22, 18, -3])
print line

"""
Description:

Input : an array of integers.
Output : this array, but sorted in such a way that there are two wings:

the left wing with numbers decreasing,
the right wing with numbers increasing.
the two wings have the same length. If the length of the array is odd the wings are around the bottom, if the length is even the bottom is considered to be part of the right wing.
each integer l of the left wing must be greater or equal to its counterpart r in the right wing, the difference l - r being as small as possible. In other words the right wing must be nearly as steeply as the left wing.
The function is make_valley or makeValley or make-valley.

a = [79, 35, 54, 19, 35, 25]
make_valley(a) --> [79, 35, 25, *19*, 35, 54]
The bottom is 19, left wing is [79, 35, 25], right wing is [*19*, 35, 54].
79..................54
    35..........35
        25.
          ..19

a = [67, 93, 100, -16, 65, 97, 92]
make_valley(a) --> [100, 93, 67, *-16*, 65, 92, 97]
The bottom is -16, left wing [100, 93, 67] and right wing [65, 92, 97] have same length.
100.........................97
    93..........
               .........92
        67......
               .....65
            -16

a = [66, 55, 100, 68, 46, -82, 12, 72, 12, 38]
make_valley(a) --> [100, 68, 55, 38, 12, *-82*, 12, 46, 66, 72]
The bottom is -82, left wing is [100, 68, 55, 38, 12]], right wing is [*-82*, 12, 46, 66, 72].

a = [14,14,14,14,7,14]
make_valley(a) => [14, 14, 14, *7*, 14, 14]

a = [14,14,14,14,14]
make_valley(a) => [14, 14, *14*, 14, 14]
A counter-example:

a = [17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1]
A solution could be [17, 17, 15, 14, 8, 1, 4, 4, 5, 7, 7]
but the right wing [4, 4, 5, 7, 7] is much flatter than the left one
[17, 17, 15, 14, 8].

Summing the differences between left and right wing:
(17-7)+(17-7)+(15-5)+(14-4)+(8-4) = 44

Consider the following solution:
[17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17]
Summing the differences between left and right wing:
(17-17)+(15-14)+(8-7)+(7-5)+(4-4) = 4
The right wing is nearly as steeply than the right one.
Note:

Don't modify the input arr in your code... or make a copy of it before modifications.
"""
def make_valley(arr):
    sortArr = list(sorted(arr))
    leftWng = sortArr[::-2]
    del sortArr[len(sortArr) - 1]
    rightWng = sortArr[::-2]
    res = leftWng + list(reversed(rightWng))
    return res

print "Testing make_valley() function"
print "Arrays with an even length"
print make_valley([20, 18, 16, 15, 14, 14, 13, 13, 10, 9, 4, 4, 4, 1])# [20, 16, 14, 13, 10, 4, 4, 1, 4, 9, 13, 14, 15, 18])
print make_valley([20, 7, 6, 2])# [20, 6, 2, 7])
print make_valley([20, 20, 16, 14, 12, 12, 11, 10, 3, 2])#[20, 16, 12, 11, 3, 2, 10, 12, 14, 20])
print "Arrays with an odd length"
print make_valley([20, 16, 14, 10, 1])# [20, 14, 1, 10, 16])
print make_valley([20, 18, 17, 13, 12, 12, 10, 9, 4, 2, 2, 1, 1])# [20, 17, 12, 10, 4, 2, 1, 1, 2, 9, 12, 13, 18])
print make_valley([14, 10, 8])# [14, 8, 10])
print make_valley([17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1])# [17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17])
print make_valley([19, 19, 18, 14, 12, 11, 9, 7, 4])# [19, 18, 12, 9, 4, 7, 11, 14, 19])
print make_valley([19, 8, 6])# [19, 6, 8])
print make_valley([19, 17, 16, 15, 13, 8, 5, 5, 4, 4, 4])# [19, 16, 13, 5, 4, 4, 4, 5, 8, 15, 17])
print line