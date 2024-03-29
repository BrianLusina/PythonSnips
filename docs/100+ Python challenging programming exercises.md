Question:

Write a program to compute:

f(n)=f(n-1)+100 when n>0 and f(0)=1

with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.

Solution:

def f(n):
if n==0:
return 0 else:
return f(n-1)+100

n=int(raw_input())
print f(n)

# ----------------------------------------#

Question:

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

13

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.

Solution:

def f(n):
if n == 0: return 0 elif n == 1: return 1 else: return f(n-1)+f(n-2)

n=int(raw_input())
print f(n)

# ----------------------------------------#

# ----------------------------------------#

Question:

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n
input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13

Hints:
We can define recursive function in Python. Use list comprehension to generate a list from an existing list. Use
string.join() to join a list of strings.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

def f(n):
if n == 0: return 0 elif n == 1: return 1 else: return f(n-1)+f(n-2)

n=int(raw_input())
values = [str(f(x)) for x in range(0, n+1)]
print ",".join(values)

# ----------------------------------------#

Question:

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is
input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

def EvenGenerator(n):
i=0 while i<=n:
if i%2==0:
yield i i+=1

n=int(raw_input())
values = []
for i in EvenGenerator(n):
values.append(str(i))

print ",".join(values)

# ----------------------------------------#

Question:

Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma
separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

def NumGenerator(n):
for i in range(n+1):
if i%5==0 and i%7==0:
yield i

n=int(raw_input())
values = []
for i in NumGenerator(n):
values.append(str(i))

print ",".join(values)

# ----------------------------------------#

Question:

Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints:
Use "assert expression" to make assertion.

Solution:

li = [2,4,6,8]
for i in li:
assert i%2==0

# ----------------------------------------#

Question:

Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example:
If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38

Hints:
Use eval() to evaluate an expression.

Solution:

expression = raw_input()
print eval(expression)

# ----------------------------------------#

Question:

Please write a binary search function which searches an item in a sorted list. The function should return the index of
element to be searched in the list.

Hints:
Use if/elif to deal with conditions.

Solution:

import math def bin_search(li, element):
bottom = 0 top = len(li)-1 index = -1 while top>=bottom and index==-1:
mid = int(math.floor((top+bottom)/2.0))
if li[mid]==element:
index = mid elif li[mid]>element:
top = mid-1 else:
bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print bin_search(li,11)
print bin_search(li,12)

# ----------------------------------------#

Question:

Please write a binary search function which searches an item in a sorted list. The function should return the index of
element to be searched in the list.

Hints:
Use if/elif to deal with conditions.

Solution:

import math def bin_search(li, element):
bottom = 0 top = len(li)-1 index = -1 while top>=bottom and index==-1:
mid = int(math.floor((top+bottom)/2.0))
if li[mid]==element:
index = mid elif li[mid]>element:
top = mid-1 else:
bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print bin_search(li,11)
print bin_search(li,12)

# ----------------------------------------#

Question:

Please generate a random float where the value is between 10 and 100 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].

Solution:

import random print random.random()*100

# ----------------------------------------#

Question:

Please generate a random float where the value is between 5 and 95 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].

Solution:

import random print random.random()*100-5

# ----------------------------------------#

Question:

Please write a program to output a random even number between 0 and 10 inclusive using random module and list
comprehension.

Hints:
Use random.choice() to a random element from a list.

Solution:

import random print random.choice([i for i in range(11) if i%2==0])

# ----------------------------------------#

Question:

Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random
module and list comprehension.

Hints:
Use random.choice() to a random element from a list.

Solution:

import random print random.choice([i for i in range(201) if i%5==0 and i%7==0])

# ----------------------------------------#

Question:

Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.

Solution:

import random print random.sample(range(100), 5)

# ----------------------------------------#

Question:

Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.

Solution:

import random print random.sample([i for i in range(100,201) if i%2==0], 5)

# ----------------------------------------#

Question:

Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000
inclusive.

Hints:
Use random.sample() to generate a list of random values.

Solution:

import random print random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5)

# ----------------------------------------#

Question:

Please write a program to randomly print a integer number between 7 and 15 inclusive.

Hints:
Use random.randrange() to a random integer in a given range.

Solution:

import random print random.randrange(7,16)

# ----------------------------------------#

Question:

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.

Solution:

import zlib s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print t print zlib.decompress(t)

# ----------------------------------------#

Question:

Please write a program to print the running time of execution of "1+1" for 100 times.

Hints:
Use timeit() function to measure the running time.

Solution:

from timeit import Timer t = Timer("for i in range(100):1+1")
print t.timeit()

# ----------------------------------------#

Question:

Please write a program to shuffle and print the list [3,6,7,8].

Hints:
Use shuffle() function to shuffle a list.

Solution:

from random import shuffle li = [3,6,7,8]
shuffle(li)
print li

# ----------------------------------------#

Question:

Please write a program to shuffle and print the list [3,6,7,8].

Hints:
Use shuffle() function to shuffle a list.

Solution:

from random import shuffle li = [3,6,7,8]
shuffle(li)
print li

# ----------------------------------------#

Question:

Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and
the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.

Solution:

subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
for j in range(len(verbs)):
for k in range(len(objects)):
sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
print sentence

# ----------------------------------------#

Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.

Solution:

li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print li

# ----------------------------------------#

Question:

By using list comprehension, please write a program to print the list after removing delete numbers which are divisible
by 5 and 7 in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.

Solution:

li = [12,24,35,70,88,120,155]
li = [x for x in li if x%5!=0 and x%7!=0]
print li

# ----------------------------------------#

Question:

By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers
in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.

Solution:

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print li

# ----------------------------------------#

Question:

By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

Hints:
Use list comprehension to make an array.

Solution:

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print array

# ----------------------------------------#

Question:

By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers
in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.

Solution:

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print li

# ----------------------------------------#

Question:

By using list comprehension, please write a program to print the list after removing the value 24
in [12,24,35,24,88,120,155].

Hints:
Use list's remove method to delete a value.

Solution:

li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print li

# ----------------------------------------#

Question:

With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are
intersection of the above given lists.

Hints:
Use set() and "&=" to do set intersection operation.

Solution:

set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2 li=list(set1)
print li

# ----------------------------------------#

With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate
values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.

Solution:

def removeDuplicate( li ):
newli=[]
seen = set()
for item in li:
if item not in seen:
seen.add( item )
newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print removeDuplicate(li)

# ----------------------------------------#

Question:

Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can
print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.

Solution:

class Person:
def getGender( self ):
return "Unknown"

class Male( Person ):
def getGender( self ):
return "Male"

class Female( Person ):
def getGender( self ):
return "Female"

aMale = Male()
aFemale= Female()
print aMale.getGender()
print aFemale.getGender()

# ----------------------------------------#

Question:

Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2 c,2 b,2 e,1 d,1 g,1 f,1

Hints:
Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.

Solution:

dic = {} s=raw_input()
for s in s:
dic[s] = dic.get(s,0)+1 print '\n'.join(['%s,%s' % (k, v) for k, v in dic.items()])

# ----------------------------------------#

Question:

Please write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

Hints:
Use list[::-1] to iterate a list in a reverse order.

Solution:

s=raw_input()
s = s[::-1]
print s

# ----------------------------------------#

Question:

Please write a program which accepts a string from console and print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

Hints:
Use list[::2] to iterate a list by step 2.

Solution:

s=raw_input()
s = s[::2]
print s

# ----------------------------------------#

Question:

Please write a program which prints all permutations of [1,2,3]

Hints:
Use itertools.permutations() to get permutations of list.

Solution:

import itertools print list(itertools.permutations([1,2,3]))

# ----------------------------------------#

Question:

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we
have?

Hint:
Use for loop to iterate all possible solutions.

Solution:

def solve(numheads,numlegs):
ns='No solutions!'
for i in range(numheads+1):
j=numheads-i if 2*i+4*j==numlegs:
return i,j return ns,ns

numheads=35 numlegs=94 solutions=solve(numheads,numlegs)
print solutions

# ----------------------------------------#


