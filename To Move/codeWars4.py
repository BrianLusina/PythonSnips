"""
You are the judge at a competitive eating competition and you need to choose a winner!

There are three foods at the competition and each type of food is worth a different amount of points. Points are as follows:

Chickenwings: 5 points
Hamburgers: 3 points
Hotdogs: 2 points
Write a function that helps you create a scoreboard. It takes as a parameter a list of objects representing the participants, for example:

[
  {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
  {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
]
It should return "name" and "score" properties sorted by score; if scores are equals, sort alphabetically by name.

[
  {name: "Big Bob", score: 134},
  {name: "Habanero Hillary", score: 98}
]
"""
def scoreboard(lst):
    total,scores,finalLst = 0,{},[]
    if len(lst) == 0:
        return lst
    else:
        for i in lst:
            total= (i.get("chickenwings") * 5)+(i.get("hamburgers") * 3)+(i.get("hotdogs") * 2)
            scores["score"] = total
            scores["name"] = i.get("name")
            finalLst.append(scores.copy())
            newlist = sorted(finalLst, key=lambda k: k['score'],reverse=True)

        return newlist


print(scoreboard([{"name": "Billy The Beast", "chickenwings": 17 , "hamburgers": 7, "hotdogs": 8},
                  {"name": "Habanero Hillary", "chickenwings": 5 , "hamburgers": 17, "hotdogs": 11},
                  {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},
                  {"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}
                  ]))

"""
  [{"name": "Big Bob", "score": 134},
   {"name": "Billy The Beast", "score": 122},
   {"name": "Habanero Hillary", "score": 98},
   {"name": "Joey Jaws", "score": 94}]
"""

print(scoreboard([{"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]))
      #[{"name": "Big Bob", "score": 134}])

print(scoreboard([
    {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},{"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]))
    #[{"name": "Big Bob", "score": 134},{"name": "Joey Jaws", "score": 94}]

print(scoreboard([
    {"name": "Joey Jaws", "chickenwings": 0, "hamburgers": 1, "hotdogs": 1},
    {"name": "Big Bob" , "chickenwings": 1, "hamburgers": 0, "hotdogs": 0}]))
    #[{"name": "Big Bob", "score": 5},{"name": "Joey Jaws", "score": 5}])

print(scoreboard([]), [])

"""
JavaScript provides a built-in parseInt method.

It can be used like this:

parseInt("10") returns 10
parseInt("10 apples") also returns 10
We would like it to return "NaN" (as a string) for the second case because the input string is not a valid number.

You are asked to write a myParseInt method with the following rules:

It should make the conversion if the given string only contains a single integer value (and eventually spaces - including tabs, line feeds... - at both ends)
For all other strings (including the ones representing float values), it should return NaN
It should assume that all numbers are not signed and written in base 10
"""
def my_parse_int(string):
    return int(string) if string.replace(" ","").isdigit() else "NaN"


print(my_parse_int("1")) #1
print(my_parse_int("  1 ")) #1
print(my_parse_int("08")) #8
print(my_parse_int("5 friends"))# "NaN"
print(my_parse_int("16.5")) #"NaN"



"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20
"""
def positive_sum(arr):
    return sum([i for i in arr if i>0])


print(positive_sum([1,2,3,4,5])) #15
print(positive_sum([1,-2,3,4,5]))#13
print(positive_sum([-1,2,3,4,-5]))#9
print(positive_sum([]))#0
print(positive_sum([-1,-2,-3,-4,-5]))#0


"""

Let's look at the following generator:

def gen():
    for i in range(2):
        for j in range(3):
            yield (i, j)
If we print all yielded values, we'll get

(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
For a given parameter list N you must return an iterator, which goes through all possible tuples A, where Ai changes from 0 to Ni.
"""
def multiiter(*args):
    m = [i for i in args]
    lst = []
    if len(m) ==1:
        for i in range(m[0]):
            yield (i,)
    elif len(args) == 2:
        for i in range(m[0]):
            for x in range(m[1]):
                yield(i,x)

print list((multiiter(2,3)))

"""
Complete function saleHotdogs, function accept 1 parameters:n, n is the number of customers to buy hotdogs, different numbers have different prices (refer to the following table), return a number that the customer need to pay how much money.

+---------------+-------------+
|  numbers n    | price(cents)|
+---------------+-------------+
|n<5            |    100      |
+---------------+-------------+
|n>=5 and n<10  |     95      |
+---------------+-------------+
|n>=10          |     90      |
+---------------+-------------+
"""
def sale_hotdogs(n):
    if n == 0: return 0
    elif n < 5: return n*100
    elif n>=5 and n<10: return n*95
    elif n>=10: return n*90


print sale_hotdogs(0)#0)
print sale_hotdogs(1)#100)
print sale_hotdogs(2)#200)
print sale_hotdogs(3)#300)
print sale_hotdogs(4)#400)
print sale_hotdogs(5)#475)
print sale_hotdogs(9)#855)

print sale_hotdogs(10)#900)
print sale_hotdogs(11)#990)
print sale_hotdogs(100)#9000)


"""
Lucy loves to travel. Luckily she is a renowned computer scientist and gets to travel to international conferences using her department's budget.

Each year, Society for Exciting Computer Science Research (SECSR) organizes several conferences around the world. Lucy always picks one conference from that list that is hosted in a city she hasn't been to before, and if that leaves her with more than one option, she picks the conference that she thinks would be most relevant for her field of research.

Write a function conferencePicker that takes in two arguments:

citiesVisited, a list of cities that Lucy has visited before, given as an array of strings.
citiesOffered, a list of cities that will host SECSR conferences this year, given as an array of strings. citiesOffered will already be ordered in terms of the relevance of the conferences for Lucy's research (from the most to the least relevant).
The function should return the city that Lucy should visit, as a string.

Also note:

You should allow for the possibility that Lucy hasn't visited any city before.
SECSR organizes at least two conferences each year.
If all of the offered conferences are hosted in cities that Lucy has visited before, the function should return 'No worthwhile conferences this year!' (Nothing in Haskell)
Example:

citiesVisited = ['Mexico City','Johannesburg','Stockholm','Osaka','Saint Petersburg','London'];
citiesOffered = ['Stockholm','Paris','Melbourne'];

conferencePicker (citiesVisited, citiesOffered);
// ---> 'Paris'
"""
def conference_picker(citVisited, citOffered):
    citiesToConsider = [x for x in citOffered if x not in citVisited]
    if len(citiesToConsider)==0:
        return "No worthwhile conferences this year!"
    else:
        return citiesToConsider[0]


print conference_picker([], ['Philadelphia', 'Osaka', 'Tokyo', 'Melbourne']) # 'Philadelphia',
print conference_picker([], ['Brussels', 'Madrid', 'London']) # 'Brussels',
print conference_picker([], ['Sydney', 'Tokyo']) # 'Sydney',
print conference_picker(
    ['London', 'Berlin', 'Mexico City', 'Melbourne', 'Buenos Aires', 'Hong Kong', 'Madrid', 'Paris'],
    ['Berlin', 'Melbourne']) # 'No worthwhile conferences this year!',
print conference_picker(
    ['Beijing', 'Johannesburg', 'Sydney', 'Philadelphia', 'Hong Kong', 'Stockholm', 'Chicago', 'Seoul',
     'Mexico City', 'Berlin'], ['Stockholm', 'Berlin', 'Chicago']) # 'No worthwhile conferences this year!',

print conference_picker(
    ['Mexico City', 'Dubai', 'Philadelphia', 'Madrid', 'Houston', 'Chicago', 'Delhi', 'Seoul', 'Mumbai', 'Lisbon',
     'Hong Kong', 'Brisbane', 'Stockholm', 'Tokyo', 'San Francisco', 'Rio De Janeiro'], ['Lisbon', 'Mexico City'])
    #'No worthwhile conferences this year!'
print conference_picker(['Mexico City','Johannesburg','Stockholm','Osaka','Saint Petersburg','London'],['Stockholm','Paris','Melbourne']) #Paris


cV = ['Beijing', 'Johannesburg', 'Sydney', 'Philadelphia', 'Hong Kong', 'Stockholm', 'Chicago', 'Seoul',
     'Mexico City', 'Berlin']
cO = ['Stockholm', 'Berlin', 'Chicago']

citiesToConsider = [x for x in cO if x not in cV]
print citiesToConsider


"""
Given few numbers, you need to print out the digits that are not being used.

Example:

unused_digits(12, 34, 56, 78) # "09"
unused_digits(2015, 8, 26) # "3479"
Note:

Result string should be sorted
The test case won't pass Integer with leading zero
"""
def unused_digits(*args):
    m = sorted("".join([str(a) for a in args]))
    res = [str(i) for i in range(0,10) if str(i) not in m]
    return "".join(res)

print unused_digits(12, 34, 56, 78), "09"
print unused_digits(2015, 8, 26), "3479"
print unused_digits(276, 575), "013489"
print unused_digits(643), "0125789"
print unused_digits(864, 896, 744), "01235"
